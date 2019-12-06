#use python3

# A simple solution that uses 2 loops, but as first loop increments, 
# Time complexity: O(n^2), Space complexity: O(1) 
# previous values are not checked to avoid double checking. Not optimal but works
def twoNumberSum_Loop(array, targetSum):
    output = []
    # check for empty array input
    if not array:
        return output

    # Loop from the first element of the array
    for i in range(len(array)-1):
        # Inner loop should always start from the item after i, this avoids unnecessary previous checks
        for j in range(i+1, len(array)):
            currentSum = array[i] + array[j]
            if currentSum == targetSum:
                output.append(array[i])
                output.append(array[j])
                output.sort(reverse=False)
                break
        if output:
            break

    return output

# More Optimal solution that uses hash tables. Time complexity: O(n), Space complexity: O(n) 
# The array is traversed only once and the hash table is checked to find current value plus value in hash table to equal target sum.
def twoNumberSum_hashTable(array, targetSum):
    # check for empty array input
    output = []
    if not array:
        return output
    hashTable = dict()
    for item in array:
        targetItem = targetSum - item
        if targetItem in hashTable:
            output.append(item)
            output.append(targetItem)
            output.sort()
            break
        else:
            hashTable.update({item: True})

    return output

# Another Optimal solution, no hash table is used and first sort the array
# Time complexity: O(nlog n) depending on sorting algorithm used, Space complexity: O(1)
# use left and right pointers, to traversed the array and move them left and right until the sum is found
# Move the left pointer to the right if current Sum is less than target, move right pointer to the left is current sum is greater than target
def twoNumberSum_optimal(array, targetSum):
    if not array:
        return []
    output = []
    array.sort()
    left = 0
    right = len(array) - 1
    while (left < right):
        currentSum = array[left] + array[right]
        if currentSum == targetSum:
            output = [array[left], array[right]]
            break
        elif currentSum < targetSum:
            left += 1
        elif currentSum > targetSum:
            right -= 1

    return output

if __name__ == '__main__':
    # The function twoNumberSum takes an array input and a target sum input
    # It should return an array on integers that sum up to the target sum 
    # Assume 1 pair exists that creates the sum
    # Sample Input: [3,5,-4,8,11,1,-1,6], 10
    # Sample Output: [-1, 11]

    arr = [3,5,-4,8,11,1,-1,6]
    targetSum = 10
    print(twoNumberSum_Loop(arr, targetSum))
    print(twoNumberSum_hashTable(arr, targetSum))
    print(twoNumberSum_optimal(arr, targetSum))
