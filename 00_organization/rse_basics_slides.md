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

# Introduction to Research Software Engineering

---

## Starting Points

- [DORA declaration](https://sfdora.org/) in 2012: reshape how research impact should be assessed underlining importance of software

> For the purposes of research assessment, consider the value and impact of all research outputs (including datasets and software) in addition to research publications ...

- [UK survey in 2014](https://zenodo.org/record/1183562): 7 out of 10 researchers could not conduct research without software.
- DFG funding calls on research software in 2016 & 2019 & [2022](https://www.dfg.de/en/news/news-topics/announcements-proposals/2022/info-wissenschaft-22-85)
- [Nationale Forschungsdaten Infrastruktur, NFDI](https://www.nfdi.de/?lang=en) since 2020
- Lack of careers for software developers in academia
- Lack of reproducibility of research that uses software (*"works for me on my machine today"* vs. *"works for everyone everywhere always"*)

---

## RSE Movement

... academic software developers needed a name:
**Research Software Engineers**

[UK Society of RSE](https://society-rse.org/):

> A Research Software Engineer (RSE) combines professional software engineering expertise with an intimate understanding of research.

- *"Movement"* started in the UK, first UK RSE conference in 2016
- First conferences in Germany and the Netherlands in 2019
- [first de-RSE position paper](https://f1000research.com/articles/9-295/v2) in 2020, [several working groups](https://de-rse.org/en/working_groups.html)
   - [learning and teaching RSE](https://de-rse.org/learn-and-teach/), [foundational competencies of an RSE](https://de-rse.org/blog/2024/10/08/identifying-the-foundational-competencies-of-an-RSE-en.html)
- Second Thursday of October is the [International RSE Day](https://researchsoftware.org/council/intl-rse-day.html)
- [Why be an RSE?](https://researchit.blogs.bristol.ac.uk/2021/10/14/international-rse-day-why-be-an-rse/) Interesting and novel projects, technical freedom, RSEs come from varied backgrounds, development for social good

---

## How is Simulation Software Engineering different from RSE?

> Why is the name of the course SSE and not RSE?

- Difference is not so big actually.
- Simulation research depends on software by definition (even less a *"by-product"* than for research in Chemistry, Biology, ...).
- Already prototypes are so complicated today that one (wo)man hero PhD projects are no longer feasible. --> Learn how to work with / contribute to community software.
- We focus on simulation software in the challenge.

---

## Do I need this in Industry?

- Yes. Research also happens in industry.
- All things we learn (Git, packaging, CI/CD, virtualization, documentation, ...) is also highly relevant for non-research software.
- Companies use (more and more) the same workflows and tools.
    - It is not just about coding. It is about collaborative work.
- Open-source development excellent door opener for industry.
- Some companies use open-source software and need to make contributions.
- Some companies develop their software as open-source software.
