#Performs a binary search in the array to return the closes value
def findClosestValueInBst(tree, target):
    if not tree:
        return 0
    left = 0
    right = len(tree) - 1
    value = 0
    if tree[left] > target:
        value = tree[left]
        return value
    elif tree[right] < target:
        value = tree[right]
        return value
    while(left < right):
        if tree[left] == target:
            value = tree[left]
            break
        elif tree[right] == target:
            value = tree[right]
            break
        if right - left <= 1:
            leftVal = tree[left] - target
            if leftVal < 0:
                leftVal *= -1
            rightVal = tree[right] - target
            if rightVal < 0:
                rightVal *= -1
            if leftVal <= rightVal:
                value = tree[left]
                break
            else:
                value = tree[right]
                break
        midpoint = ((right - left) // 2) + left
        print("left {} right {} midpoint {}".format(left, right, midpoint))
        if tree[midpoint] <= target:
            left = midpoint
        elif tree[midpoint] >= target:
            right = midpoint

    return value

if __name__ == '__main__':
    array = [1,2,5,5,10,15,13,14,22]
    target = 12
    print(findClosestValueInBst(array, target))
