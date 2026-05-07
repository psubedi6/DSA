"""
Problem: Find the minimum element in an array.
Difficulty: Easy

Time Complexity: O(n)
Space Complexity: O(1)
"""
def find_minimum(arr):
    minimum = arr[0]
    for num in arr:
        if num < minimum:
            minimum = i
    return minimum
numbers = [23,3,6,8,3,8,9,5,5,4]
minimum = find_minimum(numbers)
print("Minimum: ", minimum)