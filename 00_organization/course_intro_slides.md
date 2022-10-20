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
  .reveal section img {
    background:none;
    border:none;
    box-shadow:none;
  }
</style>


# Simulation Software Engineering

---

## The Lecturers

- Benjamin (Uekermann) [`@uekerman`](https://github.com/uekerman)
- Ishaan (Desai) [`@IshaanDesai`](https://github.com/IshaanDesai)

SSE Hall of Fame:

- Alexander (Jaust) [`@ajaust`](https://github.com/ajaust)

---

## The Idea & Learning Goals

- No (advanced) programming course
- Learn about all the other things you need to develop research /
    simulation software (to become a *"Research Software Engineer"*):
    continuous integration, virtualization, building & packaging, documentation, ...
- Focus on tools for C++ and Python
- More than a *"3-days software carpentry workshop on Python and Git"*
- Learn how to contribute to large-scale open-source simulation software projects
- Learn which important simulation software packages exist and how to use them

---

## Building Blocks

Two parallel branches:

- **Weekly lectures** (90 mins) and **exercises** (90 mins) to learn and train concepts and tools
    - Thursdays, 09:45–11:15 and 15:45–17:15
    - This room: 38-0.124
    - No strict distinction between lecture and exercise
    - Interactive style (not a theory course)
- **Individual challenge**: contribute to real simulation software :rocket:
    - List of software candidates: this afternoon
    - 3 presentations from you (more later)
    - You get a direct advisor
    - Use exercise blocks and time after lectures for discussions

---

## Prerequisites: Skills

- Basic programming (Python, C++)
- Basic software development skills (bash, Git, md, ...)
- Some simulation background

---

## Prerequisites: Infrastructure

- GitHub account
- We'll create an IPVS-SIM GitLab account for everyone
- Laptop with root access
    - You should be able to install and configure software.
- OK if we use Slido?
- Signed up on C@MPUS?

---

## Material

- Great new open-source book to recap: Irving, Hertweck, Johnston, Ostblom, Wickham, and Wilson: [Research Software Engineering with Python](https://merely-useful.tech/py-rse)
- All our material is on [https://github.com/Simulation-Software-Engineering](https://github.com/Simulation-Software-Engineering)
- Mainly markdown ... use your favorite tool to render (simply GitHub viewer, [GWDG Hedgedoc](https://pad.gwdg.de/), [stuvus Hedgedoc](https://pad.stuvus.de/), [pandoc](https://pandoc.org/), [PDFs generated in CI](https://github.com/Simulation-Software-Engineering/Lecture-Material/actions/workflows/create-pdfs-from-markdown.yml), ...)
- We rework the material as the semester goes
- We give many links to videos, docs, blog posts, podcasts, ...
- Recordings of the lecture from last year as a backup on ILIAS. Please always come when possible. What we do is interactive.

---

## Contribute to the Material

- You, no joke :see_no_evil: ([many students contributed last year](https://github.com/Simulation-Software-Engineering/Lecture-Material/graphs/contributors))
- Typos, broken links, ...
- Additional material
- By definition, we study quickly evolving technology ... help us staying up to date
- There are surely still flaws in the material ... help us fix them
- Contribute by opening PRs
- Click `edit me` on website
- For large parts (new tool, new chapter, ...), discuss in issue first
- See also [`CONTRIBUTING.md`](https://github.com/Simulation-Software-Engineering/lecture-materials/blob/main/CONTRIBUTING.md)

---

## Chapters

1. Version Control
2. Virtualization and Containers
3. Building and Packaging
4. Documentation
5. Testing and Continuous Integration
6. Miscellaneous

---

## The Challenge

1. Pick a large-scale open-source simulation software (FEniCS, PETSc, SU2, TRILINOS, ...) (till **Oct 27**, evening)
2. Present the software: how you got it, what are main features, some tutorials you did, ... (**Nov 10**)
3. Present *"RSE infrastructure"* of the software: Which CI / documentation / building / git workflow ... does it use? How do contributions work? (**Dec 15**)
4. Contribute something small (but not trivial) to the software (*"good first issue"*). Run through complete contribution cycle (issue, discussion, PR, review, merge). Present what you did. Examples: feature, tutorial, documentation, support of new packaging tool, bugfix, ... (**Feb 9**)

---

## Time Table I

<style>
td {
    font-size: 35px
}
</style>

| Date | Type | Chapter | Topic | Lecturer |
| ---- | ---- | ------- |------ | -------- |
| 20.10. |Lecture | 0-1 | Course intro, intro to SSE, VC basics | Benjamin |
| 20.10. |Lecture | 1 | Git: my workflow + quiz, software projects for challenge | Benjamin |
| 27.10. |Lecture | 3 | Packaging, pip and PyPI | Ishaan |
| 27.10. |Lab | 3 | pip and PyPI exercise | Ishaan |
| 03.11. |Lecture + presentations| 1 | *"My neat little Git trick"*, merge vs rebase, working in teams| Benjamin |
| 03.11. |Lab | 1 | Git exercise | Ishaan |
| 10.11. |Lecture | 2 | Virtual machines | Ishaan |
| 10.11. |Presentations | C | **1st student presentations** | students |

---

## Time Table II

<style>
td {
    font-size: 35px
}
</style>

| Date | Type | Chapter | Topic | Lecturer |
| ---- | ---- | ------- |------ | -------- |
| 17.11. |Lecture | 2 | Containers | Ishaan |
| 17.11. |Lab | 2 | Virtual machines and containers | Ishaan |
| 24.11. |Lecture | 3 | Make and CMake | Benjamin
| 24.11. |Lab | 3 | CMake | Benjamin |
| 01.12. |Lecture | 3 | CPack, Debian packages | tbd. |
| 01.12. |Lab | 3 | CPack, Debian packages | tbd. |
| 08.12. |Lecture + Lab | 3 | Spack | Ishaan |
| 08.12. |Lecture | 4 | tbd. | Benjamin |
| 15.12. |Lecture | 4 | tbd. | Benjamin |
| 15.12. |Presentations | C | **2nd student presentations** | students |

---

## Time Table III

<style>
td {
    font-size: 35px
}
</style>

| Date | Type | Chapter | Topic | Lecturer |
| ---- | ---- | ------- |------ | -------- |
| 12.01. |Lecture | 5 | Testing in Python | Ishaan |
| 12.01. |Lab | 5 | Testing in Python | Ishaan |
| 19.01. |Lecture | 5 | Automation, CI/CD | Benjamin |
| 19.01. |Lab | 5 | Automation, CI/CD | Benjamin |
| 26.01. |Lecture | 5 | Boost.Test | Benjamin |
| 26.01. |Lab | 5 | Boost.Test | Benjamin |
| 02.02. |Lecture | 6 | Licenses, versioning, ... | Benjamin |
| 02.02. |Lecture | 6 | tbd. | tbd. |
| 09.02. |Presentations | C | **final student presentations** | students|
| 09.02. |Presentations | C | **final student presentations** | students|

---

## Examination

- *"Course accompanying examination"*: no exam, but continuous examination (more like a lab course or a seminar)
- We look at:
    - Challenge (outcome and presentations), (~50%)
    - Exercises (not every detail, but *"passed"* or *"failed"*) (~40%)
    - Overall engagement (interactive lecture, discussions, small presentations, contributions, ...) (~10%)
- Let us know if you cannot come to a lecture / exercise (you don't have to give a reason)
- You will need to register yourself to the *"exam"* on C@MPUS
- Point of no return: Once you gave the first presentation (Nov 11), you have to register (please let us still know when you drop just before the presentation)

---

## GitLab Account

- Please write a mail till tonight to Ishaan
    - [ishaan.desai@ipvs.uni-stuttgart.de](mailto:ishaan.desai@ipvs.uni-stuttgart.de)
- Email subject: "GitLab account SSE course"
- State your **name** and preferred **email-address**
- If you already have an IPVS-SIM GitLab account, we only need your username
- We will then add you to the `Simulation Software Engineering` group
