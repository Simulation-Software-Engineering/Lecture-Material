# Reviewing code

Let us get familiar with code review tools and practices.

Deadline: **December 17, 2025, 9:00**

**Note:** This is the first time that we have this exercise. Feedback and suggestions is very welcome - [open an issue](https://github.com/Simulation-Software-Engineering/Lecture-Material/issues).

## Overview

In this exercise, you will work responsibly with AI tools to write and review code.
More specifically, you will:

1. use [Responsible AI](https://rai.uni-stuttgart.de) to write a simulation program,
2. create a repository and publish the first implementation as a pull request to your main branch,
3. review the code as if it was written by another human,
4. use [GitHub copilot](https://docs.github.com/en/copilot) to conduct an automated review,
5. compare the two reviews to each other and to examples from your challenge project.

In the end, you will need to open an issue in the [exercise repository](https://github.com/Simulation-Software-Engineering/reviewing-exercise) with name `[username] Reviewing exercise submission`.

## Generate code

Generating code can be very useful to kick-start a project or to fill rather clear code parts (such as basic tests or documentation).
With the right prompts and some iterations, one can create functional programs.

**Important note:** Always check for mistakes and check everything you do not understand with the respective documentation.
You are entering dangerous territory: AI tools have particular strengths, but also weaknesses, and they will very often confidently give wrong answers (and code with bugs), which might not be immediately visibly wrong.
You remain in control and responsible for your projects.

Now that we have set some guidelines, let's see the strengths in action:

1. Login to the [Responsible AI](https://rai.uni-stuttgart.de) provided by the University of Stuttgart.
2. In your own words, ask the tool to generate code for solving a heat equation, in a programming language you understand (e.g., Python).
   Ask it to take parameters from a configuration file and write results to an output file.
   Ask for some documentation, tests, or anything else you would like to see in such a code.
3. Create a repository on GitHub (under your namespace) and initialize it with a `README.md` file.
4. Add the files that RAI created to the repository, in a branch called `feature`. In your commit message, clearly disclose the tool. For example:

   ```text
    I acknowledge the use of RAI (https://rai.uni-stuttgart.de/) to implement the entirety of this code.

    Promts:
    1. I would like a Python script that solves the heat equation.
    2. ...
   ```

   The more details you add, the better.

5. Open a merge request from the branch `feature` to the `main` branch.

## Review the code

Assume that this code was written by another human being. Be kind and thorough, and leave some comments in the pull request. Make sure to:

- Describe what you understand this PR does.
- Does the code run? Does it do the right thing?
- Mention what you like about it
- Add [inline comments and at least one inline code suggestion](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/reviewing-changes-in-pull-requests/commenting-on-a-pull-request)
- Question parts that do not make sense to you - ask for clarifications. Are the "why" and "how" clear?
- Could parts of the code be made simpler?
- Comment on individual aspects such as documentation, testing, design, corner cases, and potential bugs. See the [Google Reviewer Guidelines](https://google.github.io/eng-practices/review/reviewer/) for some ideas.

Your goal with any code review is to help the author improve the contribution to a state that can be accepted into the project.

Start an issue in the [exercise repository](https://github.com/Simulation-Software-Engineering/reviewing-exercise) and add a link to your repository and this PR. Give a summary: what did the AI tool do nicely, where did it fail?

## Get an automated review

GitHub Copilot can automatically review a pull request. Add it as a reviewer and wait for it to submit a review.

Carefully go through the review. Apply comments you agree with, comment on the points you don't agree with.

Optional: Give [custom instructions to Copilot](https://docs.github.com/en/copilot/tutorials/customization-library/custom-instructions) (such as [code reviewer](https://docs.github.com/en/copilot/tutorials/customization-library/custom-instructions/code-reviewer)).

In the issue you just opened, edit the description and comment:

- Comparing the two reviews, what did Copilot focus on, what did you focus on?
- What did you learn from the suggestions?

## Examples from your Challenge project

In the issue you just opened, edit the description and:

- Add 1-3 examples of pull/merge requests with extensive review.
- Comment: What do reviewers seem to typically focus on?
