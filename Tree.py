import random

from Node import Node

index = 0


def create_tree(seed=None):
    """
    Create the tree starting with the root node at the middle top of the 1x1 grid.

    :return: The root node of the tree.
    """
    random.seed(seed)
    root = Node(0, 0.5, 0.95)
    global index
    index = 1
    create_children(root, 1)
    print(index)
    return root


def create_children(parent, depth):
    """
    Recursively create children for each node with random locations based on the parent's location.

    :param parent: The parent node.
    :param depth: Current depth in the tree, used to calculate the y offset.
    """
    num_children = random.randint(1, 2)  # Random number of children (0 to 3)
    for i in range(num_children):
        # Calculate child's location based on the parent's location and index
        y_offset = -0.15
        x_offset = 0.1 * (i - (num_children - 1) / 2) / depth
        child_x = parent.x + x_offset
        child_y = parent.y + y_offset

        if child_x >= 0 and child_x <= 1 and child_y > 0 and child_y <= 1:
            # Create child node if it's within the 1x1 grid
            global index
            child = Node(index, child_x, child_y)
            index += 1
            parent.children.append(child)
            create_children(child, depth + 1)
