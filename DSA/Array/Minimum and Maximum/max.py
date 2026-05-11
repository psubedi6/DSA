"""
Problem: Find the maximum element in an array.
Difficulty: Easy

Time Complexity: O(n)
Space Complexity: O(1)
"""
#practice problem
def find_max(arr):
    maximum = arr[0]
    for num in arr:
        if num > maximum:
            maximum = num
    return maximum

number=[3,6,8,4,33,6,3,78,5,3]
maximum= find_max(number)
print("Maximum: ", maximum)