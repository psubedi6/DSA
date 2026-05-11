"""
Problem: Find the largest negative number in an array.
Difficulty: Easy

Time Complexity: O(n)
Space Complexity: O(1)
"""
def largest_negative_number(arr):
    largest_negative= float("-inf")
    for num in arr:
        if num > largest_negative:
            largest_negative=num
    return largest_negative

number = [-3,-5,-7,-1,-6]
largest_negative = largest_negative_number(number)
print("Largest negative number: ", largest_negative)