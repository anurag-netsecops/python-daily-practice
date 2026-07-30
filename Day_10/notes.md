# Day 10 Notes

## Concepts Learned

- Tuples
- Immutable Data Structures
- map() Function
- tuple() Constructor
- hash() Function

---

## Solution Approach

1. Read the integer `n`.
2. Read the list of integers.
3. Convert the list into a tuple.
4. Print the hash value of the tuple.

```python
t = tuple(integer_list)
print(hash(t))
```

---

## Time Complexity

O(n)

Creating the tuple requires iterating through all elements once.

---

## Space Complexity

O(n)

The tuple stores `n` integers.

---

## Key Takeaway

A tuple is an **immutable** sequence in Python, meaning its elements cannot be modified after creation.

The `hash()` function returns a unique hash value for immutable objects like tuples, allowing them to be used as dictionary keys or set elements.

---

## Real-World Relevance

Tuples are commonly used in Python for:

- Storing immutable configuration values
- Dictionary keys
- Returning multiple values from functions
- Representing fixed data records
- Network automation scripts where configuration data should remain unchanged
