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

## Workarounds for IPv6

New bwCloud VMs only support IPv6 by default. Asking for IPv4 for a specific VM might be possible via the [helpdesk](https://bw-cloud.org/q/t).

A few workarounds are needed to make the GitLab runner work in this IPv6-only environment, especially since [`registry.gitlab.com` does not support IPv6](https://gitlab.com/gitlab-com/gl-infra/production-engineering/-/issues/18058) and the Docker support for IPv6 needs to be expliticly configured.

First, we need to tell Docker to use the host network and DNS. We also need to replace the helper image with [the one from Docker Hub](https://hub.docker.com/r/gitlab/gitlab-runner-helper/tags?name=x86_64-v17.10.1). Edit the `[runners.docker]` section in `/srv/gitlab-runner/config/config.toml`:

```toml
  volumes = ["/etc/resolv.conf:/etc/resolv.conf:ro", "/srv/gitlab-runner/custom-hosts:/etc/hosts:ro", "/cache"]
  helper_image = "gitlab/gitlab-runner-helper:x86_64-v17.10.1"
  network_mode = "host"
```

While you could pass `--network host` to `docker run`, setting this system-wide makes it easier to also start the job containers with the same settings.

Whenever changing this configuration file, we need to restart the runner (e.g., by restarting the respective container).

We also need to hard-code the IPv6 address that corresponds to the GitLab instance domain. Add the following line in the `/srv/gitlab-runner/custom-hosts`:

```
2001:7c0:2015:216::19 gitlab-sim.informatik.uni-stuttgart.de
```

You can get this address by running `dig aaaa gitlab-sim.informatik.uni-stuttgart.de`.

## Setup GitLab Runner

- Install GitLab Runner via Docker:

  ```bash
  sudo docker run -d --name gitlab-runner --restart always \
           -v /srv/gitlab-runner/config:/etc/gitlab-runner \
           -v /var/run/docker.sock:/var/run/docker.sock \
           gitlab/gitlab-runner:latest
  ```

    - `docker run -d --name gitlab-runner --restart always` runs the container in the background (`-d` means detached) names it `gitlab-runner` and makes sure that it always runs. The container is automatically restarted once it stops/crashes. If you want to stop the container, you have to stop it manually (`docker container stop`).
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
