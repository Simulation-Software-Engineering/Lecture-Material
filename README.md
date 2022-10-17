# Simulation Software Engineering Lecture Material

![markdownlint](https://github.com/Simulation-Software-Engineering/lecture-materials/actions/workflows/markdownlint.yml/badge.svg)
[![PDFs](https://github.com/Simulation-Software-Engineering/lecture-materials/actions/workflows/create-pdfs-from-markdown.yml/badge.svg)](https://github.com/Simulation-Software-Engineering/Lecture-Material/actions/workflows/create-pdfs-from-markdown.yml)
[![CC BY 4.0][cc-by-shield]][cc-by]

Material of the Simulation Software Engineering lecture. There are different way how to get an overview:

- Look at `timetable.md` of the [current course](https://github.com/Simulation-Software-Engineering/Lecture-Material/blob/main/timetable.md) or [previous courses](https://github.com/Simulation-Software-Engineering/Lecture-Material/tree/main/00_organization/wt2122/timetable.md),
- Look at the `README.md` files of each chapter / folder,
- Browse the content through the [course website](https://simulation-software-engineering.github.io/homepage/).

Please note that we update the material over the course of each semester.

## List of chapters

1. [Version Control](https://github.com/Simulation-Software-Engineering/Lecture-Material/tree/main/01_version_control)
2. [Virtualization and Containers](https://github.com/Simulation-Software-Engineering/Lecture-Material/tree/main/02_virtualization_and_containers)
3. [Building and Packaging](https://github.com/Simulation-Software-Engineering/Lecture-Material/tree/main/03_building_and_packaging)
4. [Documentation](https://github.com/Simulation-Software-Engineering/Lecture-Material/tree/main/04_documentation)
5. [Testing and CI](https://github.com/Simulation-Software-Engineering/Lecture-Material/tree/main/05_testing_and_ci)
6. [Miscellaneous](https://github.com/Simulation-Software-Engineering/Lecture-Material/tree/main/06_miscellaneous)

## Linting

The markdown files can be checked using [markdownlint](https://github.com/markdownlint/markdownlint/). Once the linter is installed one can run it locally from the root of this repository using

```
mdl .
```

It will automatically read the markdownlint configuration of this repository. The linter is configured in the files `.mdl.rb` and `.mdlrc`. The majority of the configuration is done in `.mdl.rb`.

## Third-party content

In several parts of the material, we use content from

> Irving, Hertweck, Johnston, Ostblom, Wickham, and Wilson: [Research Software Engineering with Python](https://merely-useful.tech/py-rse), 2021,

a book, which we also recommend to recap Git/Bash/Python basics.

## License

This work is licensed under a
[Creative Commons Attribution 4.0 International License][cc-by].

[![CC BY 4.0][cc-by-image]][cc-by]

[cc-by]: http://creativecommons.org/licenses/by/4.0/
[cc-by-image]: https://i.creativecommons.org/l/by/4.0/88x31.png
[cc-by-shield]: https://img.shields.io/badge/License-CC%20BY%204.0-blue.svg
