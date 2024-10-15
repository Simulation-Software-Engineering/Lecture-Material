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
  .reveal section h3 {
    color: orange;
    text-align: left; 
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
- Gerasimos (Chourdakis) [`@MakisH`](https://github.com/MakisH)
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
    - Wednesdays, 09:45–11:15 and 15:45–17:15
    - This room: 38-0.108
    - No strict distinction between lecture and exercise
    - Interactive style (not a theory course)
- **Individual challenge**: contribute to real simulation software :rocket:
    - List of software candidates: this afternoon
    - 3 rounds of presentations from you (more later)
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
- We will create IPVS-SIM GitLab accounts for everyone
- Laptop with root access
    - You should be able to install and configure software.

---

## Waiting List

- Students who have a fixed spot (top 40) in either the lecture or the exercise get in.
- We take 50 students in total.
- Remaining spots are filled by waiting list provided presence or excused today.
- We manually add these students at the end of this week.

---

## Material

- Great open-source book to recap: Irving, Hertweck, Johnston, Ostblom, Wickham, and Wilson: [Research Software Engineering with Python](https://third-bit.com/py-rse/)
- All our material is on [https://github.com/Simulation-Software-Engineering](https://github.com/Simulation-Software-Engineering)
- Mainly markdown ... use your favorite tool to render (simply GitHub viewer, [GWDG Hedgedoc](https://pad.gwdg.de/), [stuvus Hedgedoc](https://pad.stuvus.de/), [pandoc](https://pandoc.org/), [PDFs generated in CI](https://github.com/Simulation-Software-Engineering/Lecture-Material/actions/workflows/create-pdfs-from-markdown.yml), [Marp example](https://github.com/uekerman/sse-marp-example), ...)
- We rework the material as the semester goes.
- We give many links to videos, docs, blog posts, podcasts, ...

---

## Contribute to the Material

- You, no joke :see_no_evil: ([many students already contributed](https://github.com/Simulation-Software-Engineering/Lecture-Material/graphs/contributors))
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

- Contribute something small (but not trivial) to a large-scale open-source simulation software (*"good first issue"*)
- Examples: feature, tutorial, documentation, new packaging, bugfix, ...
- Run through complete cycle (issue, discussion, PR, review, merge)

### Timeline

1. Pick a software (till **Oct 23**, evening)
2. Present the software: how you got it, what are main features, some tutorials you did, ... (**Nov 6**)
3. Present *"RSE infrastructure"* of the software: Which CI / documentation / building / git workflow ... does it use? How do contributions work? (**Dec 11**)
4. Suggest contribution (**Dec 16**)
5. Present the contribution (**Feb 5**)

---

## Time Table I

<style>
td {
    font-size: 35px
}
</style>

| Date | Type | Chapter | Topic | Lecturer |
| ---- | ---- | ------- |------ | -------- |
| 16.10. |Lecture | 0-1 | Course intro, intro to SSE, VC basics | Benjamin |
| 16.10. |Lecture | 1 | Git basics, my Git workflow, Git quiz, how to challenge  | Benjamin |
| 23.10. |Lecture | 1 | *My neat little Git trick*, merge vs rebase, working in teams| Benjamin |
| 23.10. |Lab | 1 | Git  | Benjamin |
| 30.10. |Lecture | 2 | Intro containers, Docker, Singularity | Gerasimos |
| 30.10. |Lecture | 2 | Intro virtualization, VirtualBox, Vagrant | Gerasimos |
| 06.11. |Lab | 2 | Virtualization and containers | Gerasimos |
| 06.11. |Presentations | C | **1st student presentations** | students |

---

## Time Table II

<style>
td {
    font-size: 35px
}
</style>

| Date | Type | Chapter | Topic | Lecturer |
| ---- | ---- | ------- |------ | -------- |
| 13.11. |Lecture | 3 | Intro packaging, Python packaging | Ishaan |
| 13.11. |Lab | 3 | Python packaging | Ishaan |
| 20.11. |Lecture | 3 | Linux fundamentals, Make, CMake | Benjamin |
| 20.11. |Lab | 3 | CMake and Docker | Benjamin |
| 27.11. |Lecture | 3 | Spack | Ishaan |
| 27.11. |Lab | 3 | Spack | Ishaan |
| 04.12. |Lecture | 3 | CPack and more CMake | Benjamin |
| 04.12. |Lab | 3 | CPack | Benjamin |
| 11.12. |Lecture | 4 | Technical writing | Gerasimos |
| 11.12. |Presentations | C | **2nd student presentations** | students |

---

## Time Table III

<style>
td {
    font-size: 35px
}
</style>

| Date | Type | Chapter | Topic | Lecturer |
| ---- | ---- | ------- |------ | -------- |
| 08.01. |Lecture | 4 | Markup, Pandoc, website gener. | Benjamin |
| 08.01. |Lecture | 6 | FLOSS, versioning, repo layouts, DOI, Zenodo, DaRUS | Benjamin |
| 15.01. |Lecture | 5 | Intro testing, testing in Python | Ishaan |
| 15.01. |Lab | 5 | Testing in Python | Ishaan |
| 22.01. |Lecture | 5 | Automation, GitHub Actions, GitLab CI | Gerasimos|
| 22.01. |Lab | 5 | GitHub Actions | Gerasimos|
| 29.01. |Lecture | 5 | Boost.Test and CTest | Benjamin |
| 29.01. |Lab | 5 | Boost.Test and CTest | Benjamin |
| 05.02. |Presentations | C | **3rd student presentations** | students |
| 05.02. |Presentations | C | **3rd student presentations** | students |

---

## Examination

- *"Course accompanying examination"*: no exam, but continuous examination (more like a lab course or a seminar)
- Attendance is mandatory.
- We look at:
    - Challenge (reports, presentations, contribution) (45%)
    - Exercises (not every detail, but *"outstanding"* / *"passed"* / *"failed"* ) (50%)
    - Overall engagement (interactive lecture, discussions, small presentations, contributions, ...) (5%)
- You will need to register yourself to the *"exam"* on C@MPUS.
- Point of no return: Once you handed in the first report (Nov 6), you have to register.

---

## GitLab Account

- Please write a mail till tonight to Ishaan.
    - [ishaan.desai@ipvs.uni-stuttgart.de](mailto:ishaan.desai@ipvs.uni-stuttgart.de)
- Email subject: "GitLab account SSE course"
- State your **name** and preferred **email-address**
- If you already have an IPVS-SIM GitLab account, we only need your username.
- We will then add you to the `Simulation Software Engineering` group.
