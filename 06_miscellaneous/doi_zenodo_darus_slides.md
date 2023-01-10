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

## FAIR Research Data

Research data should be ...

- **F**indable (metadata, easy to find for humans and machines, ...)
- **A**ccessible (once found, how can one access data, ... open data ...)
- **I**nteroperable (with applications or workflows for analysis, storage, and processing ...)
- **R**eusable (documentation ...)

- Principles [published in 2016](https://doi.org/10.1038%2FSDATA.2016.18) by [GO FAIR](https://www.go-fair.org/)

> A bottom-up, stakeholder-driven and self-governed initiative that aims to implement the FAIR data principles

- Often research software regarded as data as well, but there is also [FAIR4RS](https://doi.org/10.15497/RDA00068)

## Challenges

How to reliably find, access, and reuse research output?

- Links may change
- People might change affiliation
- Services might stop operating
- Research data might be large
- Closed-source software, data formats, ...
- ...

---

## Digital Object Identifier (DOI) System

<img src="https://www.doi.org/img/banner-413.gif" width=30%; style="margin-left:auto; margin-right:auto; padding-top: 25px; padding-bottom: 25px;">

- Organized by [International DOI Foundation (IDF)](https://www.doi.org/)
- Standardized by ISO
- In use since 1998, launched in 2000
- Can refer to resources, machines, data, licenses, books, ... (digital and physical things)
- Used in different fields: Academia, EU, ...
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

> Zenodo, a CERN service, is an open dependable home for the long-tail of science, enabling researchers to share and preserve any research outputs in any size, any format and from any science.

- Storage option for
    - Papers/preprints
    - Datasets
    - Software
- Store data under a license
- Assigns DOI to data
- [Zenodo](https://zenodo.org/)'s code is [open source](https://github.com/zenodo/zenodo)
- Example: [DuMuX v3.5.0](https://zenodo.org/badge/DOI/10.5281/zenodo.6606582.svg)

---

## DaRUS

<img src="https://www.izus.uni-stuttgart.de/fokus/img/logoDarusKreis.png" width=35%; style="margin-left:auto; margin-right:auto; padding-top: 25px; padding-bottom: 25px;">

University of Stuttgart's [Dataverse](https://dataverse.org/) instance

- Accessible at <https://darus.uni-stuttgart.de/>
- Extensive metadata description
- Store data under a license
- Assigns DOI to data
- Indexed on [B2FIND](http://b2find.eudat.eu/group/darus), [OpenAIRE](https://explore.openaire.eu/) and [Google Dataset Search](https://datasetsearch.research.google.com)
- Demo instance [DemoDaRUS](https://demodarus.izus.uni-stuttgart.de/)
- Example: [Jaust et al. SFB1313 D02 data set](https://doi.org/10.18419/darus-1778)

---

## Further Reading

- [Digital Object Identifier System (DOI)](https://www.doi.org/)
- [DataCite: DOI basics](https://support.datacite.org/docs/doi-basics)
- [Competence Center for Research Data Management](https://www.izus.uni-stuttgart.de/en/fokus/)
