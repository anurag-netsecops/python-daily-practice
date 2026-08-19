# Day 19 Notes

## Concepts Learned

- Python Modules
- `textwrap`
- `textwrap.fill()`
- Function Parameters
- Return Values
- String Formatting

---

## Solution Approach

Python provides the built-in `textwrap` module for working with text wrapping.

First, import the module:

```python
import textwrap
```

Then use:

```python
textwrap.fill(string, max_width)
```

This wraps the string according to the specified width.

---

## Example

```python
import textwrap

text = "ABCDEFGHIJK"
result = textwrap.fill(text, 4)

print(result)
```

Output:

```text
ABCD
EFGH
IJK
```

---

## `fill()` vs `wrap()`

Python's `textwrap` module provides both:

```python
textwrap.wrap()
```

and:

```python
textwrap.fill()
```

`wrap()` returns a **list of lines**:

```python
["ABCD", "EFGH", "IJK"]
```

`fill()` returns a **single string with newline characters**:

```text
ABCD
EFGH
IJK
```

Since this HackerRank problem expects a string, `fill()` is convenient here.

---

## Time Complexity

O(n)

Where `n` is the length of the input string.

## Space Complexity

O(n)

The wrapped output requires additional memory.

---

## Key Takeaway

Python's standard library contains many useful modules that can solve common problems without reinventing functionality.

The `textwrap` module is useful when working with long text and fixed-width output.

---

## Real-World Relevance

Text wrapping and formatting can be useful in:

- CLI automation tools
- Network device reports
- Log formatting
- Terminal output
- Documentation generation
- Automation reports
