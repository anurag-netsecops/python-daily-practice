# Day 11 Notes

## Concepts Learned

- Python Lists
- `set()`
- `sort()`
- Duplicate Removal
- Descending Sorting
- List Indexing
- `map()`

---

## Solution Approach

### Step 1: Read the scores

```python
arr = list(map(int, input().split()))
```

### Step 2: Remove duplicates

```python
unique_scores = list(set(arr))
```

This is important because the highest score may appear multiple times.

Example:

```text
[2, 3, 6, 6, 5]
```

becomes:

```text
[2, 3, 5, 6]
```

### Step 3: Sort in descending order

```python
unique_scores.sort(reverse=True)
```

Result:

```text
[6, 5, 3, 2]
```

### Step 4: Find the runner-up

```python
print(unique_scores[1])
```

Index `0` contains the highest score.

Index `1` contains the second-highest score.

---

## Time Complexity

O(n log n)

Sorting the unique scores takes O(n log n) time in the worst case.

## Space Complexity

O(n)

Additional space is used to store the unique scores.

---

## Key Takeaway

When finding the second-highest **unique** value, duplicate maximum values must first be removed.

Python's `set()` provides a simple way to remove duplicates.

---

## Real-World Relevance

The same pattern can be useful in automation for:

- Finding second-highest interface utilization
- Ranking device performance
- Processing monitoring metrics
- Removing duplicate API results
- Analyzing network statistics
