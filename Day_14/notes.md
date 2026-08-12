# Day 14 Notes

## Concepts Learned

- Strings
- `split()`
- `join()`
- String Manipulation
- Function Return Values

---

## Solution Approach

First, split the string into individual words:

```python
line.split()
```

Example:

```python
"this is a string".split()
```

Result:

```python
["this", "is", "a", "string"]
```

Then join the words using `-`:

```python
"-".join(line.split())
```

Result:

```text
this-is-a-string
```

---

## Time Complexity

O(n)

Where `n` is the length of the input string.

## Space Complexity

O(n)

The split operation creates a collection of the words.

---

## Key Takeaway

`split()` and `join()` are two extremely useful Python string operations.

### split()

Converts a string into a list:

```python
"a b c".split()
```

Result:

```python
["a", "b", "c"]
```

### join()

Combines elements into a string:

```python
"-".join(["a", "b", "c"])
```

Result:

```text
a-b-c
```

---

## Real-World Relevance

String processing is frequently used in:

- Network device CLI output parsing
- Log processing
- Configuration generation
- CSV/text file processing
- API data transformation
- Network automation scripts
