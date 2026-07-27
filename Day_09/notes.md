# Day 09 Notes

## Concepts Learned

- Nested Lists
- Lists
- Sets
- Sorting
- List Comprehensions
- Filtering Data

---

## Solution Approach

### Step 1

Store every student's record in a nested list.

```python
students.append([name, score])
```

---

### Step 2

Extract all unique scores.

```python
scores = sorted(set(student[1] for student in students))
```

---

### Step 3

Find the second lowest score.

```python
second_lowest = scores[1]
```

---

### Step 4

Filter all students having that score.

```python
student[1] == second_lowest
```

---

### Step 5

Sort their names alphabetically.

```python
sorted(...)
```

---

## Time Complexity

O(n log n)

Sorting dominates the overall complexity.

---

## Space Complexity

O(n)

Stores student records and unique scores.

---

## Key Takeaway

This challenge combines several important Python concepts:

- Nested lists
- Removing duplicates using `set()`
- Sorting using `sorted()`
- Filtering with list comprehensions
- Working with structured data

These concepts are frequently used together in real-world Python applications.

---

## Real-World Relevance

Nested lists and sorting are commonly used in:

- Parsing CSV files
- Processing API responses
- Network device inventories
- Log analysis
- Report generation
- Automation scripts
