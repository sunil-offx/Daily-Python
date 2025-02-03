import heapq

def kth_largest(nums, k):
    return heapq.nlargest(k, nums)[-1]

print(kth_largest([3, 2, 1, 5, 6, 4], 2))  # Output: 5
