Title: Python Tips: List Comprehensions
Date: 2026-01-12 14:30
Category: Code
Tags: python, programming, tips
Slug: python-tips-list-comprehensions
Summary: A quick look at one of Python's most beloved features.

# Pythonic Lists

List comprehensions are a concise way to create lists. Common applications are to make new lists where each element is the result of some operations applied to each member of another sequence.

## The Old Way

Here's how you might square numbers in a loop:

```python
squares = []
for x in range(10):
    squares.append(x**2)

print(squares)
```

## The Pythonic Way

And here is the same logic, but cleaner:

```python
squares = [x**2 for x in range(10)]
print(squares)
```

### Filtering

You can also add conditions!

```python
# Get even numbers only
evens = [x for x in range(20) if x % 2 == 0]
```
Happy coding!
