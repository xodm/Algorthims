#An array is said to be monotonic
#if it is either entirely non-increasing or non-decreasing.
#Your task is to determine whether a given array is monotonic.
#That means the array is either sorted in increasing order 
#or decreasing order, or all the elements are equal.


def is_monotonic(arr):
    decreasing = increasing = True
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            increasing = False
        if arr[i] < arr[i+1]:
            decreasing = False
    return decreasing or increasing

arr = [1, 2, 2, 3]
print(is_monotonic(arr)) 
arr = [6, 5, 4, 4]
print(is_monotonic(arr))
arr = [1, 3, 2]
print(is_monotonic(arr))

#python MasteringTheArtOfProblemSolving/ArrayAlgorithims/IsMontonic.py
