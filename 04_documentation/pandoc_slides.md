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

- You know how to reuse your markup files for different purposes.
- You know how to convert markup files (Markdown, reStructuredText...) written into other formats (Markdown, reStructuredText...)

---

## "Pandoc a Universal Document Converter"

According to the project [homepage](https://pandoc.org/)

---

## Pandoc

> If you need to convert files from one markup format into another, pandoc is your swiss-army knife.
>
> [Homepage](https://pandoc.org/)

- Written in Haskell
- Converts **>=38** file formats into **>=60** file formats
    - Includes dialects
    - Results vary on language
- Write documentation/text in well-supported language, then convert to any format

---

## Conversion Overview

<img src="https://github.com/Simulation-Software-Engineering/Lecture-Material/raw/main/04_documentation/figs/pandoc/fig.png?raw=true" width=65%; style="margin-left:auto; margin-right:auto; padding-top: 25px; padding-bottom: 25px;">

- [Full diagram](https://pandoc.org/diagram.jpg) on homepage

---

## Usage

- Basic syntax

  ```bash
  pandoc INPUTFILE OPTIONS -o OUTPUTFILE
  ```

    - Without `OPTIONS` default values are used
    - Deduces conversion type from `OUTPUTFILE` file extension (by default)
- Extensive number of [options](https://pandoc.org/MANUAL.html#options)

---

## Useful options

- From file format to file format

  ```bash
  --from/-f FORMAT --to/-t FORMAT
  ```

- Create [standalone](https://pandoc.org/MANUAL.html#option--standalone) file

  ```bash
  -s/--standalone
  ```

  Uses template to add footer and header
- Set additional options

  ```bash
  -V OPTION=VALUE
  ```

  Options depend of template used

- Specify LaTeX compiler

  ```bash
  --pdf-engine=xelatex/lualatex/pdflatex
  ```

---

## Pandoc + LaTeX = Awesome PDFs

<img src="https://github.com/Simulation-Software-Engineering/Lecture-Material/raw/main/04_documentation/figs/pandoc-latex-workflow/fig.png?raw=true" width=95%; style="margin-left:auto; margin-right:auto; padding-top: 25px; padding-bottom: 25px;">

---

## Templates

- Has [default templates](https://pandoc.org/MANUAL.html#templates) for different targets
    - Print template with

      ```bash
      pandoc -D FORMAT
      ```

- Can install additional templates
    - Locations

      ```bash
      ${HOME}/.local/share/pandoc/templates/
      ```

      or

      ```bash
      ${HOME}/.pandoc/templates/
      ```

- Specify template on command line

  ```bash
  pandoc --template eisvogel
  ```

  [Eisvogel template](https://github.com/Wandmalfarbe/pandoc-latex-template)

---

## YAML Metadata Blocks

- Template may understand [`YAML` metadata blocks](https://pandoc.org/MANUAL.html#extension-yaml_metadata_block)

  ```yaml
  ---
  title: "My awesome title"
  author: Alexander Jaust
  ...
  ---
  ```

  May also be specified in separate `yaml` file.

- Available parameters depend on template
- Parameter missing? -> Build own template

---

## Further Reading

- [Pandoc homepage](https://pandoc.org/)
- [Eisvogel template](https://github.com/Wandmalfarbe/pandoc-latex-template)

