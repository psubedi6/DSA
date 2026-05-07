"""
Problem: Find the minimum element in an array.
Difficulty: Easy

Time Complexity: O(n)
Space Complexity: O(1)
"""
def minimum(arr):
    minimum = arr[0]
    for i in arr:
        if i < minimum:
            minimum = i
    return minimum
numbers = [23,3,6,8,3,8,9,5,5,4]
minimum = minimum(numbers)
print("Minimum: ", minimum)