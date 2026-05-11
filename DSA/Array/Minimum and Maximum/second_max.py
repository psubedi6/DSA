"""
Problem: Find the second largest element in an array.
Difficulty: Easy

Time Complexity: O(n)
Space Complexity: O(1)
"""
#practice problem
def second_max(arr):
    maximum= float('-inf')
    second_maximum = float('-inf')
    for num in arr:
        if num > maximum:
            second_maximum = maximum
            maximum = num
        elif num > second_maximum and num != maximum:
            second_maximum = num
    return second_maximum

number= [1,5,3,53,7,8,2,4,9]
maximum = second_max(number)
print("Second Largest Number: ", maximum)