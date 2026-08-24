# Day 3 Mistake Log

## Week 1 --- Day 3: Python Lists

### 1. Forgot parentheses with `sort()`

**Mistake**

``` python
skills.sort
```

**Correct**

``` python
skills.sort()
```

**Lesson:** `skills.sort` refers to the method; `skills.sort()` executes
it. Remember `()` when calling methods.

### 2. Confusion about `pop()`

With:

``` python
removed = skills.pop()
print(removed)
```

only `FastAPI` was displayed, which made it look like the other items
were removed.

Actually:

``` text
removed → "FastAPI"
skills  → ["Python", "SQL", "Pandas"]
```

**Lesson:** `pop()` without an index removes and returns only the last
item. The terminal only shows values you explicitly print.

### 3. Used unpacking instead of indexing

``` python
print(*skills, sep="\n")
```

This is valid Python, but the exercise was intended to practice
indexing.

For indexing practice:

``` python
print(skills[0])
print(skills[1])
print(skills[-1])
print(skills[-2])
```

**Lesson:** During exercises, use the concept being practiced even when
another valid solution exists.

### 4. Mixed up f-string syntax

**Mistake**

``` python
print{/f"employee_names[0]"}
```

**Correct**

``` python
print(f"First employee: {employee_names[0]}")
```

**Memory rule:** `print(f"Text {expression}")`

### 5. Forgot the closing quote in an f-string

**Mistake**

``` python
print(f"First two employees: {employee_names[:2]})
```

**Correct**

``` python
print(f"First two employees: {employee_names[:2]}")
```

### 6. Left an empty f-string expression

**Mistake**

``` python
print(f"Average Salary: {}")
```

**Correct**

``` python
print(f"Average Salary: {sum(salaries) / len(salaries)}")
```

**Lesson:** Put a value, variable, or calculation inside `{}`.

### 7. Swapped ascending and descending sorting

**Mistake**

``` python
ascending_order = sorted(salaries, reverse=True)
descending_order = sorted(salaries, reverse=False)
```

**Correct**

``` python
ascending_order = sorted(salaries, reverse=False)
descending_order = sorted(salaries, reverse=True)
```

Or:

``` python
ascending_order = sorted(salaries)
descending_order = sorted(salaries, reverse=True)
```

**Memory rule:** `reverse=False` means ascending; `reverse=True` means
descending.

### 8. `reverse()` is not descending sort

`reverse()` only flips the current order. It does not sort values.

``` python
scores.sort()
scores.reverse()
```

can produce descending order after sorting, while:

``` python
descending_scores = sorted(scores, reverse=True)
```

creates a descending result without modifying the original list.

### 9. Difference between `sort()` and `sorted()`

``` python
scores.sort()
```

changes the original list.

``` python
sorted_scores = sorted(scores)
```

returns a new sorted list and preserves the original.

## Day 3 Key Memory Rules

-   List indexing starts at `0`.
-   `skills[0]` is the first item; `skills[-1]` is the last.
-   Slicing uses `[start:stop]`; start is included and stop is excluded.
-   Lists are mutable.
-   `append()` adds to the end.
-   `insert()` adds at a position.
-   `remove()` removes by value.
-   `pop()` removes and returns an item.
-   `len()` counts items.
-   `min()` finds the smallest value.
-   `max()` finds the largest value.
-   `sum()` calculates the total.
-   Average = `sum(values) / len(values)`.
-   `sort()` modifies the original list.
-   `reverse()` flips the current order.
-   `sorted()` returns a new sorted list.
-   `reverse=False` means ascending.
-   `reverse=True` means descending.
-   f-string pattern: `f"Text {expression}"`

## Day 3 Final Challenge Concepts Practiced

Creating lists, positive and negative indexing, slicing, `len()`,
`min()`, `max()`, `sum()`, average calculation, `sort()`, `reverse()`,
`sorted()`, `reverse=True/False`, f-strings, and preserving original
data while creating sorted versions.
