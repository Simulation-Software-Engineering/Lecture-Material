# Automating Workflows with GitHub Actions

In this exercise, we create automated workflows and pipelines based on GitHub Actions. We are again working with our beloved diffusion Python code.

Deadline: **Thursday, February 2nd, 2023, 09:00**

## Preparations

Import the [automation exercise repository](https://github.com/Simulation-Software-Engineering/automation-exercise) in your own account/namespace on GitHub and name it `automation-exercise` again. **Note**: We cannot work with forks here because GitHub Actions may not work in pull requests without explicit approval of the owner of the target repository

## Task descriptions

The CI workflow should be triggered by `push` events and should have three jobs:

1. Name: `style_check`. Check the code style of the Python files in the repository using [`black`](https://github.com/psf/black). This check should fail if `black` finds any file to reformat.
2. Name: `test`. Run tests while also collecting coverage information via `pytest` and the `coverage` package. The coverage information (stored in the file `.coverage`) has to be stored and handed over to the next step.
    - The intermediate coverage information (`.coverage`) should be kept for one day. This is the minimum amount of time an artifact must be stored.
    - Adding a `.gitignore` file helps to not accidentally commit the temporary coverage files.
3. Name: `coverage_report`. Create a coverage report (`coverage report`) in the terminal and afterwards also convert the coverage information into XML format (`coverage xml`). For this you have to reuse the coverage information (i.e. `.coverage`) from the previous step.
    - Running `coverage report` allows us to inspect the coverage directly in the workflow's output. Saving the XML file allows us to analyze the coverage in more detail with other tools if needed.
    - The resulting file `coverage.xml` should be kept for 14 days.

Once the workflow runs successfully, add a [GitHub workflow status badge](https://docs.github.com/en/actions/monitoring-and-troubleshooting-workflows/adding-a-workflow-status-badge) for your workflow to the `README.md`. Label this badge with "SSE CI/CD".

## Submission

- Submit your solution via an issue in the *upstream* [automation exercise repository](https://github.com/Simulation-Software-Engineering/automation-exercise). The issue should be named `[USERNAME] Automation exercise`, e.g., `[uekermbn] Automation exercise`. Please use your GitLab username here. Add a link to your GitHub repository in the issue. If necessary, add further explanations in the issue description.

## Bonus: GitLab CI/CD

Realize the same workflows in GitLab CI/CD :)

- Create a new project under your namespace and push your existing automation repository to this remote.
- Create a VM on [bwCloud](https://www.bw-cloud.org/) and create a GitLab Runner with a Docker executor there. Register the runner in your repository.
- Add a link to this repository in the submission issue above and, if necessary, explain what you did. Be sure that your repository is visible to us (either public or add `uekermbn`).
