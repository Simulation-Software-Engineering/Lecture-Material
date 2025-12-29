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

# Document Conversion with Pandoc

---

## Learning Goals

- Convert markup files (Markdown, reStructuredText, ...) into other formats (Markdown, reStructuredText, PDF, docx, ...) with pandoc.
- Explain how markup languages, version control, and conversion pipelines play together.

---

## Pandoc

> - A Universal Document Converter
> - If you need to convert files from one markup format into another, pandoc is your swiss-army knife.

From [pandoc website](https://pandoc.org/)

- Written in Haskell
- Converts **>=38** file formats into **>=60** file formats
    - Includes dialects (e.g. different markdown flavors)

---

## Conversion Overview

<img src="https://github.com/Simulation-Software-Engineering/Lecture-Material/raw/main/04_documentation/figs/pandoc/fig.png?raw=true" width=65%; style="margin-left:auto; margin-right:auto; padding-top: 25px; padding-bottom: 25px;">

[Full diagram](https://pandoc.org/diagram.jpg) on homepage

- Idea: Write documentation/text in lightweight, easy to read/write, git-diffable language, then convert to any (non-git-diffable) format.

---

## Basic Usage


```bash
pandoc INPUTFILE -o OUTPUTFILE
```

- Deduces conversion type from `OUTPUTFILE` file extension (by default)
- If explicit formats required (e.g. specific md flavors):

  ```bash
  --from/-f FORMAT --to/-t FORMAT
  ```

---

## Demo: Basic Usage

---

## Pandoc + LaTeX = Awesome PDFs

<img src="https://github.com/Simulation-Software-Engineering/Lecture-Material/raw/main/04_documentation/figs/pandoc-latex-workflow/fig.png?raw=true" width=95%; style="margin-left:auto; margin-right:auto; padding-top: 25px; padding-bottom: 25px;">

- Specify LaTeX compiler: `--pdf-engine=xelatex/lualatex/pdflatex`

---

## Standalone and Default Templates

- Create [standalone](https://pandoc.org/MANUAL.html#option--standalone) file

  ```bash
  -s/--standalone
  ```

- This uses a [default template](https://pandoc.org/MANUAL.html#templates) for specific target format
    - To define, e.g., footer and header
    - Print template with, e.g.

      ```bash
      pandoc -D latex
      ```

- Set options defined in template

  ```bash
  -V OPTION=VALUE
  ```

---

## YAML Metadata Blocks

- Template may understand [`YAML` metadata blocks](https://pandoc.org/MANUAL.html#extension-yaml_metadata_block)

  ```yaml
  ---
  title: My awesome title
  author: Firstname lastname
  ...
  ---
  ```

  May also be specified in separate `yaml` file.

- Available parameters depend on template

---

## Demo: Default Templates

---

## Custom Templates

- Install additional templates in

  ```bash
  ${HOME}/.local/share/pandoc/templates/
  ```

  or

  ```bash
  ${HOME}/.pandoc/templates/
  ```

- Specify template on command line, e.g. [Eisvogel template](https://github.com/Wandmalfarbe/pandoc-latex-template)

  ```bash
  pandoc --template eisvogel
  ```

---

## Demo: Custom Templates

---

## SSE Lecture Material as Example

- [GitHub Action](https://github.com/Simulation-Software-Engineering/Lecture-Material/tree/main/.github/workflows) and [script](https://github.com/Simulation-Software-Engineering/Lecture-Material/blob/main/scripts/create-pdf-from-markdown.sh)
- Current lecture slides command:

```text
pandoc --pdf-engine=xelatex -t beamer -V aspectratio=169 -V \
             linkcolor:blue -V fontsize=12pt --listings -s \
             --output=OUTPUTFILENAME INPUTFILENAME
```

- Current lecture notes command:

```text
pandoc --pdf-engine=xelatex -V geometry:a4paper \
       -V geometry:left=2.5cm -V geometry:right=2.5cm \
       -V geometry:bottom=2.5cm -V geometry:top=2.5cm \
       -V colorlinks:true -V linkcolor:blue -V fontsize=10pt \
       --listings -s --output=OUTPUTFILENAME INPUTFILENAME
```

---

## Pandoc and Generative AI

> In the age of Large Language Models (LLMs), is Pandoc still relevant?
