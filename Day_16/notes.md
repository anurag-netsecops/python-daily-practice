# Day 16 Notes

## Concepts Learned

- String Slicing
- String Indexing
- `len()`
- `range()`
- Substring Matching
- `for` Loops
- Function Return Values

---

## Solution Approach

First, determine the maximum valid starting position for the substring.

```python
range(len(string) - len(sub_string) + 1)
```

At every position, extract a substring using slicing:

```python
string[i:i + len(sub_string)]
```

Compare it with the target substring:

```python
if string[i:i + len(sub_string)] == sub_string:
```

If they match, increase the counter:

```python
count += 1
```

Finally, return the count.

---

## Example

For:

```text
string = ABABABA
sub_string = ABA
```

The loop checks:

```text
ABA
 BAB
  ABA
   BAB
    ABA
```

The substring `ABA` occurs 3 times.

---

## Time Complexity

O(n × m)

Where:

- `n` = length of the original string
- `m` = length of the substring

Each possible position is checked and a substring comparison is performed.

## Space Complexity

O(m)

The sliced substring requires additional memory.

---

## Key Takeaway

String slicing allows us to extract a portion of a string:

```python
string[start:end]
```

This is useful for checking whether a substring exists at a particular position.

---

## Real-World Relevance

Substring matching is useful in:

- Network log analysis
- CLI output parsing
- Searching configuration text
- Detecting error messages
- Filtering device output
- Processing API responses
