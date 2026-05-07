"""
Problem: Find Maximum and Minimum
Difficulty: Easy

Time Complexity: O(n)
Space Complexity: O(1)
"""

def find_max_min(arr):
    maximum = arr[0]
    minimum = arr[0]
    for num in arr:
        if num > maximum:
            maximum = num
        if num < minimum:
            minimum = num
    return maximum, minimum

numbers = [4, 2, 9, 1, 7]
maximum, minimum = find_max_min(numbers)
print("Maximum:", maximum)
print("Minimum:", minimum)