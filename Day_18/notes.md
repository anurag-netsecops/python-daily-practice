# Day 18 Notes

## Concepts Learned

- String Methods
- `swapcase()`
- Functions
- Return Values
- String Transformation

---

## Solution Approach

Python provides a built-in method called:

```python
swapcase()
```

It automatically swaps the case of alphabetic characters.

Example:

```python
text = "Hello World"
print(text.swapcase())
```

Output:

```text
hELLO wORLD
```

---

## Important Point

`swapcase()` does not modify the original string because Python strings are immutable.

Instead, it returns a new string.

```python
result = s.swapcase()
```

---

## Time Complexity

O(n)

Each character in the string needs to be processed.

## Space Complexity

O(n)

A new string is created because strings are immutable.

---

## Key Takeaway

Python provides many built-in string methods that simplify common text-processing tasks.

Instead of manually checking every character, `swapcase()` provides a clean and readable solution.

---

## Real-World Relevance

String transformation is useful in:

- CLI output processing
- Log processing
- Text normalization
- Configuration processing
- Data transformation
- Automation scripts
