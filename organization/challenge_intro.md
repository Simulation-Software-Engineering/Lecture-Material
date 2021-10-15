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


# Your Challenge: Contribute to Real Simulation Software

---

## Schedule

1. Pick a large-scale open-source simulation software (till **Oct 28**, evening)
2. Present the software: how you got it, what are main features, some tutorials you did, ... (**Nov 11**)
3. Present *"RSE infrastructure"* of the software: Which CI / documentation / building / git workflow ... does it use? How do contributions work? (**Dec 16**)
4. Contribute something small (but not trivial) to the software (*"good first issue"*). Run through complete contribution cycle (issue, discussion, PR, review, merge). Present what you did. Examples: feature, tutorial, documentation, support of new packaging tool, bugfix, ... (**Feb 10**)

Rough workload / grading weights: 25%, 25%, 50%

---

## Which Software to Pick?

* Something in the simulation universe (this includes equation solvers, meshing, scientific visualization, ...)
* Truly open source, all development in public
* Uses Git
* Written in Python or C++ (not a strict must)
* Real community project (not 1-2 PhD students developing, but multiple research groups behind project)
* A project that is open for contributions (`CONTRIBUTING.md` or similar)
* Ideally a software you have not worked with before (if you have, please discuss with us)
* Ideally, everybody picks something different

---

## Suggestions I

* [deal.II](https://dealii.org/): FEM library in C++
* [DuMuX](https://dumux.org/): CFD library based on DUNE in C++ (Stuttgart)
* [DUNE](https://www.dune-project.org/`): Modular toolbox for PDEs
* [Eigen](https://eigen.tuxfamily.org): LA library in C++
* [ESPResSo](https://espressomd.org): MD Simulator with Python API (Stuttgart)
* [FEniCS(-X)](https://fenicsproject.org/): FEM library in Python
* [Firedrake](https://www.firedrakeproject.org/): FEM library in Python
* [Gmsh](https://gmsh.info/): Mesh generator
* [LAMMPS](https://www.lammps.org/): MD simulator
* [NETGEN/NGSolve](https://ngsolve.org`): FEM library in Python
* [Palabos](https://palabos.unige.ch/): Lattice Boltzmann

---

## Suggestions II

* [PETSc](https://petsc.org/): LA library
* [preCICE](https://precice.org/): Coupling library (Stuttgart)
* [pyiron](https://pyiron.org/): Workflow manager in Python
* [pyMOR](https://pymor.org/): MOR library in Python
* [SU2](https://su2code.github.io/): CFD code in C++
* [SUNDIALS](https://computing.llnl.gov/projects/sundials): Nonlinear solvers, ODEs
* [TRILINOS](https://trilinos.github.io/): Collection of scientific software libraries, mainly solvers
* more projects in [xSDK](https://xsdk.info/packages/): [Ginkgo](https://ginkgo-project.github.io/), ...
* **Or your suggestion**

---

## How to Submit my Choice?

* Mail to Benjamin till **28th of October** (next Thursday) evening
* Priority list with at least three choices
* If not on our suggestion list, write short paragraph what the software does and give links

---

## Role of Advisor

* Alexander or Benjamin
* Use exercise blocks and time after lectures for discussions
  * We both attend all lectures and labs
* Discuss at least what you plan to contribute
* Share links etc. to issues and PRs (or tag us)

---

## Presentations

* Length depends on students in course (maybe 5-10 mins for first two presentations, 10-20 mins for last)
* Everybody should learn something from every presentation
* Style: like a presentation in a team meeting, not like a presentation at a conference

---

## Reports

* Please also submit a report for each presentation
* 1-2 pages (2500-5000 chars)
* Written in markdown
* Submission via a merge request to (private) IPVS GitLab repo
* Add links, instructions, ... should work like a compact summary for everybody in the end
