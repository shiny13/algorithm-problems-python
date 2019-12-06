# Performs Binary search in a tree and does absolute value (target = currentValue) and traverses left or right
# Average: O(log(n)) time | O(log(n)) space
# Worst: O(n) time | O(n) space
def findClosestValueInBst_Recursive(tree, target):
    return findClosestValueInBSTHelper_Recursive(tree, target, float('inf'))

def findClosestValueInBSTHelper_Recursive(tree, target, closest):
    if tree is None: 
        return closest
    if abs(target - closest) > abs(target - tree.value):
        closest = tree.value 
    if target < tree.value: 
        return findClosestValueInBSTHelper_Recursive(tree.left, target, closest)
    elif target > tree.value: 
        return findClosestValueInBSTHelper_Recursive(tree.right, target, closest)
    else:
        return closest

# Same solution done iteratively
# Average: O(n) time | O(1) space
# Worst: O(n) time | O(1) space
# Here the recursion call stack is not used, so space is saved
def findClosestValueInBst_Iterative(tree, target):
    return findClosestValueInBSTHelper_Iterative(tree, target, float('inf'))

def findClosestValueInBSTHelper_Iterative(tree, target, closest):
    currentNode = tree
    while currentNode is not None:
        if abs(target - closest) > abs(target - currentNode.value):
            closest = currentNode.value 
        if target < currentNode.value: 
            currentNode = currentNode.left
        elif target > currentNode.value: 
            currentNode = currentNode.right
        else:
            break
    return closest