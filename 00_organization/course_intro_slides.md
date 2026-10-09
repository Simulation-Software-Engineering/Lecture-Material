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

- Gerasimos (Chourdakis) [`@MakisH`](https://github.com/MakisH)
- Frédéric (Simonis) [`@fsimonis`](https://github.com/fsimonis)
- Felix (Neubauer) [`@Logende`](https://github.com/Logende)
- On leave this year: Benjamin (Uekermann) [`@uekerman`](https://github.com/uekerman)

Additional challenge advisors:

- Serge Kotchourko [`@kotserge`](https://github.com/kotserge)

SSE Hall of Fame:

- Alexander (Jaust) [`@ajaust`](https://github.com/ajaust)
- Ishaan (Desai) [`@IshaanDesai`](https://github.com/IshaanDesai)

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
    - Wednesdays, 09:45–11:15 (in V47.05) and 15:45–17:15 (in 38-0.124, might be too small in the beginning)
    - Typically lecture in the morning and exercise in the afternoon
- **Individual challenge**: contribute to real simulation software :rocket:
    - List of software candidates: this afternoon
    - 3 rounds of presentations from you (more later)
    - You get a direct advisor
    - Use time before and after lectures for discussions

---

## Prerequisites: Skills

- Basic programming (Python, C++)
- Basic software development skills (bash, Git, md, ...)
- Some simulation background
    - SimTech, COMMAS students: no issue
    - CS, SE: ideally through Numerical Fundamentals (NumGL) and Fundamentals of Scientific Computing (WissRech)

---

## Prerequisites: Infrastructure

- GitHub account
- We will create IPVS-SIM GitLab accounts for everyone
- Laptop with root access
    - You should be able to install and configure software.

---

## Material

- Great open-source book to recap: Irving, Hertweck, Johnston, Ostblom, Wickham, and Wilson: [Research Software Engineering with Python](https://third-bit.com/py-rse/)
- All our material is on [https://github.com/Simulation-Software-Engineering](https://github.com/Simulation-Software-Engineering)
- Mainly markdown ... use your favorite tool to render (simply GitHub viewer, [GWDG Hedgedoc](https://pad.gwdg.de/), [stuvus Hedgedoc](https://pad.stuvus.de/), [pandoc](https://pandoc.org/), [PDFs generated in CI](https://github.com/Simulation-Software-Engineering/Lecture-Material/actions/workflows/create-pdfs-from-markdown.yml), [Marp example](https://github.com/uekerman/sse-marp-example), ...)
- We rework the material as the semester goes.
- We give links to docs, videos, blog posts, podcasts, ...

---

## Contribute to the Material

- You, no joke :see_no_evil: ([many students already contributed](https://github.com/Simulation-Software-Engineering/Lecture-Material/graphs/contributors))
- Typos, broken links, ...
- Additional material
- By definition, we study quickly evolving technology ... help us staying up to date
- There are surely still flaws in the material ... help us fix them
- Contribute by opening PRs
- For large parts (new tool, new chapter, ...), discuss in issue first
- See also [`CONTRIBUTING.md`](https://github.com/Simulation-Software-Engineering/lecture-materials/blob/main/CONTRIBUTING.md)

---

## Use of Generative AI

- Also changes RSE rapidly
- Even more important: having a good overview of technology and being able to **read** code (what we teach in this course)
- If you use generative AI for your exercises or your challenge: **mandatory** to make this transparent (which parts of your code, how, ...)
- It is important, experiment! But also build a firm understanding of the basics of technology!

---

## Chapters

1. Version Control
2. Virtualization and Containers
3. Building and Packaging
4. Documentation
5. Testing and Continuous Integration
6. Miscellaneous

---

## Topic Overview Demo

---

## The Challenge

- Contribute something small (but not trivial) to a large-scale open-source simulation software (*"good first issue"*)
- Examples: feature, tutorial, documentation, new packaging, bugfix, ...
- Run through complete cycle (issue, discussion, PR, review, merge)

### Timeline

- Pick a software project to contribute to
- **Step 1**: Present the software: how you got it, what are main features, some tutorials you did, ...
- **Step 2**: Present *"RSE infrastructure"* of the software: Which CI / documentation / building / git workflow ... does it use? How do contributions work?
- Suggest contribution
- **Step 3**: Present the contribution

---

## Timetable

See [GitHub: timetable.md](https://github.com/Simulation-Software-Engineering/Lecture-Material/blob/main/timetable.md)

---

## Examination

- *"Course accompanying examination"*: no exam, but continuous examination (more like a lab course or a seminar)
- Attendance is mandatory
- We look at:
    - Challenge (reports, presentations, contribution; more in the afternoon) (45%)
    - Exercises (not every detail, but *"outstanding"* / *"good"* / *"ok"* / *"not enough"* ) (50%)
    - Other (e.g. contributions to lecture material, ...) (5%)
- *"good"* everywhere leads to 1.0.
- We give (brief) feedback after every exercise.
- You will need to register yourself to the *"exam"* on C@MPUS.
- Last in: The deadline to pick a software
- Last out: Once you handed in the first report

---

## GitLab Account

- Please write a mail till tonight to Gerasimos.
    - [gerasimos.chourdakis@ipvs.uni-stuttgart.de](mailto:gerasimos.chourdakis@ipvs.uni-stuttgart.de)
- Email subject: "GitLab account SSE course"
- State your **name** and preferred **email-address**
- If you already have an IPVS-SIM GitLab account, we only need your username.
- We will then add you to the `Simulation Software Engineering` group.
