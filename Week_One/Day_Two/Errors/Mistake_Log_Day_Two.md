# Day 2 Mistake Log

## Week 1 --- Day 2: Python Strings

### 1. Forgot parentheses when calling `strip()`

**Mistake**

``` python
name = name.strip
```

**Correct**

``` python
name = name.strip()
```

**Lesson:** `strip` refers to the method; `strip()` executes the method.
This was also a repeated Day 1 mistake.

------------------------------------------------------------------------

### 2. Accessed an index outside the string

**Mistake**

``` python
language = "Python"
print(language[6])
```

**Error**

``` text
IndexError: string index out of range
```

**Lesson:** `"Python"` has 6 characters, but its valid positive indexes
are `0` through `5`. Python indexing starts at 0.

------------------------------------------------------------------------

### 3. Used `split()` without storing its returned value

**Mistake**

``` python
skills.split(",")
print(skills)
```

**Lesson:** `split()` returns a new value. It does not change the
original string.

**Correct**

``` python
result = skills.split(",")
```

------------------------------------------------------------------------

### 4. Assigned the original string instead of the result of `split()`

**Mistake**

``` python
skills.split(",")
result = skills
```

**Lesson:** `result = skills` copies the original string into `result`.
To store the split data, assign the method result directly.

**Correct**

``` python
result = skills.split(",")
```

------------------------------------------------------------------------

### 5. Forgot that values produced by `split()` are still strings

After:

``` python
employee = "Bhargav,AI Engineering,7,95000.50"
data = employee.split(",")
```

the values `"7"` and `"95000.50"` are still strings.

**Correct conversions**

``` python
data[2] = int(data[2])
data[3] = float(data[3])
```

**Lesson:** `split()` separates text but does not automatically convert
numeric-looking values to numbers.

------------------------------------------------------------------------

### 6. Used unnecessary `str()` conversion

**Mistake**

``` python
data[2] = str(data[2])
data[3] = str(data[3])
```

The values were already strings after `split()`.

**Lesson:** Convert data only when required by the operation you want to
perform.

------------------------------------------------------------------------

### 7. Mixed strings and integers during concatenation

**Mistake**

``` python
print("Experience next year:" + experience_next_year)
```

**Lesson:** `str + int` is invalid.

One solution:

``` python
print("Experience next year: " + str(experience_next_year))
```

Better Day 2 solution:

``` python
print(f"Experience next year: {experience_next_year}")
```

------------------------------------------------------------------------

### 8. Initial confusion with f-string text placement

**Mistake**

``` python
print(f"Experience next year: {data[2] + 1} "years")
```

**Correct**

``` python
print(f"Experience next year: {data[2] + 1} years")
```

**Lesson:** Normal text such as `years` can remain inside the same
f-string.

------------------------------------------------------------------------

### 9. Used the calculated future value with the current-value label

**Mistake**

``` python
print(f"Experience: {data[2] + 1}")
```

This printed `8` but labeled it as current experience.

**Correct idea**

``` python
print(f"Experience: {data[2]} years")
print(f"Experience next year: {data[2] + 1} years")
```

**Lesson:** Code can be syntactically correct but still have a
logic/meaning error.

------------------------------------------------------------------------

### 10. Hard-coded a result instead of calculating it

**Mistake**

``` python
print(f"Python skill count: {int(2)}")
```

This prints the correct-looking answer but does not actually count the
data.

**Correct**

``` python
print(f"Python skill count: {skills.count('Python')}")
```

**Lesson:** Let the program derive values from the input instead of
hard-coding expected results.

------------------------------------------------------------------------

### 11. Duplicate output lines during final challenge cleanup

`Employee` and `Department` were accidentally printed twice.

**Lesson:** After debugging, review the final output and remove
duplicate/debugging statements.

------------------------------------------------------------------------

## Day 2 Key Memory Rules

-   `method()` --- parentheses execute a method.
-   String indexing starts at `0`.
-   `[-1]` accesses the last character.
-   Slicing uses `[start:stop]`, and `stop` is excluded.
-   `split()` returns a new list; store the result.
-   Values returned from splitting text are strings until explicitly
    converted.
-   `find()` asks **where?** and returns `-1` when not found.
-   `count()` asks **how many?**
-   `startswith()` checks the beginning.
-   `endswith()` checks the ending.
-   f-string pattern: `f"Text {variable_or_expression} more text"`.
-   A program can run without errors and still contain a logic mistake.
