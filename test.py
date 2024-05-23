import os
from algortihm.MST import create_mst
from algortihm.TSP import find_tsp
from input_output.FileManager import read_distance_matrix_from_file, save_result_to_file
from main import find_max_edge_length


def read_optimal_results(optimal_results_file):
    optimal_results = {}
    with open(optimal_results_file, 'r') as file:
        for line in file:
            parts = line.strip().split(':')
            if len(parts) == 2:
                file_name = parts[0].strip()
                result = float(parts[1].strip())
                optimal_results[file_name] = result
    return optimal_results


def find_total_cost(tsp, distance_matrix):
    total_cost = 0
    for i in range(len(tsp) - 1):
        total_cost += distance_matrix[tsp[i].index][tsp[i + 1].index]
    
    if len(tsp) > 1: 
         total_cost += distance_matrix[tsp[-1].index][tsp[0].index]

    return total_cost


def find_mst_max_edge_length(tree_nodes, distance_matrix):
    max_length = 0

    def dfs(node):
        nonlocal max_length
        node.visited = True
        for neighbor in node.neighbors:
            if not neighbor.visited:
                edge_length = distance_matrix[node.index][neighbor.index]
                max_length = max(max_length, edge_length)
                dfs(neighbor)

    if tree_nodes:
        dfs(tree_nodes)

    return max_length


def process_all_txt_files(input_directory, output_directory):
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    optimal_results = read_optimal_results('./tests/test-resources/optimalResults.txt')
    with open('./tests/output/test_results.txt', 'w'):
        pass

    for file_name in os.listdir(input_directory):
        if file_name.endswith('.txt'):
            input_file_path = os.path.join(input_directory, file_name)
            output_file_path = os.path.join(output_directory, file_name)
            file_name_without_extension = os.path.splitext(file_name)[0]
            print(f"Started test {file_name_without_extension}...")

            # Wywołanie funkcji dla każdego pliku
            distance_matrix = read_distance_matrix_from_file(input_file_path)
            locations = [(0, 0) for _ in range(distance_matrix.shape[0])]
            mst = create_mst(distance_matrix, locations)
            tsp = find_tsp(mst)
            max_edge_length = find_max_edge_length(tsp, distance_matrix)
            mst.clear()
            max_mst_edge_length = find_mst_max_edge_length(mst, distance_matrix)
            save_result_to_file(output_file_path, tsp, max_edge_length)


            if file_name_without_extension in optimal_results:
                optimal_result = optimal_results[file_name_without_extension]
                test_result = find_total_cost(tsp, distance_matrix)
                error = abs(test_result - optimal_result)
                percentage_error = 100 * error / optimal_result

                with open('./tests/output/test_results.txt', 'a') as results_file:
                    if os.stat('./tests/output/test_results.txt').st_size == 0:
                        results_file.write("{:<15} {:<20} {:<20} {:<20} {:<20} {:<20} {:<20} {:<25} {:<50}\n".format(
                            "test", "optimal_result", "result", "error", "percentage_error", "max_edge_length", "max_mst_edge_length", "3*max_mst_edge_length", "max_edge_length<=3*max_mst_edge_length"
                        ))
                    results_file.write("{:<15} {:<20.2f} {:<20.2f} {:<20.2f} {:<20.2f} {:<20.2f} {:<20.2f} {:<25.2f} {:<50}\n".format(
                        file_name_without_extension,
                        optimal_result,
                        test_result,
                        error,
                        percentage_error,
                        max_edge_length,
                        max_mst_edge_length,
                        3 * max_mst_edge_length,
                        str(max_edge_length <= 3 * max_mst_edge_length)
                    ))

            print(f"Finished test {file_name_without_extension}.")


def main():
    input_directory = './tests/test-resources/test-input-files'
    output_directory = './tests/output'

    process_all_txt_files(input_directory, output_directory)


main()