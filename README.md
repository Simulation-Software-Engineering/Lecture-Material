# lecture-materials

![markdownlint](https://github.com/Simulation-Software-Engineering/lecture-materials/actions/workflows/markdownlint.yml/badge.svg)

## Linting

The markdown files can be checked using [markdownlint](https://github.com/markdownlint/markdownlint/). Once the linter is installed one can run it locally from the root of this repository using

```
mdl .
```

It will automatically read the markdownlint configuration of this repository. The linter is configured in the files `.mdl.rb` and `.mdlrc`. The majority of the configuration is done in `.mdl.rb`.