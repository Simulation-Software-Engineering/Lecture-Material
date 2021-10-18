# lecture-materials

![markdownlint](https://github.com/Simulation-Software-Engineering/lecture-materials/actions/workflows/markdownlint.yml/badge.svg)

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
