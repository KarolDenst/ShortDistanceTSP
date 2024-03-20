from matplotlib import pyplot as plt


def visualize_mst_with_cycle(root, cycle):
    """
    Visualize the Minimum Spanning Tree (MST) using matplotlib, starting from the root node.

    :param root: The root node of the MST.
    """

    def plot_node(node, index):
        plt.plot(node.x, node.y, "ro")  # Plot the node
        plt.text(node.x, node.y, index, color="blue", fontsize=12)  # Label the node

    def plot_edge(node1, node2, lw=4, color="black"):
        plt.plot(
            [node1.x, node2.x], [node1.y, node2.y], lw=lw, color=color
        )  # Draw an edge

    def traverse_and_plot(node):
        if node.visited:
            return
        node.visited = True
        # plot_node(node)
        for child in node.neighbors:
            plot_edge(node, child)
            traverse_and_plot(child)

    def plot_cycle(cycle):
        for i in range(len(cycle)):
            plot_node(cycle[i], i)
            plot_edge(cycle[i], cycle[(i + 1) % len(cycle)], lw=2, color="red")

    plt.figure(figsize=(8, 6))
    root.clear()
    traverse_and_plot(root)
    plot_cycle(cycle)

    root.clear()

    plt.show()
