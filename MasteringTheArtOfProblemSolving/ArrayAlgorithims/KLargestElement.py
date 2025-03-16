#The task is to find the Kth largest element in an unsorted array.
#The Kth largest element means the element that would 
#be at position K if the array were sorted in descending order.
#There are several approaches to solve this, such 
#as sorting the array or using a min-heap.

def kth_largest(arr, k):
    sortarr= sorted(arr)
    return sortarr[len(arr)-k]

arr = [3, 2, 1, 5, 6, 4]
k = 2
print(kth_largest(arr, k))# Output: 5

#python MasteringTheArtOfProblemSolving/ArrayAlgorithims/KLargestElement.py
