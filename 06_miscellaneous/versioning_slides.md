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

# Versioning

---

## Introduction

- Software version may indicate
    - Currentness/"Freshness"
    - (In)compatibility
    - Significance of changes
- Easy-to-understand label that something changed
- Important for packaging and reproducibility

---

## Versioning Examples

- Semantic versioning
    - [Linux Kernel](https://kernel.org/): 5.16.5 (Release), 5.17-rc2 (Preview)
- [PEP 440](https://www.python.org/dev/peps/pep-0440/)
    - [pyMOR](https://pymor.org/): 2022.2.0
- Calendar versioning
    - [Ubuntu](ubuntu.com/): 22.10 (Latest), 22.04 (LTS)
    - [OpenFOAM](https://www.openfoam.com/current-release) (`.com`): v2112
- Others
    - [TeX](https://tug.org/): 3.141592653 (Latest), 3.14159265 (Ubuntu 20.04)
    - [OpenFOAM](https://openfoam.org/release/) (`.org`): 10 (Latest), but "always releasable" (date patches, e.g. `20221128`)

---

## Versioning Standards

- [Semantic Versioning](https://semver.org/)
- [Calendar Versioning](https://calver.org/)
- [PEP 440](https://www.python.org/dev/peps/pep-0440/)

---

## Semantic Versioning

```text
MAJOR.MINOR.PATCH-<pre-release>+<build>
```

- `MAJOR` version when you make incompatible API changes,
- `MINOR` version when you add functionality in a backwards compatible manner, and
- `PATCH` version when you make backwards compatible bug fixes (no new functionality).

Homepage: [semver.org](https://semver.org)

---

## Semantic Versioning Examples

```text
MAJOR.MINOR.PATCH-<pre-release>+<build>
```

- `MAJOR`, `MINOR` and `PATCH` are numeric (mandatory)

  ```text
  0.0.1, 2.3.6, 5.0.1
  ```

    - Major `0`: often work-in-progress, any breaking changes possible

- `<pre-release>` dot-separated pre-release identifiers (optional)

  ```text
  1.0.0-alpha, 1.0.0-alpha.1, 1.0.0-0.3.7, 1.0.0-x.7.z.92
  ```

- `<build>` dot-separated build identifiers (optional)

  ```text
  1.0.0-alpha+001, 1.0.0+20130313144700, 1.0.0-beta+exp.sha.5114f85
  ```

- Implies ordering

  ```text
  1.0.0-alpha < 1.0.0 < 2.0.0 < 2.1.0 < 2.1.1
  ```

---

## Library Example

In my `/usr/local/lib/`:

```text
libprecice.so -> libprecice.so.2
libprecice.so.2 -> libprecice.so.2.5.0
libprecice.so.2.2.0
libprecice.so.2.5.0
```

- Two installed versions: `libprecice.so.2.2.0` and `libprecice.so.2.5.0`
- Symbolic links `libprecice.so` to a (often the newest) version of a library
- But we can also request a specific version, e.g. `libprecice.so.2.2.0`

---

## General Tips/Remarks

- Use a well-known versioning scheme
- Additionally if necessary: Define meaning of version jumps
    - Example DuMuX: backwards compatibility for at least two minor versions
- Do **not** modify released code

---

## Further Reading

- [Semantic versioning homepage](https://semver.org/)
- [PEP 440: Version Identification and Dependency Specification](https://www.python.org/dev/peps/pep-0440/)
- [Wikipedia: Software versioning](https://en.wikipedia.org/wiki/Software_versioning)
