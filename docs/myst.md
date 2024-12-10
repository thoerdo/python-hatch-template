# MySt Markdown

## Horizontal line

Some text, followed by a line.

---

## Lists

### Ordered lists

1. First item
2. Second item
    1. First sub-item

1. First item
2. Second item
    * First sub-item

### Unordered lists

* First item
* Second item
  * First subitem

* First item
  1. First subitem
  2. Second subitem

## Tables

```md
| left | center | right |
| :--- | :----: | ----: |
| a    | b      | c     |
```

| left | center | right |
| :--- | :----: | ----: |
| a    | b      | c     |
| d    | e      | g     |
| f    | h      | i     |

```{list-table} This table title
:header-rows: 1
:name: example-table

* - Training
  - Validation
* - 0
  - 5
* - 13720
  - 2744
```

%{numref}`example-table` is an example.
This {ref}`table <example-table>` is an example.

## Footnotes

* This is a manually-numbered footnote reference.[^3]
* This is an auto-numbered footnote reference.[^myref]
* A longer footnote definition.[^mylongdef]

    [^mylongdef]: This is the _**footnote definition**_.

        That continues for all indented lines

        - even other block elements

        Plus any preceding unindented lines,
    that are not separated by a blank line

This is not part of the footnote.

[^myref]: This is an auto-numbered footnote definition.
[^3]: This is a manually-numbered footnote definition.
