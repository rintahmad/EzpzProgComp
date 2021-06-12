# References
#https://www.techiedelight.com/chess-knight-problem-find-shortest-path-source-destination/
import sys
from collections import deque
 
 
# A queue node used in BFS
class Node:
    # `(x, y)` represents chessboard coordinates
    # `dist` represents its minimum distance from the source
    def __init__(self, x, y, dist=0):
        self.x = x
        self.y = y
        self.dist = dist
 
    # As we are using `Node` as a key in a dictionary,
    # we need to override the `__hash__()` and `__eq__()` function
    def __hash__(self):
        return hash((self.x, self.y, self.dist))
 
    def __eq__(self, other):
        return (self.x, self.y, self.dist) == (other.x, other.y, other.dist)
 
 
# Below lists detail all eight possible movements for a knight
row = [2, 2, -2, -2, 1, 1, -1, -1]
col = [-1, 1, 1, -1, 2, -2, 2, -2]
 
 
# Check if `(x, y)` is valid chessboard coordinates.
# Note that a knight cannot go out of the chessboard
def isValid(x, y, N):
    return not (x < 0 or y < 0 or x >= N or y >= N)
 
 
# Find the minimum number of steps taken by the knight
# from the source to reach the destination using BFS
def BFS(src, dest, N):
 
    # set to check if the matrix cell is visited before or not
    visited = set()
 
    # create a queue and enqueue the first node
    q = deque()
    q.append(src)
 
    # loop till queue is empty
    while q:
 
        # dequeue front node and process it
        node = q.popleft()
 
        x = node.x
        y = node.y
        dist = node.dist
 
        # if the destination is reached, return distance
        if x == dest.x and y == dest.y:
            return dist
 
        # skip if the location is visited before
        if node not in visited:
            # mark the current node as visited
            visited.add(node)
 
            # check for all eight possible movements for a knight
            # and enqueue each valid movement
            for i in range(8):
                # Get the knight's valid position from the current position on
                # the chessboard and enqueue it with +1 distance
                x1 = x + row[i]
                y1 = y + col[i]
 
                if isValid(x1, y1, N):
                    q.append(Node(x1, y1, dist + 1))
 
    # return infinity if the path is not possible
    return sys.maxsize
 
 
if __name__ == '__main__':
 
    objects = {"A":0,"B":1,"C":2,"D":3,"E":4,"F":5,"G":6,"H":7} 
    src = Node(0, 0)    # source coordinates

    # Loop
    for i in range(int(input())):
        inputs = input()
        dest = Node(objects[inputs[0]],int(inputs[1])-1)
 
        print(BFS(src, dest, 8))
