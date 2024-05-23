import math
import os

def parse_tsp_file(file_path):
    coordinates = []
    with open(file_path, 'r') as file:
        lines = file.readlines()
        node_section = False
        for line in lines:
            line = line.strip()
            if line == 'NODE_COORD_SECTION':
                node_section = True
                continue
            if line == 'DISPLAY_DATA_SECTION':
                node_section = True
                continue
            if node_section:
                if line == 'EOF' or line == '':
                    break
                parts = line.split()
                if len(parts) == 3:
                    index = int(parts[0])
                    x = float(parts[1])
                    y = float(parts[2])
                    coordinates.append((index, x, y))
    return coordinates


def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def compute_adjacency_matrix(coordinates):
    n = len(coordinates)
    matrix = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                x1, y1 = coordinates[i][1], coordinates[i][2]
                x2, y2 = coordinates[j][1], coordinates[j][2]
                matrix[i][j] = euclidean_distance(x1, y1, x2, y2)
    return matrix


def write_adjacency_matrix(matrix, output_file_path):
    with open(output_file_path, 'w') as file:
        for row in matrix:
            file.write(' '.join(f"{dist:.2f}" for dist in row) + '\n')


def process_all_tsp_files(input_directory, output_directory):
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    for file_name in os.listdir(input_directory):
        if file_name.endswith('.tsp'):
            input_file_path = os.path.join(input_directory, file_name)
            output_file_name = file_name.replace('.tsp', '.txt')
            output_file_path = os.path.join(output_directory, output_file_name)

            print(f"Processing {input_file_path}...")
            coordinates = parse_tsp_file(input_file_path)
            coordinates.sort()
            matrix = compute_adjacency_matrix(coordinates)
            write_adjacency_matrix(matrix, output_file_path)
            print(f"Saved adjacency matrix to {output_file_path}.")


def main():
    input_directory = './tests/test-resources/original-files'
    output_directory = './tests/test-resources/test-input-files'

    process_all_tsp_files(input_directory, output_directory)


if __name__ == "__main__":
    main()

