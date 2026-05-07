##Find the second smallest element in an array.
def second_minimum(arr):
    minimum = float('inf')
    second_minimum = float('inf')
    for num in arr:
        if num < minimum:
            second_minimum = minimum
            minimum = num
        elif num < second_minimum and num != minimum:
            second_minimum = num
    return second_minimum
    
numbers= [1,6,7,4,3,4]
minimum= second_minimum(numbers)
print("Second smallest number: ", minimum)