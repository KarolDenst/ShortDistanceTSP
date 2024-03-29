class Node:
    def __init__(self, index, x, y):
        self.visited = False  # Flag to indicate if the node has been visited
        self.index = index  # The index of the node
        self.x = x  # The x-coordinate of the node
        self.y = y  # The y-coordinate of the node
        self.neighbors = []  # List of neighbors nodes

    def clear(self):
        self.visited = False
        for child in self.neighbors:
            if child.visited:
                child.clear()
