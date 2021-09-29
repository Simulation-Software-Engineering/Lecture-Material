# Documentation

## Learning goals

- Understand what you want to document. Usage of a tool, development, API.
- Student can choose the right tool for the documentation needs.
- The students now common documentation tools for C++ and Python.
- The students now fundamentals of technical writing.

## Kick-off/Quiz

| Duration | Format |
| --- | --- |
| 10 minutes | Interactive/Discussion |

- Who has been annoyed some time by bad or lack of documentation? Do you have examples?
- Who has been happy/surprised by very good documentation?
    - Own examples:
        - Visual Basic for Application (VBA) documentation in Excel are (have been?/were?) great!
        - Man pages are (ofen) surprisingly enlighting.
- Who documents their code well?
    - If anyone says "yes", ask how?
    - If someone says "no, I am the only user", hint that documentation is still useful (thought process, unexpectedly need to share code, benefits collaboration). This will discussed more in second part of the topic/second lecture.


## Introduction

| Duration | Format |
| --- | --- |
| 10 minutes | Slides |

- Documentation is important:
    - For yourself. Do you remember what you did/why you did it after a long vacation?
    - For others:
        - Somebody wants to use your code, but cannot without asking you. -> Hinders adoptions/Steals your time.
        - Student thesis etc. -> Something you want to be able to offer/do.
        - Somebody wants to help/extend your code which ultimately helps your project, but the person cannot do it without knowledge about your code.
    - If there is no good documentation you might lose users, students, collaborators as well as bug fixes and improvements of your code.
    - There are (at least) two groups of people one needs documentation for:
        1. Users. They do not need all the details of the implementation and might not even have relevant programming experience.
        2. Developers. They might not know your projects standards for codings, testing, issues etc. They need quick access to relevant information.
- You want to document your code/API and the usage of your code.

## Tools

| Duration | Format |
| --- | --- |
| 10 minutes | Slides |

- In general: "Simple" to write style that generates easy to read and search documentation.
- API documentation:
    - C++: Doxygen
    - Python: DocString
- Project and user documentation
    - Wiki (Most do not allow Docs as code)
    - Markdown: jekyll, mkdocs (HedgeDoc?)
    - reStructuredText: Sphinx
    - Publication tool: ReadTheDocs
    - CI/CD for checking and deployment.
- Focus on ways to organize "docs as code". (Git lecture "If git diff does not work, it is the wrong format".)

## A short dive into markup languages

| Duration | Format |
| --- | --- |
| 15 minutes | Slides |

- Markdown
- reStructuredText (rst)
    - You will find reStructuredText especially in the world of Python.
- YAML
    - Might be needed for configuring the upcoming tools.

## A love letter to pandoc

- If you have structured text, it is easy to convert it.
- Write notes/documentation etc. in a lightweight markup language and convert it beautiful looking text and/or slides via LaTeX.
- Slide example!
- CV example?!

## Further reading

### Other

