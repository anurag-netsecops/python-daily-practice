# Day 13 Notes

## Concepts Learned

- Functions
- Function Parameters
- Return Statement
- Strings
- f-Strings
- String Formatting

---

## Solution Approach

The function receives two parameters:

```python
first
last
```

We combine them into the required message using an f-string:

```python
return f"Hello {first} {last}! You just delved into python."
```

---

## Why use `return`?

The HackerRank code stub expects the function to return a string.

```python
return f"Hello {first} {last}! You just delved into python."
```

We should not use:

```python
print(...)
```

inside the function because HackerRank handles the output through the provided code.

---

## Time Complexity

O(n)

Where `n` represents the length of the resulting string.

## Space Complexity

O(n)

The formatted string requires memory proportional to its length.

---

## Key Takeaway

Functions allow us to create reusable pieces of code.

In this problem:

```python
def print_full_name(first, last):
```

`first` and `last` are function parameters, and the function returns a formatted string.

f-strings provide a clean and readable way to insert variables into strings.

---

## Real-World Relevance

String formatting is frequently used in:

- Network automation logs
- CLI output
- API messages
- Configuration generation
- Monitoring reports
- Automation scripts
