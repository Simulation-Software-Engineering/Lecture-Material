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

## Learning Goals

- You know common markup languages (Markdown, reStructuredText, YAML).
- You know important parts of the syntax of these languages.
- You know what benefits these languages have.

---

## Do you know any (Lightweight) Markup Languages?

---

## Introduction

- Why "lightweight"/"simple"/"humane"?
    - Readable without special rendering -> readable in text editor
    - Originates from earlier times when texts on screens would not support special formatting
- Different languages with different goals
    - Presentation: `Markdown`, `reStructuredText`, `AsciiDoc`, [WhatsApp](https://faq.whatsapp.com/general/chats/how-to-format-your-messages/?lang=en)...
    - Data serialization/storage: `YAML`, `JSON`...

See [Wikipedia](https://en.wikipedia.org/wiki/Lightweight_markup_language)

---

## Common Properties

- **Whitespaces** very important
- Suitable for **conversion** into other formats, especially HTML
- Plain text files -> Good for us

  > "If you can't git diff a file format, it's broken."

    - Suitable for [Docs as code](https://www.writethedocs.org/guide/docs-as-code/) and [DocOps](https://www.writethedocs.org/guide/doc-ops/)

---

## Docs as Code

> Documentation as Code (Docs as Code) refers to a philosophy that you should be writing documentation with the same tools as code [...] following the same workflows as development teams [...]
>
> [Write the Docs](https://www.writethedocs.org/guide/docs-as-code/)

---

## DocOps

> a set of practices that works to automate and integrate the process of developing documentation across engineering, product, support, and, of course, technical writing teams.
>
> [Write the Docs](https://www.writethedocs.org/guide/doc-ops/)

---

## DocOps Lifecycle

<img src="https://www.writethedocs.org/_images/docops-lifecycle.png" width=78%; style="margin-left:auto; margin-right:auto; padding-top: 25px; padding-bottom: 25px;">

Source: [Write the Docs](https://www.writethedocs.org/guide/doc-ops/)

---

## Markdown

<img src="https://github.com/dcurtis/markdown-mark/raw/master/png/1664x1024.png" width=50%; style="margin-left:auto; margin-right:auto; padding-top: 25px; padding-bottom: 25px; background: #eeeeee">

Image Source: [markdown-mark on GitHub](https://github.com/dcurtis/markdown-mark)

---

## Markdown Introduction

> Markdown is a text-to-HTML conversion tool for web writers. Markdown allows you to write using an easy-to-read, easy-to-write plain text format, then convert it to structurally valid XHTML (or HTML).
> [Markdown Website](https://daringfireball.net/projects/markdown/)

- Created by John Gruber and Aaron Swartz in 2004
- Very popular (`README.md`, `CONTRIBUTING.md`...)
- Many tools with integrated rendering (GitHub, GitLab, Atom, Visual Studio Code...)
- Common indentation with 2 or 4 spaces
- File extension `md` or `markdown`

---

## Markdown Flavors

- Many different flavors
    - [GitHub](https://github.github.com/gfm/)/[GitLab]((https://docs.gitlab.com/ee/user/markdown.html#differences-between-gitlab-flavored-markdown-and-standard-markdown))  flavored Markdown, [RMarkdown](https://rmarkdown.rstudio.com/)...
- Effort of standardization: [CommonMark](https://commonmark.org/)

---

## Markdown Basics

- [CommonMark's "Learn Markdown in 60 seconds"](https://commonmark.org/help/)
- [Mastering Markdown (GitHub Guide)](https://guides.github.com/features/mastering-markdown/)
- [CommonMark's Markdown tutorial](https://commonmark.org/help/tutorial/)

---

<img src="https://docutils.sourceforge.io/rst.png" width=75%; style="margin-left:auto; margin-right:auto; padding-top: 25px; padding-bottom: 25px; background: #eeeeee">

Image Source: [https://docutils.sourceforge.io/rst.png](https://docutils.sourceforge.io/rst.png)

---

## reStructuredText

> reStructuredText is an easy-to-read, what-you-see-is-what-you-get plaintext markup syntax and parser system. It is useful for in-line program documentation (such as Python docstrings), for quickly creating simple web pages, and for standalone documents.
> [reStructuredText - Markup Syntax and Parser Component of Docutils](https://docutils.sourceforge.io/rst.html)

---

## Overview

- Part of [Docutils](https://docutils.sourceforge.io/index.html) project
    - Very common in Python ecosystem
- Has a [specification](https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html), good base format for conversion
- Indentation depends on context (2, 3, 4 spaces)
- Special blocks introduced by `..` or `::`followed by a space
- Common abbreviations `rst`, `reST` or `ReST`
- File extension `rst`

---

## reStructuredText Basics

- [Sphinx' reStructuredText primer](https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html)
- [A ReStructuredText Primer](https://docutils.sourceforge.io/docs/user/rst/quickstart.html)
- [Quick reStructuredText](https://docutils.sourceforge.io/docs/user/rst/quickref.html)

---

## YAML: YAML Ain't Markup Language™

<img src="https://github.com/yaml/yaml-spec/raw/main/spec/1.2/docbook/logo.png" width=50%; style="margin-left:auto; margin-right:auto; padding-top: 25px; padding-bottom: 25px; background: #eeeeee">

Image Source: [https://github.com/yaml/yaml-spec/blob/main/spec/1.2/docbook/logo.png](https://github.com/yaml/yaml-spec/blob/main/spec/1.2/docbook/logo.png)

---

## YAML

> YAML is a human-friendly data serialization language for all programming languages.

- Popular for configurations
- Indentation with **two** spaces is important.
    - Tabs **not** allowed for indentation
- Can differentiate between datatypes
- Recommended file extension `yaml` (also `yml`)

See [the official YAML website](https://yaml.org/)

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

### YAML Example from Slides

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

---

## Further Reading

- [Lightweight Markup Languages (Wikipedia)](https://en.wikipedia.org/wiki/Lightweight_markup_language)
- [Markdown](https://daringfireball.net/projects/markdown/)
- [CommonMark](https://commonmark.org/)
- [CommonMark Specification](https://spec.commonmark.org/)
- [Markdown cheat sheet with focus on GitHub's flavor](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)
- [Mastering Markdown (GitHub Guide)](https://guides.github.com/features/mastering-markdown/)

---

## Further Reading (reStructuredText)

- [Docutils](https://docutils.sourceforge.io/index.html)
- [reStructuredText - Markup Syntax and Parser Component of Docutils](https://docutils.sourceforge.io/rst.html)
- [A ReStructuredText Primer](https://docutils.sourceforge.io/docs/user/rst/quickstart.html)
- [Quick reStructuredText](https://docutils.sourceforge.io/docs/user/rst/quickref.html)
- [Sphinx' reStructuredText primer](https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html)

---

## Further Reading (YAML)

- [The official YAML website](https://yaml.org/)