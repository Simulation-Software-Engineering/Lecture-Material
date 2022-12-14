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
    font-family: 'Ubuntu Mono';
    color: orange;
  }
</style>


# Technical Writing

---

## Structure of This Lecture

1. Introduction
2. What is good documentation?
3. Standard documentation building blocks (README, changelog, error messages, commit messages)
4. API documentation

---

## 1. Introduction

---

## Documentation Survey (1/3)

- Who has been annoyed by bad (or lack of) documentation before?
- Examples?

---

## Documentation Survey (2/3)

- Who has been happy/surprised by very good documentation before?
- Examples?

---

## Documentation Survey (3/3)

- Who documents their code well?

---

## A Poem

> If people don’t know why your project exists,
they won’t use it.
> If people can’t figure out how to install your code,
they won’t use it.
> If people can’t figure out how to use your code,
they won’t use it.

Taken from [Write The Docs](https://www.writethedocs.org/guide/writing/beginners-guide-to-docs/#why-write-docs)

---

Similar message and highly recommended:
Bangerth and Heister, 2013: [What makes computational open source software libraries successful?](http://dx.doi.org/10.1088/1749-4699/6/1/015010)

---

## Learning Goals

- Be aware that documentation is crucial in RSE.
- Understand that there is a difference between documentation and **good documentation**.
- Know the purpose and basic structure of several **standard documentation building blocks** (README, commit message, changelog, ...).
- **Not**: Be able to really write good documentation. This takes practice and much more than 90 minutes.
- **Not**: Use any technical tools. This will come next week.

---

## Technical Writer

- ... is a job profile between technical know-how (computer science, engineering, ...) and language.
- ... can be a role in a software development team (*"documentation"*).
- There is a whole community, e.g. [Write the Docs](https://www.writethedocs.org/).

Much content of this lecture is taken from [Write the Docs](https://www.writethedocs.org/).

---

## Technical Writing in Research Software

- Like in a startup, **no dedicated technical writer in team** (even for large projects). Everybody does everything.
    - --> You need writing skills.
- In research, one writes a lot (papers, proposals, lecture material, ...).
    - --> Writing/communication skills are very important anyway.

---

## Why Write Documentation

- You will be using your code in 6 months.
- You want people to use your code.
- You want people to help out.
- You want your code to be better (act of putting words to paper requires a distillation of thought that may not be so easy).
- You want to be a better writer.

---

## 2. What is Good Documentation?

---

## Documentation Content Should Be

- **ARID** (*"Accept (some) Repetition in Documentation"*)
    - Not like good code (**DRY**: *"don't repeat yourself"*),
      but also not **WET**
    - Repetition from code to docs
    - Not everything can be auto-generated.
- **Skimmable**
    - Headings: should be descriptive and concise
    - Hyperlinks: descriptive, not [click here](https://www.smashingmagazine.com/2012/06/links-should-never-say-click-here/)
    - Use listings etc. where appropriate, no *"wall of text"*
- **Exemplary** (some, but not too many)
- **Consistent** (language, formatting, wording)
- **Current**

---

## Be Clear About Your Audience (1/2)

**User vs. developer documentation**:

- Distinction important for larger projects, not so important for smaller projects
- Sometimes also third category *"maintainer"*
- User docs: How to use the software?
- Dev docs: Why does the software work a certain way? Not only how
- Dev docs typically closer to where the code is than user docs
- Example: preCICE: [user docs](https://precice.org/docs.html), [dev docs](https://precice.org/dev-docs-overview.html), [dev docs close to code](https://github.com/precice/precice/blob/1444fd90536f629b08bcf52238816d3c4ca141e4/src/mapping/Mapping.hpp#L15-L32)

---

From [py-RSE](https://merely-useful.tech/py-rse/documentation.html):

> The best function names in the world aren't going to answer the questions “Why does the software do this?” and “Why doesn’t it do this in a simpler way?”

---

## Be Clear About Your Audience (2/2)

[py-RSE](https://merely-useful.tech/py-rse/documentation.html) distinguishes novices, competent practitioners, and experts (following [Wilson 2019, Teaching Tech Together](https://doi.org/10.1201/9780429330704))

- A **novice** doesn’t yet have a mental model of the domain. -> Needs **tutorials** that introduce key ideas one by one.
    - Good example: [deal.ii tutorials](https://dealii.org/developer/doxygen/deal.II/Tutorial.html)).
- A **competent practitioner** knows enough to accomplish routine tasks with routine effort. -> Needs **reference guides, cookbooks, and Q&A sites**.
    - Good example: [preCICE config reference](https://precice.org/configuration-xml-reference.html)).
- An **expert** need this material as well – nobody's memory is perfect.

---

## Style Guides (1/4)

Consistent tone and style ...

- makes content easier to read.
- reduces the reader's cognitive load.
- increases confidence in authority of content.

Read more: [Write the Docs on style guides](https://www.writethedocs.org/guide/writing/style-guides/)

---

## Style Guides (2/4)

- Different people write differently. Even the same person writes differently every day.
- Style guide contains a set of standards.
- Writer does not have to worry -> saves time.
- Traditional style guides have been around as long as publishing, e.g. [The Chicago Manual of Style](https://www.chicagomanualofstyle.org/).

---

## Style Guides (3/4)

Example: brief excerpt of [Google developer documentation style guide](https://developers.google.com/style)

- **Timeless documentation**: Avoid words such as *"currently"*, *"in the future"*, *"soon"*
- Use present tense, avoid *"will"*
    - Bad: *Send a query to the service. The server will send an acknowledgment.*
    - Good: *Send a query to the service. The server sends an acknowledgment.*

- **Exclamation points**: Don't use them. Rather use notices such as Note or Caution.

---

## Style Guides (4/4)

- **Headings**: Use "Sentence case for headings", not "Title Case for Headings"
- **Image URLs**: Use site-root-relative URL from same domain
- **Referring to filenames**: code font, word "file" after filename, exact spelling
    - Good: *In the following `build.sh` file, modify the default values for all parameters.*

- ... even [example person names](https://developers.google.com/style/examples#example-person-names)
- Another example: [SSE lecture material style guide](https://github.com/Simulation-Software-Engineering/Lecture-Material/blob/main/docs/styleguide.md)

---

## Tone of Voice (1/2)

... helps a lot to make tone of documentation consistent.

- If your software/product was a person, how would they be?
- Let it talk like this person.

> Example preCICE:
> - Three things to define character? Smart, approachable, responsible.
> - Does preCICE have a sense of humor? Yes. When do they use it? Only rarely.
> - ...

---

## Tone of Voice (2/2)

- Define how to talk to users

> Example preCICE:
> - Treat users as peers. preCICE is a Computer Science PhD student, user is a Mechanical Engineering PhD student.

- Example: [Google style guide – voice and tone](https://developers.google.com/style/tone)

---

## 3. Standard Documentation Building Blocks

---

## README

**Every** code should contain a README file. There is even [readme driven development](https://tom.preston-werner.com/2010/08/23/readme-driven-development.html).

Minimal variant should contain at least (following [Write the Docs](https://www.writethedocs.org/guide/writing/beginners-guide-to-docs/#readme)):

- What problem the project solves
- A small code example (for libraries) or how to run (for programs)
- A screenshot for code using a GUI or a visual part
- How to get support and a link to issue tracker
- Information for people who want to contribute back (also `CONTRIBUTING.md`)
- Installation instructions
- The code's license (also `LICENSE`)
- Frequently Asked Questions (FAQ)

---

## Changelog (1/2)

Following [Keep a Changelog](https://keepachangelog.com):

- **What is a changelog?**
    - *A changelog is a file which contains a curated, chronologically ordered list of notable changes for each version of a project. Focus on the "what", not the "how" and "why".*
- **Why keep a changelog?**
    - *To make it easier for users and contributors to see precisely what notable changes have been made between each release (or version) of the project.*
- **Who needs a changelog?**
    - *People do. Whether consumers or developers, the end users of software are human beings who care about what's in the software. When the software changes, people want to know why and how.*

[Example from SU2](https://github.com/su2code/SU2/releases/tag/v7.2.0)

---

## Changelog (2/2)

The **Keep a Changelog** convention groups by categories:

- **Added** for new features.
- **Changed** for changes in existing functionality.
- **Deprecated** for soon-to-be removed features.
- **Removed** for now removed features.
- **Fixed** for any bug fixes.
- **Security** in case of vulnerabilities.

There are [tools to auto-generate](https://github.com/github-changelog-generator/github-changelog-generator), but be careful.

> Don’t let your friends dump git logs into changelogs

---

## Error Messages (1/5)

From [How to write better error messages](https://opensource.com/article/17/8/write-effective-error-messages):

> The first time a user encounters an application's documentation, it's not always with the user manual or online help. Often, that first encounter with documentation is an error message.

---

## Error Messages (2/5)

Examples from preCICE before Spring 2020:

- *Safety Factor must be positive or 0*
- *Data with name "Forces" is not defined on mesh with ID 1.*
- *At least two participants need to be defined!*

What is wrong with these?

---

## Error Messages (3/5)

Examples from preCICE after Spring 2020 (error messages sprint):

- **Give context**:
    - *Participant "Fluid" uses mesh "FluidMesh" with safety-factor="-0.5". Please use a positive or zero safety-factor instead.*
- **Give advice**:
    - *Data with name "Forces" is not defined on mesh "FluidMesh". Please add `<use-data name="Forces"/>` under `<mesh name="FluidMesh/>`.*
- **Improve tone**:
    - *In the preCICE configuration, only one participant is defined. One participant makes no coupled simulation. Please add at least another one.*

---

## Error Messages (4/5)

Tips from [Write the Docs](https://www.writethedocs.org/guide/writing/style-guides/#error-messages):

- Provide explicit indication that something has gone wrong.
- Write like a human, not a robot.
- Don’t blame the user – be humble.
- Make the message short and meaningful.
- Include precise descriptions of exact problems.
- Offer constructive advice on how to fix the problem.

---

## Error Messages (5/5)

Who did something wrong? The software or the user?

- Example preCICE:
    - The user -> error
    - The software -> assertion
- Make this transparent to the user

---

## Commit Messages (1/3)

Same story again:

- Consistent
- Descriptive and concise (such that complete history becomes skimmable)
- Explain the "why" (the "how" is covered in the diff)

---

## Commit Messages (2/3)

[The seven rules of a great Git commit message](https://chris.beams.io/git-commit/):

- Separate subject from body with a blank line.
- Limit the subject line to 50 characters.
- Capitalize the subject line.
- Do not end the subject line with a period.
- Use the imperative mood in the subject line.
- Wrap the body at 72 characters.
- Use the body to explain what and why vs. how.

---

## Commit Messages (3/3)

Tags can also be useful (e.g. `[Bugfix]`), but consistency is key. Our [lecture material](https://github.com/Simulation-Software-Engineering/Lecture-Material/commits/main) is a bad example. :grin:

---

## 4. API Documentation

---

## Starting Remarks

- All basics apply (be consistent, descriptive, and concise; explain the why, ...)
- Consistency is also great for automatization: rendering, interlinking, suggestions by IDE, ... (next week)
- Different syntax (e.g. [Google style for Python](https://github.com/google/styleguide/blob/gh-pages/pyguide.md#38-comments-and-docstrings), [numpydoc style](https://numpydoc.readthedocs.io/en/latest/), [doxygen for C++ and more](https://www.doxygen.nl), [Javadoc](https://www.oracle.com/technical-resources/articles/java/javadoc-tool.html))
- The [API reference](https://developers.google.com/style/api-reference-comments) of the Google developer documentation style guide is a very good source, **language independent**, and used on the following slides.

---

## Class Documentation (1/2)

Description of a class or method is split into a **short** and a **long description**.

**Short description**:

- First sentence of description (many doc tools pick automatically)
- State intended purpose of class with information that can't be deduced from the class name and signature.
- Do not repeat the class name.
- Do not say "this class will/does ...".

Android's ActionBar class:

> A primary toolbar within the activity that may display the activity title, application-level navigation affordances, and other interactive items.

---

## Class Documentation (2/2)

**Long description**: how to use, key features, best practices, ...

Example: [preCICE API](https://precice.org/doxygen/main/classprecice_1_1SolverInterface.html)

---

## Method Documentation (1/3)

**Short description**:

- Briefly state what action the method performs.
- **Use present tense**:
    - *Adds a new bird to the ornithology list.*
    - *Returns a bird.*
- **Operation + return data**:
    - *Adds a new bird to the ornithology list and returns the ID of the new entry.*
- **"Getter" that returns a boolean**:
    - *Checks whether ...*
- **"Getter" that return sth else**:
    - *Gets the ...*
- **No return value**:
    - *Sets the ..., Updates the ..., Deletes the ..., Registers ..., Creates a ...*

---

## Method Documentation (2/3)

**Long description**: why and how to use the method, prerequisites, related methods, ...

---

## Method Documentation (3/3)

**Parameters**:

- **Non-boolean parameters**:
    - *The ID of the bird you want to get.*
    - *A description of the bird.*
- **Boolean parameters**:
    - *If true, turn traffic lines on. If false, turn them off.*
- **Return values**:
    - *The bird specified by the given ID.*
    - *True if the bird is in the sanctuary; false otherwise.*

Example: [preCICE API](https://precice.org/doxygen/main/classprecice_1_1SolverInterface.html)

---

## Summary

- Documentation/technical writing is important.
- Be clear about your audience.
- Documentation should be skimmable, concise, and consistent.
- For consistency, define and/or follow a style guide.
- There are conventions/styles for README, changelog, commit messages, error messages, API documentation

---

## Further Reading

- [py-rse appendix on documentation](https://merely-useful.tech/py-rse/documentation.html)
- [py-rse on docstrings](https://merely-useful.tech/py-rse/scripting.html#scripting-docstrings)
- [Write the Docs](https://www.writethedocs.org/)
- [I'd Rather Be Writing blog](https://idratherbewriting.com/)
- [Google developer documentation style guide](https://developers.google.com/style)
    - [Section on API documentation](https://developers.google.com/style/api-reference-comments)
