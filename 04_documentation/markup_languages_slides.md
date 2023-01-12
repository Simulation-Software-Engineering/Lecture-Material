---
type: slide
slideOptions:
  transition: slide
  width: 1400
  height: 900
  margin: 0.1
---

<style>
  .reveal strong {
    font-weight: bold;
    color: orange;
  }
  .reveal p {
    text-align: left;
  }
  .reveal section h1 {
    color: orange;
  }
  .reveal section h2 {
    color: orange;
  }
  .reveal code {
    font-family: 'Source Code Pro';
    color: orange;
  }
  .reveal section img {
    background:none;
    border:none;
    box-shadow:none;
  }
</style>

# Lightweight Markup Languages

---

## Quick Survey

- Who knows any (lightweight) markup language?
- What could *"lightweight"* mean?

---

## Learning Goals

- Explain what lightweight markup languages are and why they are important for documentation.
- Recognize the syntax of Markdown, reStructuredText, and YAML.
- Write in these languages (with a little help of cheat sheets sometimes).
- Explain the specific purposes of these languages.

---

## What are Markup Languages?

> - Markup language refers to a text-encoding system consisting of a set of symbols inserted in a text document to control its structure, formatting, or the relationship between its parts.
> - The idea and terminology evolved from the "marking up" of paper manuscripts (i.e., the revision instructions by editors), which is traditionally written with a red pen or blue pencil on authors' manuscripts.

See [Wikipedia](https://en.wikipedia.org/wiki/Markup_language)

---

## What are Lightweight Markup Languages?

- Why "lightweight"/"simple"/"humane"?
    - Readable in raw text form **and** rendered
    - Originates from earlier times when texts on screens would not support special formatting
    - Not lightweight: `xml`, `html`, `tex`, ...
- Different languages with different goals
    - Presentation: `Markdown`, `reStructuredText`, `AsciiDoc`, [WhatsApp](https://faq.whatsapp.com/general/chats/how-to-format-your-messages/?lang=en), ...
    - Data serialization/storage: `YAML`, `JSON`, ...
- Easy to write, easy to read --> Perfect for documentation

See [Wikipedia](https://en.wikipedia.org/wiki/Lightweight_markup_language)

---

## Common Properties

- **Whitespaces** very important
- Suitable for **conversion** into other formats, especially HTML
- Plain text files --> Good for us

  > "If you can't git diff a file format, it's broken."

- Suitable for [Docs as code](https://www.writethedocs.org/guide/docs-as-code/) and [DocOps](https://www.writethedocs.org/guide/doc-ops/)

---

## Docs as Code

> Documentation as Code (Docs as Code) refers to a philosophy that you should be writing documentation with the same tools as code [...] following the same workflows as development teams [...]

From [Write the Docs](https://www.writethedocs.org/guide/docs-as-code/)

---

## DocOps

> A set of practices that works to automate and integrate the process of developing documentation across engineering, product, support, and, of course, technical writing teams.

From [Write the Docs](https://www.writethedocs.org/guide/doc-ops/)

---

## DocOps Lifecycle

<img src="https://www.writethedocs.org/_images/docops-lifecycle.png" width=72%; style="margin-left:auto; margin-right:auto; padding-top: 25px; padding-bottom: 25px;">

Image source: [Write the Docs](https://www.writethedocs.org/guide/doc-ops/)

---

## Markdown

<img src="https://github.com/dcurtis/markdown-mark/raw/master/png/1664x1024.png" width=25%; style="margin-left:auto; margin-right:auto; padding-top: 25px; padding-bottom: 25px; background: #eeeeee">

Image source: [markdown-mark on GitHub](https://github.com/dcurtis/markdown-mark)

> Markdown is a text-to-HTML conversion tool for web writers. Markdown allows you to write using an easy-to-read, easy-to-write plain text format, then convert it to structurally valid XHTML (or HTML).

From [Markdown website](https://daringfireball.net/projects/markdown/)

---

## Markdown Overview

- Created by John Gruber and Aaron Swartz in 2004
- Very popular (`README.md`, `CONTRIBUTING.md`...)
- Many tools with integrated rendering (GitHub, GitLab, Atom, Visual Studio Code...)
- Common indentation with 2 or 4 spaces
- File extension `md` or `markdown`
- Markdown example in `./examples/markdown-example.md`

---

## Markdown Flavors

- Many different flavors
    - [GitHub](https://github.github.com/gfm/)/[GitLab]((https://docs.gitlab.com/ee/user/markdown.html#differences-between-gitlab-flavored-markdown-and-standard-markdown)) flavored Markdown, [RMarkdown](https://rmarkdown.rstudio.com/), ...
- Effort of standardization: [CommonMark](https://commonmark.org/)

---

## Markdown Basics

- [CommonMark's "Learn Markdown in 60 seconds"](https://commonmark.org/help/)
- [CommonMark's Markdown tutorial](https://commonmark.org/help/tutorial/)
- [Mastering Markdown (GitHub Guide)](https://guides.github.com/features/mastering-markdown/)
- [Markdown cheat sheet with focus on GitHub's flavor](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)

---

## reStructuredText

> reStructuredText is an easy-to-read, what-you-see-is-what-you-get plaintext markup syntax and parser system. It is useful for in-line program documentation (such as Python docstrings), for quickly creating simple web pages, and for standalone documents.

From [reStructuredText - Markup Syntax and Parser Component of Docutils](https://docutils.sourceforge.io/rst.html)

---

## reStructuredText Overview

- Part of [Docutils](https://docutils.sourceforge.io/index.html) project
    - Very common in Python ecosystem
- Has a [specification](https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html), good base format for conversion
- Indentation depends on context (2, 3, 4 spaces)
- Special blocks introduced by `..` or `::`followed by a space
- Common abbreviations `rst`, `reST` or `ReST`
- File extension `rst`
- More tedious, but more powerful than markdown
- ReST example in `./examples/reStructuredText-example.rst`

---

## reStructuredText Basics

- [Sphinx' reStructuredText primer](https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html)
- [A reStructuredText primer](https://docutils.sourceforge.io/docs/user/rst/quickstart.html)
- [Quick reStructuredText](https://docutils.sourceforge.io/docs/user/rst/quickref.html)

---

## YAML: YAML Ain't Markup Language™

<img src="https://github.com/yaml/yaml-spec/raw/main/spec/1.2/docbook/logo.png" width=30%; style="margin-left:auto; margin-right:auto; padding-top: 25px; padding-bottom: 25px; background: #eeeeee">

Image source: [https://github.com/yaml/yaml-spec/blob/main/spec/1.2/docbook/logo.png](https://github.com/yaml/yaml-spec/blob/main/spec/1.2/docbook/logo.png)

> YAML is a human-friendly data serialization language for all programming languages.

From [YAML website](https://yaml.org/)

---

## YAML Overview

- Popular for configurations
- Indentation with **two** spaces is important.
    - Tabs **not** allowed for indentation
- Can differentiate between datatypes
- Recommended file extension `yaml` (also `yml`)

---

## YAML Example

```yaml
keyA: value
keyB:
- list
- of
- values
keyC:
  keyD: some value
  keyE: some other value
```

---

## YAML Example from Slides

```yaml
---
type: slide
slideOptions:
  transition: slide
  width: 1400
  height: 900
  margin: 0.1
---
```

- `---` separates directives from content
