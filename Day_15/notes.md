# Day 15 Notes

## Concepts Learned

- String Immutability
- String Slicing
- String Concatenation
- Function Parameters
- Return Statement

---

## Important Concept

Python strings are **immutable**.

This means we cannot directly change a character:

```python
string[5] = "k"
```

This produces an error.

Instead, we create a new string using slicing.

---

## Solution Approach

Suppose:

```python
string = "abracadabra"
position = 5
character = "k"
```

Take everything before the target position:

```python
string[:position]
```

Result:

```text
abrac
```

Take everything after the target position:

```python
string[position + 1:]
```

Result:

```text
dabra
```

Then combine them:

```python
string[:position] + character + string[position + 1:]
```

Result:

```text
abrackdabra
```

---

## Time Complexity

O(n)

A new string is created because strings are immutable.

## Space Complexity

O(n)

The modified string requires additional memory.

---

## Key Takeaway

When you need to modify a character in a Python string, use:

```python
string[:position] + character + string[position + 1:]
```

This pattern is useful whenever a specific character needs to be replaced.

---

## Real-World Relevance

String manipulation is commonly used in:

- Network CLI output processing
- Configuration generation
- Log parsing
- IP address and hostname processing
- API data transformation
- Automation scripts
