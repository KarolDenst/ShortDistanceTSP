# Short distance TSP

## Help
```
python main.py -help
```

## Input from file
Command reads a graph from specified file and saves result in file in the same directory as input file:
```
python main.py <path_to_file>
```

## Random input
Command creates a random planar graph with the specified number of vertices based on the seed. It then displays the solution for the created graph:
```
python main.py -random <seed> <number_of_vertices>>
```

## Test
Command runs tests and saves result in '.\tests\output':
```
python test.py
```

## File generator
Command generates an input file in './generatedFiles' directory based on the given seed and number of locations:
```
python fileGenerator.py <number_of_locations> <seed>
```

