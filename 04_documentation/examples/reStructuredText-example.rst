==================
Top-level headline
==================

Overlining is optional. One can use other characters for the headline marking such as ``-`` or ``*``. There is no strict hierarchy of these characters defined to mark sections, subsections etc. The actual hierarchy is determined by the order of headings. However, the Python style guide proposes ``#`` > ``*`` > ``=`` and so on with each character referring to a certain type of structure (part, chapter, section...)

More information can be found in the `Python documentation style guide <https://devguide.python.org/documenting/#sections>`_

-------------------------------
This is the second-level header
-------------------------------

Hello there.

*This text is emphasized (italics)*

**This text is heavily emphasized (bold)**

``This is monofont text``

We can also have nice lists

* Item 1
* Item 2

which can be numbered as well

1. Item 1
2. Item 2

   1. Item 2a
   2. Item 2b

As one can see we can also have sublists. In contrast to markdown there has to be a line break before the sublist starts.

Code uses backticks. This can be code/variable names in text that ``appear`` in a monospace font. Code blocks start and end with triple backticks and often take a specifier of the presented language.

.. code-block:: c++

    int main()
    {
        return 0;
    }

.. Quotations can be done by two dots

We can also have hyperlinks to other websites. We could link to the `course website`_, but separate the link and target definition.

.. _course website: https://simulation-software-engineering.github.io/homepage

------
Tables
------

There is two ways to create tables. The more powerful way uses grid tables:

+----------+----------+
| Column A | Column B |
+==========+==========+
| Value A  | Value  B |
+----------+----------+

Tables the simple way

========== ==========
 Column A   Column B
========== ==========
 Value A    Value B
 Value C    Value D
========== ==========

