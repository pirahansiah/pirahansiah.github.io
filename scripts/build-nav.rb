#!/usr/bin/env ruby
# frozen_string_literal: true

# Parse Obsidian-style MOC (contents/site.md) → _data/nav.yml + assets/site-map.md
# Run before Jekyll build (see run.sh). No gem plugins required.

require "yaml"
require "fileutils"

ROOT = File.expand_path("..", __dir__)
SITE_MD = File.join(ROOT, "contents", "site.md")
OUT_YML = File.join(ROOT, "_data", "nav.yml")
OUT_ASSET = File.join(ROOT, "assets", "site-map.md")

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

def parse_moc(text)
  menu = []
  ctx = {
    h1: nil,
    h2: nil,
    h3: nil,
    last_node: nil,
    list_stack: []
  }

  strip_front_matter(text).each_line do |raw|
    line = raw.chomp
    stripped = line.strip
    next if stripped.empty? || stripped == "[]"

    if (m = stripped.match(/\A(#+)\s+(.+)\z/))
      level = m[1].length
      next if level > 6
      info = parse_inline(m[2])
      node = { "title" => info[:title], "items" => [] }
      node["url"] = info[:url] if info[:url]

      case level
      when 1
        menu << node
        ctx[:h1] = node
        ctx[:h2] = ctx[:h3] = nil
      when 2
        unless ctx[:h1]
          ctx[:h1] = { "title" => "Notes", "items" => [] }
          menu << ctx[:h1]
        end
        ctx[:h1]["items"] << node
        ctx[:h2] = node
        ctx[:h3] = nil
      when 3
        parent = ctx[:h2] || ctx[:h1]
        parent["items"] << node
        ctx[:h3] = node
      else
        (ctx[:h3] || ctx[:h2] || ctx[:h1])["items"] << node
      end

      ctx[:last_node] = node
      ctx[:list_stack] = []
      next
    end

    if (m = line.match(/\A(\s*)[-*+]\s+(.+)\z/))
      indent = m[1].length
      info = parse_inline(m[2].strip)
      node = { "title" => info[:title], "items" => [] }
      node["url"] = info[:url] if info[:url]

      parent = list_parent(ctx, indent)
      parent["items"] << node

      ctx[:list_stack].pop while ctx[:list_stack].any? && ctx[:list_stack].last[:indent] >= indent
      ctx[:list_stack] << { indent: indent, node: node }
      ctx[:last_node] = node
      next
    end

    if (m = stripped.match(/\A\[(.+?)\]\((.+?)\)\z/))
      url = normalize_url(m[2])
      if ctx[:last_node] && !ctx[:last_node]["url"]
        ctx[:last_node]["url"] = url
        ctx[:last_node]["title"] = m[1] if ctx[:last_node]["title"].to_s.empty?
      else
        append_link(menu, ctx, m[1], url)
      end
      next
    end

    if stripped.match?(/\A\[\[.+?\]\]\z/)
      info = parse_inline(stripped)
      if ctx[:last_node] && !ctx[:last_node]["url"]
        ctx[:last_node]["url"] = info[:url]
        ctx[:last_node]["title"] = info[:title] if ctx[:last_node]["title"].to_s.empty?
      else
        append_link(menu, ctx, info[:title], info[:url])
      end
    end
  end

  menu
end

def list_parent(ctx, indent)
  if indent.positive?
    entry = ctx[:list_stack].reverse.find { |s| s[:indent] < indent }
    return entry[:node] if entry
  end

  ctx[:h3] || ctx[:h2] || ctx[:h1]
end

def append_link(menu, ctx, title, url)
  node = { "title" => title, "url" => url, "items" => [] }
  parent = ctx[:h3] || ctx[:h2] || ctx[:h1]
  if parent
    parent["items"] << node
  else
    menu << node
  end
  ctx[:last_node] = node
end

unless File.file?(SITE_MD)
  warn "Missing #{SITE_MD} — writing empty nav."
  FileUtils.mkdir_p(File.dirname(OUT_YML))
  File.write(OUT_YML, "---\n[]\n")
  FileUtils.mkdir_p(File.dirname(OUT_ASSET))
  File.write(OUT_ASSET, "")
  exit 0
end

source = File.read(SITE_MD)
nav = parse_moc(source)

FileUtils.mkdir_p(File.dirname(OUT_YML))
File.write(OUT_YML, nav.to_yaml)

FileUtils.mkdir_p(File.dirname(OUT_ASSET))
File.write(OUT_ASSET, source)

puts "Wrote #{nav.length} top-level nav items → #{OUT_YML}"
puts "Copied site map → #{OUT_ASSET}"
