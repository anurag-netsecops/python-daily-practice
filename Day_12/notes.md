# Day 12 Notes

## Concepts Learned

- Python Lists
- `append()`
- `insert()`
- `remove()`
- `sort()`
- `pop()`
- `reverse()`
- `split()`
- Conditional Statements
- Command Processing

---

## Solution Approach

### 1. Create an empty list

```python
my_list = []
```

### 2. Read each command

```python
command = input().split()
```

For example:

```text
insert 1 5
```

becomes:

```python
["insert", "1", "5"]
```

This allows us to identify the operation using:

```python
command[0]
```

### 3. Execute the appropriate operation

For example:

```python
if command[0] == "append":
    my_list.append(int(command[1]))
```

For an insert operation:

```python
if command[0] == "insert":
    my_list.insert(int(command[1]), int(command[2]))
```

---

## Important List Methods

| Method | Purpose |
|---|---|
| `append(x)` | Add an item to the end |
| `insert(i, x)` | Insert an item at an index |
| `remove(x)` | Remove the first occurrence |
| `sort()` | Sort the list |
| `pop()` | Remove the last item |
| `reverse()` | Reverse the list |

---

## Key Takeaway

The main learning from this challenge is not only list manipulation but also **dynamic command processing**.

Instead of knowing the operation beforehand, the program:

1. Reads a command.
2. Splits it into components.
3. Identifies the requested operation.
4. Executes the corresponding list method.

This pattern is useful when building CLI-based automation tools.

---

## Real-World Relevance

A similar command-processing approach can be used in Network Automation for commands such as:

```text
add_router R1
remove_router R2
show_devices
sort_devices
```

The automation script can read the requested action and execute the corresponding operation.
