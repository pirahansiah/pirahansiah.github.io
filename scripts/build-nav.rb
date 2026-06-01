#!/usr/bin/env ruby
# frozen_string_literal: true

# Parse Obsidian-style MOC (contents/site.md) → _data/nav.yml + assets/site-map.md
# Run before Jekyll build (see run.sh). No gem plugins required.

require "json"
require "yaml"
require "fileutils"

ROOT = File.expand_path("..", __dir__)
SITE_MD = File.join(ROOT, "contents", "site.md")
OUT_YML = File.join(ROOT, "_data", "nav.yml")
OUT_ASSET = File.join(ROOT, "assets", "site-map.md")
OUT_GRAPH = File.join(ROOT, "assets", "graph.json")

def strip_front_matter(text)
  return text unless text.start_with?("---\n")

  text.sub(/\A---\s*\n.*?\n---\s*\n/m, "")
end

def wiki_index
  @wiki_index ||= begin
    idx = {}
    Dir.glob(File.join(ROOT, "contents", "**", "*.md")).each do |path|
      base = File.basename(path, ".md")
      rel = path.sub("#{ROOT}/", "").sub(/\.md\z/, "")
      url = "/#{rel}/"
      idx[base.downcase] = url
      idx[rel.downcase] = url
      idx[rel.sub("contents/", "").downcase] = url
    end
    idx
  end
end

