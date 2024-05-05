import sys

from FileManager import read_distance_matrix_from_file, save_result_to_file
from MST import create_mst
from TPSDataGenerator import (
    generate_random_locations,
    create_distance_matrix_from_locations,
)
from TSP import find_tsp
from Tree import create_tree
from Visualize import visualize_mst_with_cycle


def test(n, max):
    i = 0
    index = 1
    while i < max:
        locations = generate_random_locations(n, i)
        distance_matrix = create_distance_matrix_from_locations(locations)
        mst = create_mst(distance_matrix, locations)
        tsp = find_tsp(mst)
        if len(tsp) != len(locations):
            print(f"Error for seed {i}")
            break
        i += 1

        if i == index or i == max:
            print(f"Done for the first {i} seeds")
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


def find_max_edge_length(tsp, distance_matrix):
    max_edge_length = 0
    for i in range(len(tsp)):
        for j in range(i + 1, len(tsp)):
            distance = distance_matrix[tsp[i].index][tsp[j].index]
            if distance > max_edge_length:
                max_edge_length = distance
    
    if len(tsp) > 1: 
        distance = distance_matrix[tsp[-1].index][tsp[0].index]
        if distance > max_edge_length:
            max_edge_length = distance

    return str(max_edge_length)



def main():
    args = sys.argv[1:]
    
    if len(args) == 0:
        print("No arguments. Possible options: \n\t-> python main.py -help \n\t-> python main.py -random <seed> <number_of_locations> \n\t-> python main.py -test <number_of_locations> <number_of_iterations> \n\t-> python main.py <path_to_source_file>")
        return
    
    if args[0] == '-help':
        print("Possible options: \n\t-> python main.py -help \n\t-> python main.py -random <seed> <number_of_locations> \n\t-> python main.py -test <number_of_locations> <number_of_iterations> \n\t-> python main.py <path_to_source_file>")
        return
    if args[0] == '-random':
        if len(args) < 2:
            print("No seed. Expected command:\n\t python main.py -random <seed> <number_of_locations>")
            return
        if len(args) < 3:
            print("No number of locations. Expected command:\n\t python main.py -random <seed> <number_of_locations>")
            return
        seed = int(args[1])
        n = int(args[2])
        visualize(n, seed)
        return
    if args[0] == '-test':
        if len(args) < 2:
            print("No number of locations. Expected command:\n\t python main.py -test <number_of_locations> <number_of_iterations>")
            return
        if len(args) < 3:
            print("No number of iterations. Expected command:\n\t python main.py -test <number_of_locations> <number_of_iterations>")
            return
        test(int(args[1]), int(args[2]))
        return
    
    distance_matrix = read_distance_matrix_from_file(args[0])
    locations = [(0, 0) for _ in range(distance_matrix.shape[0])]
    mst = create_mst(distance_matrix, locations)
    tsp = find_tsp(mst)
    save_result_to_file(args[0], tsp, find_max_edge_length(tsp, distance_matrix))
    

if __name__ == "__main__":
    main()
    # visualize(10, 2)
    # visualize_tree(None)
    # test(20)
