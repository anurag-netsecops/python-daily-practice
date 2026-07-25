# Day 08 Notes

## Concepts Learned

- Dictionaries
- Lists
- map() Function
- sum() Function
- len() Function
- String Formatting (f-strings)

---

## Solution Approach

1. Read the number of students.
2. Store each student's marks in a dictionary.
3. Read the student's name to search.
4. Calculate the average using:

```python
average = sum(student_marks[query_name]) / len(student_marks[query_name])
```

5. Print the result with two decimal places:

```python
print(f"{average:.2f}")
```

---

## Time Complexity

O(n)

where `n` is the number of students. Dictionary lookup is O(1).

---

## Space Complexity

O(n)

The dictionary stores all student records.

---

## Key Takeaway

This challenge demonstrates how dictionaries efficiently store and retrieve key-value pairs.

It also introduces formatted output using Python f-strings, which are widely used for displaying numerical results.

---

## Real-World Relevance

Dictionaries are commonly used in Python automation for:

- API response processing
- JSON data handling
- Configuration management
- Device inventory storage
- User and credential mapping
- Network automation scripts
