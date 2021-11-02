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

# Singularity

- Back story
  - Created at Lawrence Berkeley National Laboratory but now developed by SyLabs
  - Based on Go
- Container solution with high-performance computing in mind
  - "Mobility of compute", "Bring your own environment"
    - Mobility of your compute environment
    - Normally immutable images
  - Integration in scheduling systems
  - Runs in *user-space* (no root privilege escalation)
  - Direct network and (some) hardware access (GPUs, accelerators)
  - Mounts common/important directories
  - Images can be based on Docker images (**TODO** check this). This is nice to prebuild parts of the image as Docker image since Singularity's format is not layer based. This means you have to rebuilt from scratch if it fails.
  - Small runtime penalty.
- Nowadays available on many HPC platforms
- Show text-based file format. Is similar to Docker
- Common commands:
  - TODO