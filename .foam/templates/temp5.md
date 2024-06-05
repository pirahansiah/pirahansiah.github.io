---
foam_template:
  name: My Note Template
  filepath: 'journal/${FOAM_TITLE}.md'
  foam_filepath: '${FOAM_FILEPATH}'
  foam_name: '${FOAM_NAME}'
  foam_description: '${FOAM_DESCRIPTION}'
  background: '${FOAM_BACKGROUND_IMAGE}'
  date: '${FOAM_DATE}'
  description: '${FOAM_DESCRIPTION}'
  draft: false
  expiryDate: '${FOAM_EXPIRY_DATE}'
  headless: true
  isCJKLanguage: false
  lastmod: '${FOAM_LASTMOD}'
  layout: "post"
  linkTitle: '${FOAM_LINK_TITLE}'
  markup: "markdown"
  menus: ["main", "footer"]
  outputs: ["HTML", "RSS"]
  customParam: '${FOAM_CUSTOM_PARAM}'
  publishDate: '${FOAM_PUBLISH_DATE}'
  sitemap:
    changefreq: '${FOAM_CHANGEFREQ}'
  cssclass: '${FOAM_CSSCLASS}'
  author:
    - name: '${FOAM_AUTHOR1}'
      affiliation: '${FOAM_AFFILIATION1}'
    - name: '${FOAM_AUTHOR2}'
      affiliation: '${FOAM_AFFILIATION2}'
  last_modified_at: '${FOAM_LASTMOD}'
  tags: ['${FOAM_TAG1}', '${FOAM_TAG2}', '${FOAM_TAG3}']
  resources:
    - src: '${FOAM_IMAGE_SRC}'
      title: '${FOAM_IMAGE_TITLE}'
  slug: '${FOAM_SLUG}'
  summary: '${FOAM_SUMMARY}'
  translationKey: '${FOAM_TRANSLATION_KEY}'
  alias: '${FOAM_ALIAS}'
  lang: '${FOAM_LANG}'
  nocite: '${FOAM_NOCITE}'
  category: '${FOAM_CATEGORY}'
---

---
existing_frontmatter: "Existing Frontmatter block"
# ${FOAM_DATE_YEAR}-${FOAM_DATE_MONTH}-${FOAM_DATE_DATE}




Title: ${FOAM_TITLE}
Description: ${FOAM_DESCRIPTION}


Link Title: ${FOAM_LINK_TITLE}
Custom Param: ${FOAM_CUSTOM_PARAM}
Publish Date: ${FOAM_PUBLISH_DATE}
Image Source: ${FOAM_IMAGE_SRC}
Image Title: ${FOAM_IMAGE_TITLE}
Change Frequency: ${FOAM_CHANGEFREQ}
Priority: ${FOAM_PRIORITY}
Summary: ${FOAM_SUMMARY}
Translation Key: ${FOAM_TRANSLATION_KEY}
Alias: ${FOAM_ALIAS}
CSS Class: ${FOAM_CSSCLASS}
Author 1: ${FOAM_AUTHOR1}
Affiliation 1: ${FOAM_AFFILIATION1}
Author 2: ${FOAM_AUTHOR2}
Affiliation 2: ${FOAM_AFFILIATION2}
Language: ${FOAM_LANG}
No Cite: ${FOAM_NOCITE}
Category: ${FOAM_CATEGORY}
---
