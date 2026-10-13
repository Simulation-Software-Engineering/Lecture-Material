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


# Challenge: Contribute to real simulation software

---

## The Challenge

- Contribute something small (but not trivial) to a large-scale open-source simulation software (*"good first issue"*)
- Examples: feature, tutorial, documentation, new packaging, bugfix, ...
- Run through complete cycle (issue, discussion, PR, review, merge)

---

## Timeline

1. Pick a simulation software project
2. **Presentation 1**: How you got the software, what are main features, some tutorials you did, ...
3. **Presentation 2**: *"RSE infrastructure"* of the software:<br/> Which CI / documentation / building / git workflow ... does it use? How do contributions work?
4. Suggest contribution
5. **Presentation 3**: Your contribution

---

## Grading

Challenge / exercises / engagement = 45% / 50% / 5%

The challenge part:

- All 3 reports: **3/9**
- Presentation: **2/9**
- Actual contribution: **2/9** difficulty + **2/9** quality
    - **difficulty**: extent / difficulty of the contribution
    - **quality**: how well executed? Communication, documentation, tests, ... (*"net benefit"* for maintainers?)
- *"outstanding"* / *"good"* / *"ok"* / *"not enough"* (*"good"* -> 1.0)
- You need to pass (at least *"ok"*) all steps individually

---

## Example contributions

1. Ported several demo cases ([see one](https://github.com/FEniCS/dolfinx/pull/2508)) from FEniCS to [FEniCSx](https://fenicsproject.org/): difficulty *"outstanding"* (before widespread AI assistance)
2. [Improved website search](https://github.com/MakieOrg/Makie.jl/pull/2474) of [Makie](https://makie.org/website/): difficulty *"good"*
3. [Solved a simple good first issue](https://github.com/pymor/pymor/pull/1898) in [pyMOR](https://pymor.org/): difficulty *"ok"*

(all did a good or outstanding job in terms of quality)

---

## Which software to pick?

- Something in the simulation universe (this includes equation solvers, meshing, scientific visualization, (AI), ...)
- Truly open source, all development in public
- Uses Git
- Real community project (not 1-2 PhD students developing, but multiple research groups behind project)
- A project that is open for contributions (`CONTRIBUTING.md` or similar)
- Ideally a software you have not worked with before (if you have, please discuss with us)
- Ideally, everybody picks something different
- You need to understand the background at least a bit

---

## Suggestions I

- [deal.II](https://dealii.org/): FEM library in C++
- [DuMuX](https://dumux.org/): CFD library based on DUNE in C++ (Stuttgart)
- [DUNE](https://www.dune-project.org/): Modular toolbox for PDEs
- [Eigen](https://eigen.tuxfamily.org): LA library in C++
- [ESPResSo](https://espressomd.org): MD Simulator with Python API (Stuttgart)
- [Firedrake](https://www.firedrakeproject.org/): FEM library in Python
- [LAMMPS](https://www.lammps.org/): MD simulator
- [MercuryDPM](https://www.mercurydpm.org/home): particle code
- [MFEM](https://mfem.org/): FEM library in C++
- [NeoFOAM](https://exasim-project.com/NeoFOAM/)
- [Kynema-UGF](https://github.com/kynema/kynema-ugf): CFD solver for wind farms
- [Palabos](https://palabos.unige.ch/): Lattice Boltzmann method solver

---

## Suggestions II

- [PETSc](https://petsc.org/): LA library
- [pyiron](https://pyiron.org/): Workflow manager in Python
- [pyMOR](https://pymor.org/): MOR library in Python
- [pyLife](https://pylife.readthedocs.io/en/stable/): fatigue of mechanical components in Python
- [SU2](https://su2code.github.io/): CFD code in C++
- [SUNDIALS](https://computing.llnl.gov/projects/sundials): Nonlinear solvers, ODEs
- [TRILINOS](https://trilinos.github.io/): Collection of scientific software libraries, mainly solvers
- [VisIt](https://visit-dav.github.io/visit-website/index.html): Scientific visualization software
- more projects in [NumFOCUS](https://numfocus.org/sponsored-projects) or [HiRSE Code Promotion](https://www.helmholtz-hirse.de/promo.html)
- **Or your suggestion** (also agent-based or discrete event simulation software)

---

## The Challenge: Advice

- Pick something from your background
- Don't choose based on the programming language
- Start early, persist with questions, iterate quickly
- Start with something clear, extend with a second contribution
- Contact us early in case of trouble
- Make reviews easy for maintainers (will return to this)

---

## What happens if maintainers do not react?

- Give them time, contact early
- Not your fault
- Keep all communication public, then easy for us to review

---

## How to submit my choice?

- Challenge repository (see `timetable.md`)
- Comment in `work item #1` till next Wednesday evening (no FCFS)
- Priority list with at least three choices
- If **not** on our suggestion list, motivate and give links
- Add pre-knowledge that you have in the field. For example, if you pick pyMOR, you should know already what MOR is.

---

## Role of advisor

- Felix, Frédéric, Serge, or Gerasimos
- Use, for example, exercise blocks and time before and after lectures for discussions
- Share links etc. to issues and PRs (or tag us)

---

## Presentations

- Length depends on number of students in course (maybe 5-10 mins)
- Everybody has to present once or twice (depending on number of students)
- Everybody should learn something from every presentation
- Style: like a presentation in a team meeting, not like a presentation at a conference

---

## Reports

- Submit a report for each step
- 1-2 pages (2500-5000 chars)
- Written in Markdown
- Submission via a merge request to the GitLab challenge repo
- Add links, instructions, ... should work like a compact summary for everybody in the end
- Will be visible to everybody in SSE group
- We will prepare templates
