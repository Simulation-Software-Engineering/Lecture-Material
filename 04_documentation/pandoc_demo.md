# Pandoc Demo

- Show [Try Pandoc](https://pandoc.org/try/)
    - **Note**: The list of options is not complete here!
- Show very simple example on try pandoc

  ```markdown
  ---
  title: My awesome title
  author: Firstname lastname
  date: 2022-01-27
  ---

  # Introduction

  This is my text
  ```

  Convert to different file formats

  If we have time also compile to PDF locally.

- Convert exercise sheet with default template

  ```bash
  pandoc packaging_spack_exercise.md --pdf-engine=xelatex --listings -V colorlinks -o packaging_spack_exercise.pdf
  ```

  with [`eisvogel` template](https://github.com/Wandmalfarbe/pandoc-latex-template)

  ```bash
  pandoc packaging_spack_exercise.md --pdf-engine=xelatex --template eisvogel --listings -V colorlinks -o packaging_spack_exercise.pdf
  ```

- GitHub Action and script for lecture material.
    - [Link to the actions](https://github.com/Simulation-Software-Engineering/Lecture-Material/tree/main/.github/workflows)
    - [Link to the scripts](https://github.com/Simulation-Software-Engineering/Lecture-Material/blob/main/scripts/create-pdf-from-markdown.sh)
    - Current lecture slides command:

      ```text
      pandoc --pdf-engine=xelatex -t beamer -V aspectratio=169 -V linkcolor:blue -V fontsize=12pt --listings -s --output=OUTPUTFILENAME INPUTFILENAME
      ```

    - Current lecture notes command:

      ```text
      pandoc --pdf-engine=xelatex -V geometry:a4paper -V geometry:left=2.5cm -V geometry:right=2.5cm -V geometry:bottom=2.5cm -V geometry:top=2.5cm -V colorlinks:true -V linkcolor:blue -V fontsize=10pt --listings -s --output=OUTPUTFILENAME INPUTFILENAME
      ```

