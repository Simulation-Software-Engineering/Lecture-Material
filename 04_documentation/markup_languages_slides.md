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

- You know common markup languages.
- You know important parts of the syntax of these languages.
- You know what benefits these languages have.
- You know how to convert files written in these languages.

---

## Do you know any (Lightweight) Markup Languages?

---

## Introduction 1/2

- Why "lightweight"/"simple"/"humane"?
    - Readable without special rendering -> readable in text editor
    - Originates
- Different languages with different goals
    - Presentation: `Markdown`, `reStructuredText`, `AsciiDoc`...
    - Data serialization/storage: `YAML`, `JSON`...
- Suitable for **conversion** into other formats
- Plain text files

  > "If you can't git diff a file format, it's broken."

See [Wikipedia](https://en.wikipedia.org/wiki/Lightweight_markup_language)


---

## Markdown

<img src="https://github.com/dcurtis/markdown-mark/blob/master/png/1664x1024.png?raw=true" width=25%; style="margin-left:auto; margin-right:auto; padding-top: 25px; padding-bottom: 25px; background: #eeeeee">

Image Source: [markdown-mark on GitHub](https://github.com/dcurtis/markdown-mark)

---

## Markdown Introduction

> Markdown is a text-to-HTML conversion tool for web writers. Markdown allows you to write using an easy-to-read, easy-to-write plain text format, then convert it to structurally valid XHTML (or HTML).
> [Markdown Website](https://daringfireball.net/projects/markdown/)

- Created by John Gruber and Aaron Swartz in 2004
- Very popular (`README.md`, `CONTRIBUTING.md`...)
- Many tools with integrated rendering (GitHub, GitLab, Atom, Visual Studio Code...)
- Many different flavors
    - [GitHub Flavored Markdown](https://github.github.com/gfm/), [pandoc Markdown]()
- Effort of standardization: [CommonMark](https://commonmark.org/)
- File extension `md` or `markdown`

---

## Markdown Basics

- [CommonMark's "Learn Markdown in 60 seconds"](https://commonmark.org/help/)
- [Mastering Markdown (GitHub Guide)](https://guides.github.com/features/mastering-markdown/)

---

<img src="https://docutils.sourceforge.io/rst.png" width=75%; style="margin-left:auto; margin-right:auto; padding-top: 25px; padding-bottom: 25px; background: #eeeeee">

Image Source: [https://docutils.sourceforge.io/rst.png](https://docutils.sourceforge.io/rst.png)

---

## reStructuredText Overview

> reStructuredText is an easy-to-read, what-you-see-is-what-you-get plaintext markup syntax and parser system. It is useful for in-line program documentation (such as Python docstrings), for quickly creating simple web pages, and for standalone documents.
> [reStructuredText - Markup Syntax and Parser Component of Docutils](https://docutils.sourceforge.io/rst.html)

- Part of [Docutils](https://docutils.sourceforge.io/index.html) project
    - Very common in Python ecosystem
- Has a [specification](https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html)
- Common abbreviations `rst`, `reST` or `ReST`
- File extension `rst`

---

## reStructuredText Basics

- [Sphinx' reStructuredText primer](https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html)
- [A ReStructuredText Primer](https://docutils.sourceforge.io/docs/user/rst/quickstart.html)
- [Quick reStructuredText](https://docutils.sourceforge.io/docs/user/rst/quickref.html)

---

## YAML Ain't Markup Language™

---

## YAML

> YAML is a human-friendly data serialization   language for all programming languages.

- Popular as for configurations
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