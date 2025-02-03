from collections import Counter

def first_non_repeating(s):
    count = Counter(s)
    for char in s:
        if count[char] == 1:
            return char
    return None

print(first_non_repeating("swiss"))  # Output: "w"
