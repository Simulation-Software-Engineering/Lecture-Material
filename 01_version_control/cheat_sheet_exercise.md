# SSE Git Cheat Sheet – Instructions

## Prerequisites and Preparation

- Everybody needs a GitHub account.
- GitHub repo per group (6-10 students) with empty cheat sheet + license + everybody added as contributor.
- Team `Octocat` uses front rows, team `Tux` uses back rows. Fill only every second row such that we can walk by to help.

## Introduction

Let's create our own SSE Git cheat sheets written in markdown. Obviously, there are many great Git cheat sheets out there. There is also the official manual. Our goal is not to make even better cheat sheets. Instead, our goal is to go through the process of how to get there: to learn how to work together as a team on GitHub and to maybe learn something new about Git on the way. Restrict the cheat sheet to the really important everyday Git commands. We want to have a usable cheat sheet in one hour. Make use of the [feature branch workflow](https://github.com/Simulation-Software-Engineering/Lecture-Material/blob/main/01_version_control/workflow_slides.md#Feature-Branch-Workflow) with forks.

## Tasks

1. Fork your Git cheat sheet repository, [Octocat](https://github.com/Simulation-Software-Engineering/Git-Cheat-Sheet-Octocat) or [Tux](https://github.com/Simulation-Software-Engineering/Git-Cheat-Sheet-Tux).
2. Create issues (in the upstream repository) on what you think the group should work on. Examples: "Define categories" or "Add `git pull and push`". Look for and avoid duplicates. Assign an issue to yourself if you want to work on it. If necessary, use the issue to discuss details. Don't open too many issues right away. If necessary, discuss with your group, but the main conversations should happen on GitHub.
3. If you think you have a good first extension of the cheat sheet, open a PR from a feature branch on your fork to the upstream `main` branch. Keep PRs concise, such that they are easy to review and quick to merge. Briefly describe the rationale of the PR. Assign yourself to the PR. You are responsible for the life cycle of the PR.
4. Find at least one reviewer for your PR (by asking around offline). Assign the review of the PR to them.
5. Review other PRs. Give constructive feedback on how to improve and / or use the suggestion feature of GitHub. Avoid endless discussions, better open additional issues if something goes beyond current PRs.
6. Regularly rebase your PR on `main` (force push to your feature branch if necessary). Avoid merge commits. Ideally, we get a perfectly readable (linear) history in the end.
7. Merge the PR if you have at least one *approving* review and no *changes requested*. Squash if necessary to get meaningful commits. Add reviewers as co-authors (`Co-authored-by: name <name@example.com>` in commit message) if they contributed.
8. Start at step 2 or step 5 again.

## Bonus

- Create a GitHub project to manage and oversee the overall progress.
- Add a markdown lint configuration and a GitHub action to check whether your cheat sheet follows markdown standards. You could find some inspiration in [lecture material repo](https://github.com/Simulation-Software-Engineering/Lecture-Material).
- Discuss and add categories to issues and PRs.
- Extend the readme file and add a contributors list there.
- Add a `CONTIRBUTING.md`.
- Push your fork also to a (private) GitLab repository.
- Be creative.

## Minimal Requirement

To pass, everybody should at least ...

- Open and merge one PR
- Give one review

## Discussion

At least 10 minutes in the end:

- How did it work?
- Where were problems?
- What was over-engineered? Which part of the workflow turned out to be actually helpful?
- What did you learn? Any other trick you want to share?

## Final remarks

If you want, continue with the Git cheat sheet after the exercise or do similar ones during other chapters of the lecture (Docker, CMake, ...). Let us know if we should create repositories under the `SSE` organization.
