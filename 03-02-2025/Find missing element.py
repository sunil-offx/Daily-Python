def find_missing_number(lst):
    n = len(lst) + 1
    return (n * (n + 1) // 2) - sum(lst)

print(find_missing_number([1, 2, 4, 5, 6]))  # Output: 3
