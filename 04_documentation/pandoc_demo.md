# Pandoc Demo Notes

## Basic Usage

- Markdown example in `./examples/pandoc/example.md`
- Convert to `rst`: `pandoc example.md -o example.rst`
    - Meta data not used
- Convert to `pdf`: `pandoc example.md -o example.pdf`
    - Meta data used
- Convert to `docx`: `pandoc example.md -o example.docx`
- Convert to `tex`: `pandoc example.md -o example.tex`
    - No standalone file (cannot be further compiled into pdf just like that)
    - Not readable
- Standalone `tex`: `pandoc example.md -s -o example.tex`
- [Try pandoc online](https://pandoc.org/try/)
    - Not all file formats available
    - Choose example from drop down menu,  e.g. "Markdown to reStructureText"
    - Command in right top corner

## Default Templates

- Print `latex` template: `pandoc -D latex >> template.tex`
    - Very long
    - There is no `pdf` template, always goes through `latex`
- Convert to `pdf`: `pandoc example.md -o example.pdf`
    - Needs no `-s` option, since `pdf` is always standalone
    - Point out that link is not colored
- Color link: `pandoc example.md -V colorlinks -o example.pdf`
    - Binary option, no value
    - Find `colorlinks` in `template.tex`
    - [All variables for LaTeX](https://pandoc.org/MANUAL.html#variables-for-latex)

## Custom Templates

- Show that I have `eisvogel` installed: `ls ~/.pandoc/templates`
- Use template: `pandoc example.md --template eisvogel  -o example.pdf`
- Even nicer code: use `--listings` option
    - Uses latex listings package
    - Has nothing to do with `eisvogel` template
    - Extensive number of [options](https://pandoc.org/MANUAL.html#options)
