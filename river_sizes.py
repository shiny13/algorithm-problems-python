#use python3
def riverSizes(matrix):
    sizes = []
    visited = [[False for value in row] for row in matrix]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if visited[i][j]:
                continue
            currentRiverSize = traverseNode(i, j, matrix, visited, sizes)
            if currentRiverSize > 0:
                sizes.append(currentRiverSize)
    sizes.sort(reverse=False)
    return sizes

def traverseNode(i, j, matrix, visited, sizes):
    currentRiverSize = 0
    #using a stack for DFS
    nodesToExplore = [[i,j]]
    while len(nodesToExplore):
        currentNode = nodesToExplore.pop()
        i = currentNode[0]
        j = currentNode[1]
        if visited[i][j]:
            continue
        visited[i][j] = True
        if matrix[i][j] == 0:
            continue
        currentRiverSize += 1
        unvisitedNeighbours = getUnvisitedNeighbours(i, j, matrix, visited)
        for neighbour in unvisitedNeighbours:
            nodesToExplore.append(neighbour)
    return currentRiverSize

def getUnvisitedNeighbours(i, j, matrix, visited):
    unvisitedNeighbours = []
    if i > 0 and not visited[i-1][j]:
        unvisitedNeighbours.append([i-1, j])
    if i < len(matrix) - 1 and not visited[i+1][j]:
        unvisitedNeighbours.append([i+1, j])
    if j > 0 and not visited[i][j-1]:
        unvisitedNeighbours.append([i, j-1])
    if j < len(matrix[0]) - 1 and not visited[i][j+1]:
        unvisitedNeighbours.append([i, j+1])
    return unvisitedNeighbours

if __name__ == '__main__':
    #No need for input, the sample runs a 2D matrix array as follows
    #Enter code here to generate one or multiple 2D matrices with values 0s and 1s
    #where 1 denotes river and 0 denotes land. 
    matrix = [
        [1,0,0,1,0],
        [1,0,1,0,0],
        [0,0,1,0,1],
        [1,0,1,0,1],
        [1,0,1,1,0]
    ]
    
    #testing matrix format
    #for m in matrix: print(m)
    print(riverSizes(matrix))