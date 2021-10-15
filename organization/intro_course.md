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
</style>

# Course Intro

---

## Corona Rules

* We need to check everybody's **3G status** and **registration for contact tracing**
  * Use hardware cactUS reader for both when entering the room (each session)
  * We are below 35 students --> Teachers need to check --> Please wait entering the room till we are there (15 mins before session)
  * Please act accordingly (e.g. fill out paper registration if needed or get tested if needed)
  * Check out after lecture
* Everybody in audience needs to wear an **FFP2 mask**
* Keep distance, but please don't spread equally over the large room

---

## The Lecturers

- Alex (Jaust) [`@ajaust`](https://github.com/ajaust)
- Benjamin (Uekermann) [`@uekerman`](https://github.com/uekerman)
- Ishaan (Desai) [`@IshaanDesai`](https://github.com/IshaanDesai)

---

## The Idea & Learning Goals


- No (advanced) programming course
- Learn about all the other things you need to develop research /
  simulation software (to become a *"Research Software Engineer"*):
  continuous integration, virtualization, building & packaging, documentation, ...
- Focus on tools for C++ and Python
- More than a *"3-days software carpentry workshop on Python and git"*
- Learn how to contribute to large-scale open-source simulation software projects
- Learn which important simulation software packages exist and how to use them

---

## Building Blocks

Two parallel branches:

- **Weekly lectures** (90 mins) and **exercises** (90 mins) to learn and train concepts and tools
  - Thursdays, 09:45–11:15 and 15:45–17:15
  - This lecture hall: 38.04
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
- Basic software development skills (bash, git, md, ...)
- Some simulation background

---

## Prerequisites: Infrastructure

- GitHub account
- We'll create an IPVS GitLab account for everyone
- Laptop with root access
- OK if we use Slido?

---

## Material

- Great new open-source book to recap: Irving, Hertweck, Johnston, Ostblom, Wickham, and Wilson: [Research Software Engineering with Python](https://merely-useful.tech/py-rse)
- All our material is on [GitHub](https://github.com/Simulation-Software-Engineering/lecture-materials)
- Mainly markdown ... use your favorite tool to render (simply GitHub viewer, [GWDG Hedgedoc](https://pad.gwdg.de/), [pandoc](https://pandoc.org/), ...)
- We'll add more as the semester goes
- We give many links to videos, docs, blog posts, podcasts, ...
- We currently do not plan to record lectures (but are open to do if needed)

---

## Contribute to the Material

- You, no joke :see_no_evil:
- Typos, broken links, ...
- Additional material
- By definition, we study quickly evolving technology ... help us staying up to date
- We do the course for the first time ... there will still be flaws
- Contribute by opening PRs (we'll obviously acknowledge contributions)
- Click `edit me` on website
- For large parts (new tool, new chapter, ...), discuss in issue first
- See also [`CONTRIBUTING.md`](TODO)

---

## Chapters

1. Organization and Introduction to RSE
2. Version Control
3. Virtualization and Containerization
4. Building and Packaging
5. Documentation
6. Testing and Continuous Integration
7. Legal, Archiving, Community, and More

---

## The Challenge

1. Pick a large-scale open-source simulation software (FEniCS, PETSc, SU2, TRILINOS, ...) (till **Oct 28**, evening)
2. Present the software: how you got it, what are main features, some tutorials you did, ... (**Nov 11**)
3. Present *"RSE infrastructure"* of the software: Which CI / documentation / building / git workflow ... does it use? How do contributions work? (**Dec 16**)
4. Contribute something small (but not trivial) to the software (*"good first issue"*). Run through complete contribution cycle (issue, discussion, PR, review, merge). Present what you did. Examples: feature, tutorial, documentation, support of new packaging tool, bugfix, ... (**Feb 10**)

---

## Time Table I

<style>
td {
  font-size: 35px
}
</style>

| Date | Type | Chapter | Topic | Lecturer |
| ---- | ---- | ------- |------ | -------- |
| 21.10. |Lecture | 1-2 | course intro, intro to SSE, VC basics | Benjamin |
| 21.10. |Lecture | 2 | Git: my workflow + quiz, software projects for challenge  | Benjamin |
| 28.10. |Lecture + presentations| 2 | *"my neat little Git trick"*, merge vs rebase, working in teams| Benjamin |
| 28.10. |Lab | 2 | *"Git cheat sheet"*  | Benjamin |
| 04.11. |Lecture | 3 | Virtualbox, Vagrant | Alex |
| 04.11. |Lecture | 3 | Docker, Singularity | Alex |
| 11.11. |Lab | 3 | tbd.  | Alex |
| 11.11. |Presentations | C | **1st student presentations** | students|

---

## Time Table II

<style>
td {
  font-size: 35px
}
</style>

| Date | Type | Chapter | Topic | Lecturer |
| ---- | ---- | ------- |------ | -------- |
| 18.11. |Lecture | 4 | CMake | |
| 18.11. |Lab | 4 | CMake | |
| 25.11. |Lecture | 4 | Packaging and package managers, pip, conda | Ishaan |
| 25.11. |Lab | 4 | pip and PyPI exercise | Ishaan |
| 02.12. |Lecture | 4 | tbd. |  |
| 02.12. |Lab | 4 | tbd. | |
| 09.12. |Lecture | 5 | documentation tools | Alex |
| 09.12. |Lab | 5 | tbd. |  |
| 16.12. |Lecture | 5 | Technical writing | Benjamin |
| 16.12. |Presentations | C | **2nd student presentations** | students |

---

## Time Table III

<style>
td {
  font-size: 35px
}
</style>

| Date | Type | Chapter | Topic | Lecturer |
| ---- | ---- | ------- |------ | -------- |
| 13.01. |Lecture | 6 | tbd. | |
| 13.01. |Lab | 6 | tbd. | |
| 20.01. |Lecture | 6 | tbd. | |
| 20.01. |Lab | 6 | tbd. | |
| 27.01. |Lecture | 7 | tbd. | |
| 27.01. |Lab | 7 | tbd. | |
| 03.02. |Lecture | 7 | tbd. | |
| 03.02. |Lecture | 7 | tbd. | |
| 10.02. |Presentations | C | **final student presentations** | students|
| 10.02. |Presentations | C | **final student presentations** | students|

---

## Examination

- *"Course accompanying examination"*: no exam, but continuous examination (more like a lab course or a seminar)
- We look at:
  - Challenge (outcome and presentations)
  - Exercises (not every detail, but *"passed"* or *"failed"*)
  - Overall engagement (interactive lecture, discussions, small presentations, ...)
- Let us know if you cannot come to a lecture / exercise (you don't have to give a reason)

---

## GitLab Account

- Please write a mail till tonight to Alex
- TODO
