import sys

from input_output.FileManager import read_distance_matrix_from_file, save_result_to_file
from algortihm.MST import create_mst
from tests.TSPDataGenerator import (
    generate_random_locations,
    create_distance_matrix_from_locations,
)
from algortihm.TSP import find_tsp
from algortihm.Tree import create_tree
from input_output.Visualize import visualize_mst_with_cycle


def random_test(n, max):
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
        print("No arguments. Possible options: \n\t-> python main.py -help \n\t-> python main.py -random <seed> <number_of_vertices> \n\t-> python main.py <path_to_file>")
        return
    
    if args[0] == '-help':
        print("Possible options: \n\t-> Help: \n\n\t\t python main.py -help \n\n\t-> Command reads graph from specified file and saves result in file in the same directory as input file: \n\n\t\t python main.py -random <seed> <number_of_vertices> \n\n\t-> Command creates random graph with specified number of vertices based on seed: \n\n\t\t python main.py <path_to_file>\n")
        return
    if args[0] == '-random':
        if len(args) < 2:
            print("No seed. Expected command:\n\t python main.py -random <seed> <number_of_vertices>")
            return
        if len(args) < 3:
            print("No number of locations. Expected command:\n\t python main.py -random <seed> <number_of_vertices>")
            return
        seed = int(args[1])
        n = int(args[2])
        visualize(n, seed)
        return
    if args[0] == '-test':
        print("Tests started...")
        
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
