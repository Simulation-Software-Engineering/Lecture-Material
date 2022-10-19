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


# Your Challenge: Contribute to Real Simulation Software

---

## Schedule

1. Pick a large-scale open-source simulation software (till **Oct 27**, evening)
2. Present the software: how you got it, what are main features, some tutorials you did, ... (**Nov 10**)
3. Present *"RSE infrastructure"* of the software: Which CI / documentation / building / git workflow ... does it use? How do contributions work? (**Dec 15**)
4. Contribute something small (but not trivial) to the software (*"good first issue"*). Run through complete contribution cycle (issue, discussion, PR, review, merge). Present what you did. Examples: feature, tutorial, documentation, support of new packaging tool, bugfix, ... (**Feb 9**)

Rough workload / grading weights: 25%, 25%, 50%

---

## Which Software to Pick?

- Something in the simulation universe (this includes equation solvers, meshing, scientific visualization, ...)
- Truly open source, all development in public
- Uses Git
- Written in Python or C++ (not a strict must)
- Real community project (not 1-2 PhD students developing, but multiple research groups behind project)
- A project that is open for contributions (`CONTRIBUTING.md` or similar)
- Ideally a software you have not worked with before (if you have, please discuss with us)
- Ideally, everybody picks something different

---

## Suggestions I

- [deal.II](https://dealii.org/): FEM library in C++
- [DuMuX](https://dumux.org/): CFD library based on DUNE in C++ (Stuttgart)
- [DUNE](https://www.dune-project.org/`): Modular toolbox for PDEs
- [Eigen](https://eigen.tuxfamily.org): LA library in C++
- [ESPResSo](https://espressomd.org): MD Simulator with Python API (Stuttgart)
- [FEniCS(-X)](https://fenicsproject.org/): FEM library in C++ with Python interface
- [Firedrake](https://www.firedrakeproject.org/): FEM library in Python
- [Gmsh](https://gmsh.info/): Mesh generator
- [LAMMPS](https://www.lammps.org/): MD simulator
- [Nalu-Wind](https://github.com/Exawind/nalu-wind): CFD solver for wind farms
- [Palabos](https://palabos.unige.ch/): Lattice Boltzmann method solver

---

## Suggestions II

- [OpenFAST](https://www.nrel.gov/wind/nwtc/openfast.html): Multi-fidelity wind turbine simulation tool
- [PETSc](https://petsc.org/): LA library
- [preCICE](https://precice.org/): Coupling library (Stuttgart)
- [pyiron](https://pyiron.org/): Workflow manager in Python
- [pyMOR](https://pymor.org/): MOR library in Python
- [SU2](https://su2code.github.io/): CFD code in C++
- [SUNDIALS](https://computing.llnl.gov/projects/sundials): Nonlinear solvers, ODEs
- [TRILINOS](https://trilinos.github.io/): Collection of scientific software libraries, mainly solvers
- [VisIt](https://visit-dav.github.io/visit-website/index.html): Scientific visualization software
- more projects in [xSDK](https://xsdk.info/packages/) or [NumFOCUS](https://numfocus.org/sponsored-projects)
- **Or your suggestion** (also agent-based or discrete event simulation software)

---

## How to Submit my Choice?

- [https://gitlab-sim.informatik.uni-stuttgart.de/simulation-software-engineering-wite2223/challenge](https://gitlab-sim.informatik.uni-stuttgart.de/simulation-software-engineering-wite2223/challenge)
- Comment in [issue #1](https://gitlab-sim.informatik.uni-stuttgart.de/simulation-software-engineering-wite2223/challenge/-/issues/1) till **27th of October** (next Thursday) evening (no FCFS)
- Priority list with at least three choices
- If not on our suggestion list, write short paragraph what the software does and give links

---

## Role of Advisor

- Benjamin or Ishaan
- Use exercise blocks and time after lectures for discussions
- Discuss at least what you plan to contribute
- Share links etc. to issues and PRs (or tag us)

---

## Presentations

- Length depends on students in course (maybe 5-10 mins for first two presentations, 10-20 mins for last)
- Everybody should learn something from every presentation
- Style: like a presentation in a team meeting, not like a presentation at a conference

---

## Reports

- Please also submit a report for each presentation
- 1-2 pages (2500-5000 chars)
- Written in markdown
- Submission via a merge request to the [GitLab challenge repo](https://gitlab-sim.informatik.uni-stuttgart.de/simulation-software-engineering/challenge)
- Add links, instructions, ... should work like a compact summary for everybody in the end
- Will be visible to everybody in SSE group
- We will prepare templates
