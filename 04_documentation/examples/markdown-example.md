# This is the top level header

If you follow some (?) standard strictly, the top level header should be the very first line in a markdown file.

## You can write text

Hello there.
*This text is emphasized (italics)*
**This text is heavily emphasized (bold)**

We can also have nice lists

- Item 1
- Item 2

which can be numbered as well

1. Item 1
2. Item 2
    1. Item 2a
    2. Item 2b

As one can see we can also have sublists.

Code uses backticks. This can be code/variable names in text that `appear` in a monospace font. Code blocks start and end with triple backticks and often take a specifier of the presented language.

```c++
int main()
{
    return 0;
}
```

One could also define code blocks with by indentation (usually 4 spaces), but it is better to not mix styles.

> Quotations can be done by angle brackets

We can also have hyperlinks to other websites. We could link to the [course website](https://simulation-software-engineering.github.io/homepage/) within the text, but separate [the link][course-website] in the text from the target definition. You find the target definition at the bottom of the Markdown file.

## This is a subheader

We can have nice tables

| Column A | Column B |
| -------- | -------- |
| Value A  | Value  B |

[course-website]: https://simulation-software-engineering.github.io/homepage/