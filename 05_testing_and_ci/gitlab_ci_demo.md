# Demo: GitLab Runner

Test code in [automation lecture repository](https://gitlab-sim.informatik.uni-stuttgart.de/simulation-software-engineering-wite2425/lecture-automation) on our GitLab instance

## Inspect Repository

- Same code as for GitHub Actions, but now `gitlab-ci.yml` instead of `.github/workflows/...`
- Look at `gitlab-ci.yml`:
    - Does the same things as GitHub actions
    - Runs on a Docker image `ajaust/automation-lecture`
- Self-hosted GitLab instance: where should the CI run?
- Click on CI symbol of latest commit: pipeline is stuck
- Click on job: "doesn't have any runners"
- Edit in pipeline editor -> Visualize
- Settings -> CI/CD -> Runners -> Specific runners
    - URL and Token; we will need this in a minute
    - Select `Run untagged jobs` (optional, but can make things simpler for now)

## Inspect bwCloud

- bwCloud: many services academia in BW can use; e.g. VMs
- Go to dashboard: https://portal.bw-cloud.org/ and login with Uni Stuttgart account
- I have already set up a VM. What I did:
    - Add public SSH key
    - Instances -> Launch instance
        - Ubuntu 24.04
        - Flavor: m1.small
    - `sudo apt update && sudo apt -y upgrade`
    - `sudo apt install -y docker.io`
- VM is up and running, connect to it: `ssh ubuntu@<IP>`

You can get the IP from the [Instances view](https://portal.bw-cloud.org/project/instances/). Note that there are two addresses here: an IPv4 (decimal) and an IPv6 (hexadecimal) address. New VMs on bwCloud only support IPv6 networks, so you need the second address.

## Setup GitLab Runner

- Install GitLab Runner via Docker:

  ```bash
  sudo docker run -d --name gitlab-runner --restart always \
           --network host \
           -v /srv/gitlab-runner/config:/etc/gitlab-runner \
           -v /var/run/docker.sock:/var/run/docker.sock \
           gitlab/gitlab-runner:latest
  ```

    - `docker run -d --name gitlab-runner --restart always` runs the container in the background (`-d` means detached) names it `gitlab-runner` and makes sure that it always runs. The container is automatically restarted once it stops/crashes. If you want to stop the container, you have to stop it manually (`docker container stop`).
    - `--network host` tells Docker to use the host network stack and is needed on bwCloud VMs, which only support IPv6.
    - `-v /srv/gitlab-runner/config:/etc/gitlab-runner` mounts the directory `/srv/gitlab-runner/config` into the container.
    - `-v /var/run/docker.sock:/var/run/docker.sock` mounts important Docker files into the container such that the container can start other containers (for pipelines).
    - `gitlab/gitlab-runner:latest` is the GitLab Runner image used from Docker Hub.
    - Summary: We start a manager Docker container (called runner) that will handle the jobs

- More information:
    - [installation instructions](https://docs.gitlab.com/runner/install/)
    - And more specific [Run GitLab Runner in a container](https://docs.gitlab.com/runner/install/docker.html)

## Register Runner

You can register a runner using the following command. Notice again the `--network host` option, which tells Docker to use the host network stack. This is an important workaround for the fact that bwCloud only supports IPv6 networks:

```bash
sudo docker run --rm -it \
         --network host \
         -v /srv/gitlab-runner/config:/etc/gitlab-runner \
         gitlab/gitlab-runner register \
         --url https://gitlab-sim.informatik.uni-stuttgart.de/
```

- Enter the following details: 
    - URL: (press Enter to confirm)
    - Token: see above
    - Description: `SSE Automation Demo Runner`
    - No tags, no maintenance note
    - Executor: `docker`
    - Default Docker image: `alpine:latest` (used for pipelines that do not specify any Docker image themselves, can be overwritten in configuration of pipeline)
- `sudo vi /srv/gitlab-runner/config/config.toml`
- Verify that there is now a runner in the repo settings
- Verify that pipeline now ran

- More information:
    - [Executors and their abilities](https://docs.gitlab.com/runner/executors/)
    - [Registering runners](https://docs.gitlab.com/runner/register/index.html#docker).
