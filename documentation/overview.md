# Documentation

## Learning goals

- Understand what you want to document. Usage of a tool, development, API.
- Student can choose the right tool for the documentation needs.
- The students now common documentation tools for C++ and Python.
- The students now fundamentals of technical writing.
- Students understand the importance of documentatio for themselves and others.
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
- Writing documentation is more fun if you know what to look out for and when using the right tools.

**TODO** Should there be something about `man` pages?
## Lightweight markup languages

| Duration | Format |
| --- | --- |
| 15 minutes | Slides/Interactive |

**TODO** We should maybe have some (light) Markdown introduction already for the first

- Do you now and maybe even use a lightweight markup language?
- Markdown
    - Created by John Gruber and Aaron Swartz in 2004
    - Markup language that is easy to read when you read the source code and a tool to convert Markdown to HTML as mentioned on the [website](https://daringfireball.net/projects/markdown/)
    - Very popular
    - Markdown example. Maybe a README or parts of the homepage or lecture planning. **TODO** Some of this should go into some exercise. Should we discuss this earliers in the lecture?
    ```markdown
    # This is the top level header

    If you follow some (?) standard strictly, the top level header should be the very first line in a markdown file.

    ## You can write text

    Hello there.
    *This text is emphasized (italics)*
    **This text is heavily emphasized (bold)**

    We can also have nice lists

    - Item 1
    - Item 2

    which can be numbered as well

    1. Item 1
    2. Item 2
        1. Item 2a
        2. Item 2b

    As one can see we can also have sublists.

    Code uses backticks. This can be code/variable names in text that `appear` in a monospace font. Code blocks start and end with triple backticks and often take a specifier of the presented language.

    > ```c++
        int main()
        {
            return 0;
        }
      ```

    > Quotations can be done by angle brackets

    We can also have hyperlinks to other websites. We could link to the [course website][], but separate the link in the text from the target definition.

      [course website]: https://simulation-software-engineering.github.io/homepage

    ## This is a subheader

    We can have nice tables

    | Column A | Column B |
    | -------- | -------- |
    | Value A  | Value  B |
    ```
    - Indentation is important (spaces). Number of spaces depends on the implementation. Common are `2` and `4` space characters. I usuallay use `4` spaces.
    - Not standardized -> There are several specializations:
        - GitHub-flavored Markdown
        - GitLab-flavored Markdown. Differences are described in the [docs](https://docs.gitlab.com/ee/user/markdown.html#differences-between-gitlab-flavored-markdown-and-standard-markdown)
        - RMarkDown
        - Pandoc Markdown
        - There a lots of extensions to add new features.
- CommonMark
    - Effort to standardize Markdown started in 2014
    - No `1.0` release yet, but the "standard" or baseline of many Markdown implementations (GitHub, Reddit etc.)
- reStructuredText (rst)
    - Developed by [docutils project](docutils.sourceforge.net)
        > Docutils is an open-source text processing system for processing plaintext documentation into useful formats, such as HTML, LaTeX, man-pages, OpenDocument, or XML. It includes reStructuredText, the easy to read, easy to use, what-you-see-is-what-you-get plaintext markup language.
    - You will find reStructuredText especially in the world of Python.
    - Much more standardized and feature rich than markdown.\
    - Indentation is important (spaces). Often identation of `3` characters. Two characters to announce some special block coming (using `..` or `::`) that is followed by a space.
    - Allows for anchors, cross references, footnotes etc.
    ```reStructuredText
    ==================
    Top-level headline
    ==================

    Overlining is optional. One can use other characters for the headline marking such as ``-`` or ``*``. There is not strict hierarchy of these characters defined to mark sections, subsections etc. The actual hierarchy is determined by the order of headings. However, the Python style guide proposes ``#`` > ``*`` > ``=`` and so on with each character referring to a certain type of structure (part, chapter, section...)

    More information can be found in the `Python documentation style guide <https://devguide.python.org/documenting/#sections>`_

    -------------------------------
    This is the second-level header
    -------------------------------

    Hello there.
    *This text is emphasized (italics)*
    **This text is heavily emphasized (bold)**

    We can also have nice lists

    * Item 1
    * Item 2

    which can be numbered as well

    1. Item 1
    2. Item 2

       1. Item 2a
       2. Item 2b

    As one can see we can also have sublists. In contrast to markdown there has to be a line break before the sublist starts.

    Code uses backticks. This can be code/variable names in text that ``appear`` in a monospace font. Code blocks start and end with triple backticks and often take a specifier of the presented language.

    .. code-block:: c++

       int main()
       {
           return 0;
       }

    .. Quotations can be done by two dots

    We can also have hyperlinks to other websites. We could link to the `course website`_, but separate the link and target definition.

    .. _course website: https://simulation-software-engineering.github.io/homepage

    ------
    Tables
    ------

    There is two ways to create tables. The more powerful way uses grid tables:

    +----------+----------+
    | Column A | Column B |
    +==========+==========+
    | Value A  | Value  B |
    +----------+----------+

    ```
- YAML
    - Might be needed for configuring the upcoming tools.
    - Indentation with 4 spaces is important. Tabs do **not** work!
    - Example
    ```yaml
    keyA: option
    keyB:
    - list
    - of
    - options
    keyC:
        keyD: some suboption
    ```
- In general: Use "simple" to write style that generates easy to read and search documentation.

## API documentation

| Duration | Format |
| --- | --- |
| 20 minutes | Slides |

- API documentation:
    - C++: Doxygen
    - Python: DocString
- Doxygen:
    - Documentation (can be) in code
    - Understands markdown
- DocString
    - Documentation in code
    - Generate API overview
- Show some C++ and/or Python code example and generate the API documentation for this.

### Project and user documentation

| Duration | Format |
| --- | --- |
| 20 | Slides |

- Wiki (Most do not allow Docs as code)
- Markdown:
    - [Jekyll](https://jekyllrb.com/): Ruby, Static site generator, initially microblogging engine, but can be use for everything.
        - Examples:
            - [precice.org](https://precice.org)
    - [mkdocs](https://www.mkdocs.org): Python, Static site generator, focuses on documentation.
        - Examples:
            - [Our course homepage](https://simulation-software-engineering.github.io/homepage/) is based on mkdocs using the [mkdocs-material](https://squidfunk.github.io/mkdocs-material/) theme. This includes some markdown extensions.
    - HedgeDoc?
        - Browser based.
        - Not really documenting of code, but for meetings, project ideas etc.
        - Allows to make slides as well.
- reStructuredText:
    - Sphinx
        - Site generator
        - Python
        - Heavily integrated in the Python ecosystem for documentation and homepage generation.

#### Demo

- Create initial project for mkdocs and extend it.
    - `mkdocs new PROJECTNAME`
    - `mkdocs serve`
    - Edit name of project in `mkdocs.yml`
    - Add another file `example.md` in `docs/` and add it to `mkdocs.yml`
    - Write something in the markdown files and check the rebuild home page.
    - Change theme.
- Repeat for Sphinx?


### Publication of user documentation

| Duration | Format |
| --- | --- |
| 10 of 30 minutes | Slides |

- Publication of documentations
    - [ReadTheDocs](https://readthedocs.org/)
    - GitHub Pages
- CI/CD for checking and deployment.
    - markdownlint:
        -Ruby
- Focus on ways to organize "docs as code". (Git lecture "If git diff does not work, it is the wrong format".)


## A love letter to pandoc

| Duration | Format |
| --- | --- |
| 20 minutes | Slides |

- Written in Haskell
- If you have structured text, it is easy to convert it to other formats
- Write notes/documentation etc. in a lightweight markup language and convert it beautiful looking text and/or slides via LaTeX or to reStructuredText or to Markdown or vice versa.
- Slide example!
- CV example?!
- One can try pandoc directly online [https://pandoc.org/try](https://pandoc.org/try)

## Exercise

| Duration | Format |
| --- | --- |
| 80-90 minutes | Exercise |

- mkdocs
    - Set up a new project
    - Fill it with content
    - Check the content locally using mkdocs' integrated web server
    - Publish something on GitHub pages.
- sphinx
    - Do the same as for mkdocs, but now with sphinx
    - Alternative to GitHub pages one could publish something at ReadTheDocs.
- pandoc
    - Write some CV example. This combines YAML with some LaTeX template.
        - Add some extra information.
        - Work smartly with lists of parameters. If one has a list of information, one wants proper separation via a comma for example.

## Further reading

### Other

- [Documenting Python](https://devguide.python.org/documenting/)
- [Mastering Markdown (GitHub Guide)](https://guides.github.com/features/mastering-markdown/)

### Markup languages

- [Markdown](https://daringfireball.net/projects/markdown/)
- [CommonMark](https://spec.commonmark.org/)
- [Markdown cheat sheet with focus on GitHub's flavor](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)
- [Sphinx' reStructuredText primer](https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html)
### Site generators

- [Jekyll](https://jekyllrb.com/)
- [mkdocs](https://www.mkdocs.org)

### CI tools

- [markdownlint based on Ruby](https://github.com/markdownlint/markdownlint)
- [markdownlint based on Node.js being influenced by the Ruby checker](https://github.com/DavidAnson/markdownlint)

