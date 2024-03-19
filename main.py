from MST import create_mst
from TPSDataGenerator import (
    generate_random_locations,
    create_distance_matrix_from_locations,
)
from TSP import find_tsp
from Tree import create_tree
from Visualize import visualize_mst_with_cycle


def test(n):
    i = 0
    index = 1
    while True:
        locations = generate_random_locations(n, i)
        distance_matrix = create_distance_matrix_from_locations(locations)
        mst = create_mst(distance_matrix, locations)
        tsp = find_tsp(mst)
        if len(tsp) != len(locations):
            print(f"Error for seed {i}")
            break
        i += 1

        if i == index:
            print(f"Done for the first {index} seeds")
            index *= 10


def visualize(n, seed):
    locations = generate_random_locations(n, seed)
    distance_matrix = create_distance_matrix_from_locations(locations)
    mst = create_mst(distance_matrix, locations)
    tsp = find_tsp(mst)
    visualize_mst_with_cycle(mst, tsp)


def visualize_tree(seed):
    tree = create_tree(seed)
    tsp = find_tsp(tree)
    visualize_mst_with_cycle(tree, tsp)
    index_list = [node.index for node in tsp]
    print(index_list)


if __name__ == "__main__":
    # visualize(10, 2)
    visualize_tree(None)
    # test(20)
