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
</style>

# Introduction to Make

---

## Learning Goals of This Unit

- Understand the basic functionality of makefiles (timestamps, dependencies, update rules).
- Read simple makefiles and know where to look for additional material for complex makefiles.
- Write simple makefiles for small projects.

---

## Demo Part 1

Introduce `Hello-World` example

---

## What is Make?

- A build system
- The / a go-to solution for small (research) projects (e.g., latex document, processing data, ...), though also used in big projects ([Linux kernel](https://github.com/torvalds/linux))
- A building block for CMake
- Nice non-expert introduction in [py-RSE book, chapter 9](https://merely-useful.tech/py-rse/automate.html)
- [GNU Make](https://www.gnu.org/software/make/): standard implementation of Make for Linux and macOS

---

## How Does it Work?

- When you create / change a file, the OS updates timestamp of file.
- Make compares timestamps to see which files are older / newer than others.
- In `Makefile`:
    - Rules which file(s) depend on which other file(s)
    - Rules how to update out-of-date files
- When you run `make`, Make updates out-of-date files including transitive dependencies in correct order.

---

## Demo Part 2

- Single rule makefile
- Multiple rules
- Phony targets

---

## Advanced Make

- There is more:
    - Variables
    - Rules
    - Wildcards
- ... but becomes quickly [very hard to read](https://www.gnu.org/software/make/manual/html_node/Automatic-Variables.html).
- Not covered because CMake does this for us.
- But nicely documented in [py-RSE chapter 9](https://merely-useful.tech/py-rse/automate.html).

---

## Summary

- Make is an important build system by itself and an important building block for CMake.
- Make works by checking timestamps and updating outdated files if necessary.
- Each file can be a target. A target has dependencies and an update rule.
- `make target` updates "target", just `make` updates first target.
- Phony targets are empty (helper) targets, not files.
- Always define the standard phony targets `all` and `clean`.

---

## Further Reading

- [GNU Make manual](https://www.gnu.org/software/make/manual/html_node/index.html)
