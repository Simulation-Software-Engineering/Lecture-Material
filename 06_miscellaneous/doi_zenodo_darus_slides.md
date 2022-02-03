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

# DOI, Zenodo, and Dataverses

---

## Introduction

- How to reliably find and reuse research output?
    - Links may change
    - People might change affiliation
    - Services might stop operating
- Software and data is research output
    - Data might be large
- How to find/cite/preserve information?
- Important goals:
    - Findable information
    - Reusable information
- Research data management

---

## Digital Object Identifier (DOI) System

<img src="https://www.doi.org/img/banner-413.gif" width=30%; style="margin-left:auto; margin-right:auto; padding-top: 25px; padding-bottom: 25px;">

- Organized by [International DOI Foundation (IDF)](https://www.doi.org/)
- Standardized by ISO
- In use since 1998, launched in 2000
- Can refer to resources, parties, licenses, etc. (digital or physical)
- Used in different fields: Academia, EU...
- Different registration agencies
    - [Crossref](https://www.crossref.org/): Scholarly data (articles, book chapters etc.)
    - [DataCite](https://datacite.org/): Research datasets

---

## DOI Properties

- Has a `prefix/suffix` system
- Prefix usually `10.NUMBER`
    - `10.` refers to DOI namespace
- Suffix almost arbitrary string
- DOI Examples:

  ```text
  10.1000/182 (DOI handbook)
  10.5281/zenodo.5152939 (DuMuX 3.4.0)
  10.18419/darus-1778 (DaRUS dataset)
  ```

- Proxy (resolver) example: <https://www.doi.org>

    ```text
    https://www.doi.org/10.1000/182
    https://www.doi.org/10.18419/darus-1778
    ```

---

## Zenodo

<img src="https://about.zenodo.org/static/img/logos/zenodo-gradient-1000.png" width=30%; style="margin-left:auto; margin-right:auto; padding-top: 25px; padding-bottom: 25px;">


> Zenodo, a CERN service, is an open dependable home for the long-tail of science, enabling researchers to share and preserve any research outputs in any size, any format and from any science.

---

## Zenodo Properties

- Similar to [arxiv](https://arxiv.org/) not limited to preprints
- Storage option for
    - Papers/preprints
    - Datasets
    - Software
- Store data under a license
- Assigns DOI to data
- [Zenodo](https://zenodo.org/)'s code is [open source](https://github.com/zenodo/zenodo)

---

## DaRUS

<img src="https://www.izus.uni-stuttgart.de/fokus/img/logoDarusKreis.png" width=35%; style="margin-left:auto; margin-right:auto; padding-top: 25px; padding-bottom: 25px;">

University of Stuttgart's [Dataverse](https://dataverse.org/) instance

---

## DaRUS Properties

- Accessible at <https://darus.uni-stuttgart.de/>
- Store data according to FAIR principles
    - **F**indable
    - **A**ccessible
    - **I**nteroperable
    - **R**eusable
- Extensive metadata description
- Store data under a license
- Assigns DOI to data
- Indexed on [B2FIND](http://b2find.eudat.eu/group/darus), [OpenAIRE](https://explore.openaire.eu/) and [Google Dataset Search](https://datasetsearch.research.google.com)
- Demo instance [DemoDaRUS](https://demodarus.izus.uni-stuttgart.de/)

---

## Demo

---

## Further Reading

- [Digital Object Identifier System (DOI)](https://www.doi.org/)
- [DataCite: DOI basics](https://support.datacite.org/docs/doi-basics)
- [Zenodo](https://zenodo.org/)
- [The Dataverse Project](https://dataverse.org/)
- [DaRUS](https://darus.uni-stuttgart.de/)
- [Competence Center for Research Data Management](https://www.izus.uni-stuttgart.de/en/fokus/)
