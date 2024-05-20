import numpy as np


def find_tsp(root):
    """
    Find a cycle that minimizes the longest edge. This algorithm finds a solution that is at most thrice the optimal.
    :param root: The root node an MST.
    :return: A list of nodes in the cycle.
    """
    ordered_nodes = []
    order_nodes(root, ordered_nodes)
    root.clear()
    reachable_matrix = get_reachable_matrix(root, len(ordered_nodes))
    root.clear()

    cycle = []
    curr_node = ordered_nodes[-1]
    curr_node.visited = True
    cycle.append(curr_node)
    for _ in range(len(ordered_nodes) - 1):
        for next_node in ordered_nodes:
            if (
                not next_node.visited
                and reachable_matrix[curr_node.index][next_node.index]
            ):
                next_node.visited = True
                curr_node = next_node
                cycle.append(curr_node)
                break

    return cycle


def order_nodes(node, ordered_nodes):
    """
    Order the nodes in the cycle using a depth-first traversal.
    :param node: The current node.
    :param ordered_nodes: The list of ordered nodes.
    """
    node.visited = True
    for child in node.neighbors:
        if child.visited:
            continue
        order_nodes(child, ordered_nodes)
    ordered_nodes.append(node)


def get_reachable_matrix(root, num_nodes):
    neighbor_matrix = np.full((num_nodes, num_nodes), fill_value=0, dtype=bool)

    def traverse_and_mark(node):
        node.visited = True
        for child in node.neighbors:
            if child.visited:
                continue
            neighbor_matrix[node.index][child.index] = 1
            neighbor_matrix[child.index][node.index] = 1
            traverse_and_mark(child)

    traverse_and_mark(root)

    A2 = np.matmul(neighbor_matrix, neighbor_matrix)
    A3 = np.matmul(A2, neighbor_matrix)

    reachable_in_3 = (neighbor_matrix + A2 + A3) > 0

    return reachable_in_3.astype(bool)
