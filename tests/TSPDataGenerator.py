import math
import random


def generate_random_locations(n, seed=None):
    """
    Generate n random locations within a 2D space, with each coordinate between 0 and 1, using a specified seed.

    :param n: Number of random locations to generate.
    :param seed: Seed for the random number generator to ensure reproducibility.
    :return: A list of tuples, where each tuple represents the (x, y) coordinates of a location.
    """
    random.seed(seed)  # Set the seed
    return [(random.random(), random.random()) for _ in range(n)]


def create_distance_matrix(n, seed):
    """
    Generate a distance matrix directly from the number of nodes and seed, version 1.

    :param n: Number of nodes (random locations) to generate.
    :param seed: Seed for the random number generator to ensure reproducibility.
    :return: A 2D list representing the distance matrix.
    """
    locations = generate_random_locations(n, seed)
    return create_distance_matrix_from_locations(locations)


def create_distance_matrix_from_locations(locations):
    """
    Create a distance matrix from a list of locations, where each entry (i, j) contains
    the Euclidean distance between point i and point j.

    :param locations: List of tuples, where each tuple represents the (x, y) coordinates of a location.
    :return: A 2D list representing the distance matrix.
    """
    n = len(locations)
    distance_matrix = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if i != j:
                # Calculate the Euclidean distance between points i and j
                distance_matrix[i][j] = math.sqrt((locations[i][0] - locations[j][0]) ** 2 +
                                                  (locations[i][1] - locations[j][1]) ** 2)
    return distance_matrix
