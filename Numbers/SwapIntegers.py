def swap_integers(a, b):
    a, b = b, a
    return a, b

# Example
x, y = 5, 10
x, y = swap_integers(x, y)
print(f"x: {x}, y: {y}") # Output: x: 10, y: 5