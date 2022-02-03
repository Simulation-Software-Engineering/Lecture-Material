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

# FLOSS Licenses

---

## Disclaimer

- IANAL: *I am not a lawyer.*
- Provided information "as-is", no warranty
- Things are simplified sometimes.

---

## Licenses are Complicated, Right?

- The details, yes
- The big picture, no
- Every RSE should know the big picture.

---

## Use Cases

- You want to pick a license for your (new) code.
- You use software of others and want to know what you are allowed to do.
- You contribute to an existing software and want to understand what this legally means.
- You want others to be able to use your software.

---

## Code Without a License

- Code is creative work and, thus, under **exclusive copyright by default**.
- Copyright owner is typically the creator (or their employer).
- Nobody else can copy / distribute / modify
- If code has more than one contributor, all contributors might become this *"nobody"*.
- **GitHub terms of service**:
    - Others can view and fork your repository.
    - Does not imply that they can use / modify / share your code.
- Still, you do not have to give a license.
    - Even though not necessary, putting a copyright notice in a prominent place helps clarifying in this case.

---

## Using a License

- A FLOSS license allows reuse of your code while retaining copyright.
- To choose or changing a license all copyright owners must agree (if not stated otherwise).

---

## Types of Licenses

... but there are sooo many licenses, they even have different versions. :scream:

Focus on big picture: There are mainly **three types**:

- Permissive licenses (not restrictive)
- Copyleft licenses (very restrictive)
- Intermediate licenses (complicated, will not cover here)

... and always choose the newest version of a license.

---

## Permissive Licenses

- In general, you can do what you want if you provide the original license and copyright notice with code.
    - Modifications might be done under different license
    - Can ship code as part of commercial software
- Examples: MIT, Apache, or BSD
- **MIT** is the way to go if you do not yet know where to go.
    - Short, easy to understand
    - Easy to change

---

## MIT License

... so simple, we can actually read and mostly understand it:

```
Copyright (c) [year] [fullname]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", ...
```

---

## Copyleft Licenses

- Main example is **GNU GPL**
- Two main restrictions:
    - (A) If you modify software and share it (e.g. sell binary), you need to publish the source code of the modification under the same license.
    - (B) If you use software in larger works (e.g. through interfaces or data structures), restriction (A) holds for larger works as well.
        - Example: DuMuX is GPLv3. Thus, if you publish a solver using DuMuX, it needs to be GPLv3 again.
- **GNU LGPL**: "L" stands for lesser (sometimes also for library)
    - Only restriction A, not B

---

## Creative Commons Licenses

- Not everything is code, CC licenses is specifically for creative work that is not code.

- The basis, plain **CC** or **CC0**: copyright waived, do what you want
- Restrictions are _"substracted"_:
    - **-BY**: attribution -> you need to credit original creation
    - **-SA**: share alike -> modifications need same license (similar to copyleft)
    - **-ND**: no derivatives -> you are not allowed to modify
    - **-NC**: non-commercial -> you cannot use in commercial context
- Combine as you want, e.g. **CC-BY-NC**

---

## Summary

- Though details are complicated, the big picture is easy
- And the big picture is important, every RSE should know
- Permissive licenses: do what you want, but credit creation (e.g. MIT)
- Copyleft licenses: modified work and derivatives need to get same license (e.g. GPL)

---

## Further Reading

- Many interesting resources and articles on [GNU licenses](https://www.gnu.org/licenses/)
- [GitHub: The Legal Side of Open Source](https://opensource.guide/legal/)
- [Software Licenses in Plain English](https://tldrlegal.com)
- [Choose a License](https://choosealicense.com/)
- [Creative Comments](https://creativecommons.org/licenses/)
- [Compatibility Checker](https://joinup.ec.europa.eu/collection/eupl/solution/joinup-licensing-assistant/jla-compatibility-checker)
