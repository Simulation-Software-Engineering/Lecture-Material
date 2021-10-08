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

## Suggestions

TODO: add links and 4 words explaining the software

BU

* FEniCS(-X): FEM library in Python
* deal.II: FEM library in C++
* preCICE: Coupling library (Stuttgart)
* SG++: Sparse grids library for high-dimensional numerics (Stuttgart) 
* MegaMol:
* ESPResSo:
* PETSc: LA library
* pyMOR: MOR library in Python


AJ

* pyiron: Workflow manager in Python
* DuMuX: CFD library based on DUNE in C++
* DUNE: Library for parallel mesh data structure in C++??
* Eigen: LA library in C++
* TRILINOS:
* NETGEN/NGSolve: 
* SU2: CFD code in C++
* SUNDIALS
* **Or your suggestion**

---

## How to Submit my Choice?

* Mail to Benjamin till **28th of October** (next Thursday) evening
* Priority list with at least three choices
* If not on our suggestion list, write short paragraph what the software does and give links

---

## Role of Advisor

* Alex or Benjamin
* Use exercise blocks and time after lectures for discussions
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

--- 

## TODOs for us

Check software suggestions:

* also criteria above!
* (relatively) modern RSE infrastructure used, good role models
* open for contributions, meaning there needs to be some statement or oral commitment
* if we have personal contact, we could let them know that sth is coming and that they should treat students as normal academic contributions (maybe have time frame in mind)
