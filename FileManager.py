import time
import numpy as np
import os


def read_distance_matrix_from_file(file_path):
    with open(file_path, 'r') as file:
        matrix = []
        for line in file:
            row = [int(x) for x in line.split()]
            matrix.append(row)
        matrix = np.array(matrix)
    
    return matrix

def save_result_to_file(input_file_path, tsp, max_edge_length):
    index_list = [node.index for node in tsp]
    input_directory = os.path.dirname(input_file_path)
    output_file_path = os.path.join(input_directory, os.path.splitext(os.path.basename(input_file_path))[0] + "_result_" + time.strftime("%Y%m%d%H%M%S") + ".txt")
    with open(output_file_path, 'w') as file:
        file.write(' '.join(map(str, index_list)) + '\n')
        file.write(max_edge_length)