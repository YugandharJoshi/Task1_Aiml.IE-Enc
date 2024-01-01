def compare(x, y, z):
    if x == y == z:
        return "All three values equal"
    elif x == y or y == z or x == z:
        return "Two values equal"
    else:
        return "All three values different"

v1 = 3
v2 = 4
v3 = 9

comparison_result = compare(v1, v2, v3)
print(f"Comparison result: {comparison_result}")