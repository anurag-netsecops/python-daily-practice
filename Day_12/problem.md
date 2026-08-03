# Day 12 - Lists

## Platform

HackerRank

## Problem Link

https://www.hackerrank.com/challenges/python-lists/problem?isFullScreen=true

## Difficulty

Easy

---

## Problem Statement

Initialize an empty list and process `N` commands.

The following commands can be performed:

1. `insert i e` - Insert integer `e` at position `i`.
2. `print` - Print the list.
3. `remove e` - Remove the first occurrence of `e`.
4. `append e` - Add `e` to the end of the list.
5. `sort` - Sort the list.
6. `pop` - Remove the last element.
7. `reverse` - Reverse the list.

Execute each command in the order it is provided.

---

## Example

### Input

```text
4
append 1
append 2
insert 1 3
print
```

### Output

```text
[1, 3, 2]
```

---

## Input Format

The first line contains an integer `N`, representing the number of commands.

The next `N` lines contain one command each.

## Output Format

For every `print` command, print the current list.
