"""
Problem: Find the smallest negative number in an array.
Difficulty: Easy

Time Complexity: O(n)
Space Complexity: O(1)
"""
def smallest_negative_number(arr):
    smallest_negative= float("inf")
    for num in arr:
        if num < smallest_negative:
            smallest_negative = num
    return smallest_negative

numbers = [-3,-5,-7,-1,-6]
smallest_negative= smallest_negative_number(numbers)
print("smallest negative number is: ", smallest_negative)