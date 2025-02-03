from collections import Counter

def most_frequent(lst):
    return Counter(lst).most_common(1)[0][0]

print(most_frequent([1, 3, 2, 3, 4, 3, 5]))  # Output: 3
