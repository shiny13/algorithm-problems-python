# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, values, i=0):
        if i >= len(values):
            return
        queue = [self]
        while len(queue) > 0:
            current = queue.pop(0)
            if current.left is None:
                current.left = BinaryTree(values[i])
                break
            queue.append(current.left)
            if current.right is None:
                current.right = BinaryTree(values[i])
                break
            queue.append(current.right)
        self.insert(values, i+1)
        return self

# Logic to generate the return branch sums in an array in recurssion
# Time: O(n) | Space: O(n)
def branchSums(root):
    leafSums = []
    initiazeLeaves(root, leafSums)
    print(leafSums)
    return leafSums

# Main recursive algorithm
def initiazeLeaves(node, leafSums, val = 0):
    if not node:
        return
       
    if not node.left and not node.right: 
        val += node.value 
        leafSums.append(val)
        return
    
    initiazeLeaves(node.left, leafSums, node.value + val) 
    initiazeLeaves(node.right, leafSums, node.value + val) 

# Algo Expert Solution:
# Time: O(n) | Space: O(n)
def branchSums_AE(root):
    sums = []
    calculateBranchSums(root, 0 , sums)
    return sums 

def calculateBranchSums(node, runningSum, sums):
    if node is None:
        return
    
    newRunningSum = runningSum + node.value 
    if node.left is None and node.right is None:
        sums.append(newRunningSum)
        return
    calculateBranchSums(node.left, newRunningSum, sums)
    calculateBranchSums(node.right, newRunningSum, sums)

if __name__ == "__main__":
    #testing a tree with custom case
    tree = BinaryTree(0)
    tree.left = BinaryTree(2)
    tree.left.left = BinaryTree(20)
    tree.right = BinaryTree(1)
    tree.right.right = BinaryTree(10)
    tree.right.right.right = BinaryTree(100)
    branchSums(tree)

    #Expected [1]
    tree = BinaryTree(1)
    branchSums(tree)

    #Expected [3]
    tree = BinaryTree(1).insert([2])
    branchSums(tree)

    #Expected [3, 4]
    tree = BinaryTree(1).insert([2, 3])
    branchSums(tree)

    #Expected [7, 8, 4]
    tree = BinaryTree(1).insert([2, 3, 4, 5])
    branchSums(tree)
