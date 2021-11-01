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

# Containers

---

## What is a container

![A sketch of containers](container-sketch.png)

- Low(er) overhead than virtual machines.
- Container operates in "fenced off" part of the operating system (`cgroups`).
- Container runs kernel of the host OS.
- Operating system (OS) needs to be compatible with underlying OS. Cannot run different OS than host. (TODO: Verify this)