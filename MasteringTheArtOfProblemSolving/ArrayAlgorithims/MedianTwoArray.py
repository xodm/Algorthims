#The task is to find the median of two sorted arrays.
#The median is the middle element in a sorted list of numbers.
#If the total number of elements is even, the median is 
#the average of the two middle elements.
#The challenge is to solve this problem 
#efficiently in O(log(min(m,n))) time complexity.

def median(arr1, arr2):
    arr = sorted(arr1 + arr2)
    n = len(arr)
    if n % 2 == 0:
        return (arr[(n//2)-1] + arr[n//2])/2
    return arr[(n//2)]

nums1 = [1, 3, 4, 5, 6]
nums2 = [2]
print(median(nums1, nums2))


#python MasteringTheArtOfProblemSolving/ArrayAlgorithims/MedianTwoArray.py
