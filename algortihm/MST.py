from algortihm.Node import Node


def create_mst(distance_matrix, locations):
    """
    Create a Minimum Spanning Tree (MST) from a distance matrix using Prim's algorithm.

    :param distance_matrix: A 2D list representing the distance matrix of a fully connected graph.
    :param locations: A list of locations of the nodes.
    :return: The root node of the constructed tree.
    """
    edges, _ = create_mst_from_distance_matrix(distance_matrix)
    return construct_tree_from_mst_edges(edges, locations)


def create_mst_from_distance_matrix(distance_matrix):
    """
    Create a Minimum Spanning Tree (MST) from a distance matrix using Prim's algorithm.

    :param distance_matrix: A 2D list representing the distance matrix of a fully connected graph.
    :return: A tuple containing a list of edges in the MST and the total weight of the MST.
    """
    num_nodes = len(distance_matrix)
    in_mst = [False] * num_nodes  # Track nodes included in MST
    edge_count = 0  # Number of edges in MST
    mst_edges = []  # Store edges of MST
    total_weight = 0  # Total weight of MST

    in_mst[0] = True

    while edge_count < num_nodes - 1:
        minimum = float("inf")
        a = -1
        b = -1
        for m in range(num_nodes):
            if in_mst[m]:
                for n in range(num_nodes):
                    if not in_mst[n] and distance_matrix[m][n]:
                        if distance_matrix[m][n] < minimum:
                            minimum = distance_matrix[m][n]
                            a, b = m, n
        if a != -1 and b != -1:
            mst_edges.append((a, b))
            total_weight += minimum
            in_mst[b] = True
            edge_count += 1

    return mst_edges, total_weight


def construct_tree_from_mst_edges(mst_edges, locations):
    """
    Construct a tree from the edges of a Minimum Spanning Tree (MST).

    :param mst_edges: A list of edges in the MST, where each edge is a tuple (i, j).
    :param locations: A list of locations of the nodes.
    :return: The root node of the constructed tree.
    """
    node_map = {}  # Map of index to node for quick lookup

    # Create nodes for all unique indices in mst_edges
    for edge in mst_edges:
        for index in edge:
            if index not in node_map:
                node_map[index] = Node(index, locations[index][0], locations[index][1])

    # Set up the neighbors based on mst_edges
    for a, b in mst_edges:
        node_map[a].neighbors.append(node_map[b])
        # Assuming undirected graph; if directed, remove the next line
        node_map[b].neighbors.append(node_map[a])

    # Return the root node (assuming the first index as root for simplicity)
    return node_map[mst_edges[0][0]] if mst_edges else None
