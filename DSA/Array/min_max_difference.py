"""
Problem: Find the difference between the maximum and minimum element.
Difficulty: Easy

Time Complexity: O(n)
Space Complexity: O(1)
"""
def min_max_difference(arr):
    minimum = arr[0]
    maximum = arr[0]
    for num in arr:
        if num>maximum:
            maximum = num
        if num<minimum:
            minimum = num
    difference = maximum - minimum
    return difference
    
numbers = [7,4,7,8,2,5,3,1]
difference= min_max_difference(numbers)
print("The difference is: ", difference)