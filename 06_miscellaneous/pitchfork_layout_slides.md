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

# Repository Layouts

---

## Introduction

- Structure of repository important
    - Makes navigation easier
    - Clear where to put new files
- No "best" standard

---

## Project/Repository Layout

- C and C++
    - [Pitchfork](https://github.com/vector-of-bool/pitchfork)
- Python:
    - [The Hitchiker's Guide to Python](https://docs.python-guide.org/writing/structure/)
        - Layout also depends on frameworks used
- There are more

---

## Pitchfork (Layout)

- Originated from [Reddit](https://www.reddit.com/r/cpp/comments/996q8o/prepare_thy_pitchforks_a_de_facto_standard/): "Prepare thy Pitchforks: A (de facto) Standard Project Layout"
- [GitHub repo](https://github.com/vector-of-bool/pitchfork) includes conventions and useful tools

```text
README
LICENSE
build/
src/
include/  (optional)
tests/
examples/
external/
extras/
data/
tools/
docs/
libs/
```

---

## The Hitchiker's Guide to Python

- Based on [K. Reitz's recommendation](https://kennethreitz.org/essays/2013/01/27/repository-structure-and-python)

```text
README.rst
LICENSE
setup.py
requirements.txt
sample/__init__.py
sample/core.py
sample/helpers.py
docs/conf.py
docs/index.rst
tests/test_basic.py
tests/test_advanced.py
```

---

## Remarks/Tips

- Define a structure and stick to it
- Use short, but meaningful names
- As few files in root of respository as possible
- Projects might define own structure
    - Example: [DUNE/DuMuX](https://tu-dresden.de/mn/math/numerik/sander/ressourcen/dateien/sander-getting-started-with-dune-2-7.pdf?lang=en)

---

## Further Reading

- [Pitchfork GitHub repository](https://github.com/vector-of-bool/pitchfork)
- [Pitchfork project layout conventions](https://api.csswg.org/bikeshed/?force=1&url=https://raw.githubusercontent.com/vector-of-bool/pitchfork/develop/data/spec.bs)
- [The Hitchiker's Guide to Python](https://docs.python-guide.org/writing/structure/)