import numpy as np

class Node():

    def __init__(self, position = None, parent = None):
        self.position = position
        self.parent = parent

        self.f = 0
        self.g = 0
        self.h = 0


def aStar(maze, startPos, endPos):

    startNode = Node(startPos, None)
    endNode = Node(endPos, None)
    open_list = [endNode]
    closed_list = []

    open_list.append(startNode)
    startNode.h = endNode.g = (endNode.position[0]-startNode.position[0])**2 + (endNode.position[1]-startNode.position[1])**2
    startNode.f = endNode.f = (endNode.position[0]-startNode.position[0])**2 + (endNode.position[1]-startNode.position[1])**2
    # check to see if the end is reached
    #    # if there exists a node in the closed list that has the same position as the endNode position

    while len(open_list) > 0:
        # append the lowest f value in the open list to the closed list and delete it from the open list
        current_node = open_list[0]

        # Search all around the latest value of the closed list (parent) and define the nodes around it (children)
        children = []
        for look in [(-1, -1), (0, -1), (1, -1), (-1, 0), (0, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]:
            look_location = (current_node.position[0] + look[0], current_node.position[1] + look[1])
            child = Node(look_location, current_node)
            child.g = current_node.g + 1
            child.h = (endNode.position[0] - current_node.position[0]) ** 2 + \
                      (endNode.position[1] - current_node.position[1]) ** 2
            child.f = current_node.g + current_node.h
            children.append(child)

        for child in children:
            if (child.position[0] < 0) or (child.position[1] < 0) or (child.position[0] > len(maze)) or (child.position[0] > len(maze)):
                continue

            if maze[child.position[0]][child.position[1]] == 1:
                continue

            open_list.append(child)
            open_list.pop(0)
            open_list.position.sort()
            print(child.position)

        #    # ignore child if not walkable
        #    # if walkable, add the child to the open list
        #    # if the child's position is already in the open list, see if its path is better than the one already in t
        #      open list (child.g is lower). If it is, replace the old one with this child, then recalculate this
        #      child's f and g scores
        #    # resort the open list (bubble sort function)

maze = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

aStar(maze, (0, 1), (5, 5))
