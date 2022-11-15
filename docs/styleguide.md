# Style Guide for SSE Lecture Material

## Names of Folders and Files

- Use `snail_case`. Only exception are standard files such as `CONTRIBUTING.md`.
- Slides end with `_slides.md`, demo notes with `_demo.md`, and exercise sheets with `_exercise.md`.

## Headings

- Use "Title Case for Headings".
- Each document has exactly one h1 heading.

## Listings

The two important questions are:

- Should an item start with a capital or a lower case letter?
- How should an item end?

### Full Sentences

- ... start with a capital letter.
- ... end with a period, a questions mark, or an exclamation mark. Use exclamation marks with care (do not shout at the student).

Example:

> - Running predefined workflows is simple.

### Items that are not full Sentences

- ... also start with a capital letter.
- ... do **not** end with a period, but can end with a question mark, or an exclamation mark. Use exclamation marks with care (do not shout at the student).

Example:

> - Ensuring reproducible test environments

### Half Sentences

What if the sentence starts in a heading and continues in the item?

- Start the item with `...`, a space, and then a lower case letter
- End with a period, a question mark, or an exclamation mark

Example:

> Git
> - ... is a version control system.
> - ... is very important.

### More Rules

- After a colon:
    - Start a full sentence with a capital letter.
    - Otherwise, start with a lower-case letter.
- Use [Oxford Comma](https://en.wikipedia.org/wiki/Serial_comma) in a series of three or more terms.

## Links

- Do not use [click here](https://www.smashingmagazine.com/2012/06/links-should-never-say-click-here/) links.

## Slides

- Each slide has exactly one heading, which is a h2 heading.
- If headings are repeated on consecutive slides, use the following construction:

> Some Title Case Heading 1/2
> Some Title Case Heading 2/2

- If a sentence needs to be highlighted, add **Note** before it, for example:

> **Note**: This particular concept is only applicable for specific compilers.

## Learning Goals

### Style

- Start with a verb. Think of an implicit "After listening to all lectures and doing all exercises of this unit, students are able to ...".
- Be specific.

> - Describe the tools available within the preCICE ecosystem and their usage (performance analysis, testing of data mapping, . . . ).
> - Navigate the preCICE documentation and all community channels.
> - Choose and apply common software engineering concepts for a preCICE adapter for a given
solver.

### Location

- In the `README.md` of each chapter
- On the [course content page](https://simulation-software-engineering.github.io/homepage/course-content/) of the website
- At the beginning of intro slides set of each chapter
- Do not use separate learning goals for a specific lecture session. However, listing parts of or all learning goals again is possible.
