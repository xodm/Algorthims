def find_equilibrium_index(arr):
    #The sum() function returns a number, 
    #the sum of all items in an iterable.
    #sum(iterable, initialSum)
    totalsum = sum(arr);
    leftSum = 0;
    #enumerate adds a index to each iterable item.
    for i, num in enumerate(arr):
        rightSum = totalsum - leftSum - num
        if leftSum == rightSum:
            return i
        leftSum += num
    return -1
print(find_equilibrium_index([2, 3, -1, 5]))

#Runs in O(n) and is the most efficient
#since we have to go thru each element to find sum

#python MasteringTheArtOfProblemSolving/ArrayAlgorithims/EquilibriumIndexInArray.py
