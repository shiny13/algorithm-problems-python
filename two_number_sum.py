#use python3
def twoNumberSum(array, targetSum):
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
if __name__ == '__main__':
    # The function twoNumberSum takes an array input and a target sum input
    # It should return an array on integers that sum up to the target sum 
    # Assume 1 pair exists that creates the sum, but 2 or more pairs may also exist
    # Sample Input: [3,5,-4,8,11,1,-1,6], 10
    # Sample Output: [-1, 11]

    arr = [3,5,-4,8,11,1,-1,6]
    targetSum = 10
    print(twoNumberSum(arr, targetSum))