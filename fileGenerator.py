import sys
import os
import numpy as np

from tests.TSPDataGenerator import create_distance_matrix_from_locations, generate_random_locations


def save_distance_matrix_to_file(distance_matrix, directory, n, seed):
    if not os.path.exists(directory):
        os.makedirs(directory)
    file_path = os.path.join(directory, f"test_{n}_{seed}.txt")
    np.savetxt(file_path, distance_matrix, fmt='%.10f')
    return file_path

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python fileGenerator.py <number_of_locations> <seed>")
        sys.exit(1)
    
    try:
        n = int(sys.argv[1])
        seed = int(sys.argv[2])
    except ValueError:
        print("Both <number_of_locations> and <seed> must be integers.")
        sys.exit(1)

    output_directory = "./generatedFiles"

    locations = generate_random_locations(n, seed)
    distance_matrix = create_distance_matrix_from_locations(locations)
    file_path = save_distance_matrix_to_file(distance_matrix, output_directory, n, seed)
    
    print(f"Distance matrix saved to {file_path}")