def normalize_url(url)
  return url if url.nil? || url.empty?
  return url if url.match?(%r{\A(https?:|#|mailto:)}i)

  url = url.sub(/\.md\z/i, "")
  url = "/#{url}" unless url.start_with?("/")
  url = "#{url}/" unless url.end_with?("/")
  url
end

def parse_inline(text)
  text = text.to_s.strip
  return { title: "", url: nil } if text.empty?

  if (m = text.match(/\A\[(.+?)\]\((.+?)\)\z/))
    return { title: m[1], url: normalize_url(m[2]) }
  end

  if (m = text.match(/\A\[\[(.+?)\|(.+?)\]\]\z/))
    return { title: m[2].strip, url: resolve_wiki(m[1].strip) }
  end

  if (m = text.match(/\A\[\[(.+?)\]\]\z/))
    ref = m[1]
    if ref.include?("|")
      path, label = ref.split("|", 2)
      return { title: label.strip, url: resolve_wiki(path.strip) }
    end
    return { title: ref, url: resolve_wiki(ref) }
  end

  { title: text, url: nil }
end

def resolve_wiki(ref)
  ref = ref.sub(/\.md\z/i, "")
  key = File.basename(ref).downcase
  found = wiki_index[key] || wiki_index[ref.downcase]
  return found if found

  normalize_url("/contents/#{ref}")
end

def attach_link_to_heading(ctx, title, url)
  heading = ctx[:last_heading]
  return unless heading
  return unless ctx[:last_heading_level] && ctx[:last_heading_level] >= 2
  return if heading["url"]

  heading["url"] = url
  heading["title"] = title if heading["title"].to_s.empty?
end

# Menu rules (Obsidian MOC):
#   #       → level 1 top menu only
#   ## ###  → submenu under their parent #
#   links on the line after ##/### attach to that heading (not separate menu items)
#   lists, tasks, and other lines are ignored for the menu (still in site-map body)
def parse_moc(text)
  menu = []
  ctx = {
    h1: nil,
    h2: nil,
    h3: nil,
    last_heading: nil,
    last_heading_level: nil
  }

  strip_front_matter(text).each_line do |raw|
    stripped = raw.strip
    next if stripped.empty? || stripped == "[]"

    if (m = stripped.match(/\A(#+)\s+(.+)\z/))
      level = m[1].length
      next unless [1, 2, 3].include?(level)

      info = parse_inline(m[2])
      node = { "title" => info[:title], "items" => [] }
      node["url"] = info[:url] if info[:url]

      case level
      when 1
        menu << node
        ctx[:h1] = node
        ctx[:h2] = ctx[:h3] = nil
      when 2
        next unless ctx[:h1]

        ctx[:h1]["items"] << node
        ctx[:h2] = node
        ctx[:h3] = nil
      when 3
        parent = ctx[:h2] || ctx[:h1]
        next unless parent

        parent["items"] << node
        ctx[:h3] = node
      end

      ctx[:last_heading] = node
      ctx[:last_heading_level] = level
      next
    end

    next unless stripped.match?(/\A(\[.+\]\(.+\)|\[\[.+\]\])\z/)

    if (m = stripped.match(/\A\[(.+?)\]\((.+?)\)\z/))
      attach_link_to_heading(ctx, m[1], normalize_url(m[2]))
      next
    end

    if stripped.match?(/\A\[\[.+?\]\]\z/)
      info = parse_inline(stripped)
      attach_link_to_heading(ctx, info[:title], info[:url])
    end
  end

  menu
end

def slug_id(text)
  text.to_s.downcase.gsub(/[^a-z0-9]+/, "-").gsub(/^-|-$/, "")
end

def url_to_node_id(url)
  return nil if url.nil? || url.empty?

  path = url.sub(%r{\A/}, "").sub(%r{/\z}, "")
  slug_id(path.gsub("/", "-"))
end

def extract_links_from_markdown(text, source_id)
  links = []
  text.scan(/\[\[([^\]|#]+)(?:\|([^\]]+))?\]\]/) do |ref, _label|
    target = resolve_wiki(ref.strip)
    tid = url_to_node_id(target)
    links << { "source" => source_id, "target" => tid, "kind" => "wiki" } if tid
  end

  text.scan(/\[([^\]]+)\]\(([^)]+)\)/) do |_label, href|
    next if href.match?(%r{\A(https?:|#|mailto:)}i)

    target = normalize_url(href)
    tid = url_to_node_id(target)
    links << { "source" => source_id, "target" => tid, "kind" => "mdlink" } if tid
  end

  links
end

def build_graph(nav)
  nodes = {}
  links = []
  seen_links = {}

  add_link = lambda do |source, target, kind|
    next if source.nil? || target.nil? || source == target

    key = [source, target, kind].join("|")
    return if seen_links[key]

    seen_links[key] = true
    links << { "source" => source, "target" => target, "kind" => kind }
  end

  add_node = lambda do |id, label, url: nil, kind: "note"|
    nodes[id] ||= { "id" => id, "label" => label, "url" => url, "kind" => kind }
  end

  walk_nav = nil
  walk_nav = lambda do |items, parent_id|
    items.each do |item|
      id = "moc-#{slug_id(item['title'])}"
      add_node.call(id, item["title"], url: item["url"], kind: "moc")
      add_link.call(parent_id, id, "moc") if parent_id

      if item["url"]
        file_id = url_to_node_id(item["url"])
        if file_id
          add_node.call(file_id, File.basename(item["url"].sub(%r{/\z}, "")), url: item["url"], kind: "note")
          add_link.call(id, file_id, "link")
        end
      end

      walk_nav.call(item["items"] || [], id)
    end
  end

  walk_nav.call(nav, nil)

  Dir.glob(File.join(ROOT, "contents", "**", "*.md")).each do |path|
    next if File.basename(path) == "site.md"

    rel = path.sub("#{ROOT}/", "").sub(/\.md\z/, "")
    id = slug_id(rel.gsub("/", "-"))
    label = File.basename(path, ".md")
    url = "/#{rel}/"
    add_node.call(id, label, url: url, kind: "note")

    body = strip_front_matter(File.read(path))
    extract_links_from_markdown(body, id).each do |link|
      add_link.call(link["source"], link["target"], link["kind"])
      tgt = nodes[link["target"]]
      add_node.call(link["target"], link["target"], url: tgt&.dig("url"), kind: "note") unless nodes[link["target"]]
    end
  end

  { "nodes" => nodes.values, "links" => links }
end

unless File.file?(SITE_MD)
  warn "Missing #{SITE_MD} — writing empty nav."
  FileUtils.mkdir_p(File.dirname(OUT_YML))
  File.write(OUT_YML, "---\n[]\n")
  FileUtils.mkdir_p(File.dirname(OUT_ASSET))
  File.write(OUT_ASSET, "")
  File.write(OUT_GRAPH, JSON.pretty_generate({ "nodes" => [], "links" => [] }))
  exit 0
end

source = File.read(SITE_MD)
nav = parse_moc(source)

FileUtils.mkdir_p(File.dirname(OUT_YML))
File.write(OUT_YML, nav.to_yaml)

FileUtils.mkdir_p(File.dirname(OUT_ASSET))
File.write(OUT_ASSET, source)

graph = build_graph(nav)
FileUtils.mkdir_p(File.dirname(OUT_GRAPH))
File.write(OUT_GRAPH, JSON.pretty_generate(graph))

puts "Wrote #{nav.length} top-level nav items → #{OUT_YML}"
puts "Copied site map → #{OUT_ASSET}"
puts "Wrote graph (#{graph['nodes'].length} nodes, #{graph['links'].length} links) → #{OUT_GRAPH}"
