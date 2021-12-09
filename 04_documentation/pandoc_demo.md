# Pandoc Demo

- GitHub Action script
    - Lecture slides
    - Lecture notes
- Convert exercise sheet with default template

  ```bash
  pandoc packaging_spack_exercise.md --pdf-engine=xelatex --template eisvogel --listings -V colorlinks -o packaging_spack_exercise.pdf
  ```

  with `eisvogel` template

  ```bash
  pandoc packaging_spack_exercise.md --pdf-engine=xelatex --template eisvogel --listings -V colorlinks -o packaging_spack_exercise.pdf
  ```