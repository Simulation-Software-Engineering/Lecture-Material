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

# Introduction to Version Control

---

## Learning Goals of Chapter

- Refresh and organize students' existing knowledge on Git (learn how to learn more).
- Students can explain difference between merge and rebase and when to use what.
- How to use Git workflows to organize research software development in a team.
- Get to know a few useful GitHub/GitLab standards and a few helpful tools.

---

## Why Do We Need Version Control?

Version control ...

- tracks changes to files and helps people share those changes with each other.
    - Could also be done via email / Google Docs / ..., but not as accurately and efficiently
- was originally developed for software development, but today cornerstone of *reproducible research*

> "If you can't git diff a file format, it's broken."

---

## The Alternative: A Story Told in File Names

<img src="http://phdcomics.com/comics/archive/phd052810s.gif" width=60% style="margin-left:auto; margin-right:auto">

[http://phdcomics.com/comics/archive/phd052810s.gif](http://phdcomics.com/comics/archive/phd052810s.gif)

---

## How Does Version Control Work?

- *master* (or *main*) copy of code in repository, can't edit directly
- Instead: check out a working copy of code, edit, commit changes back
- Repository records complete revision history
    - You can go back in time
    - It's clear who did what when

---

## A Very Short History of Version Control I

The old centralized variants:

- 1982: RCS (Revision Control System), operates on single files
- 1986 (release in 1990): CVS (Concurrent Versions System), front end of RCS, operates on whole projects
- 1994: VSS (Microsoft Visual SourceSafe)
- 2000: SVN (Apache Subversion), mostly compatible successor of CVS, *still used today*

---

## A Very Short History of Version Control II

Distributed version control:

- Besides remote master version, also local copy of repository
- More memory required, but much better performance
- For a long time: highly fragmented market
    - 2000: BitKeeper (originally proprietary software)
    - 2005: Mercurial
    - 2005: Git
    - A few more

Learn more: [Podcast All Things Git: History of VC](https://www.allthingsgit.com/episodes/the_history_of_vc_with_eric_sink.html)

---

## The Only Standard Today: Git

No longer a fragmented market, there is nearly only Git today:

- [Stackoverflow developer survey 2021](https://insights.stackoverflow.com/survey/2021#technology-most-popular-technologies):
    > "Over 90% of respondents use Git, suggesting that it is a fundamental tool to being a developer."
- All software project candidates for *contribution challenge* use Git
- Is this good or bad?

---

## More Facts on Git

Git itself is open-source: GPL license

- source on [GitHub](https://github.com/git/git), contributions are a bit more complicated than a simple PR
- written mainly in C
- started by Linus Torvalds, core maintainer since later 2005: Junio Hamano
