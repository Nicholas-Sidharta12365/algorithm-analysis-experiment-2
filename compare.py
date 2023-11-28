import time
from memory_profiler import profile
from Branch_Bound import main as bb_main
from Greedy import main as greedy_main

def process_dataset(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        m = int(lines[0])
        subsets = [list(map(int, line.split())) for line in lines[1:-1]]  # Split each line to get the sets
        weights = list(map(int, lines[-1].split()))

    return m, subsets, weights

@profile
def run_algorithm(m, subsets, weights, algorithm, algorithm_name):
    print(f"\nProcessing with {algorithm_name}:")
    start_time = time.time()
    algorithm(m, subsets, weights)
    end_time = time.time()
    print(f"Time taken for {algorithm_name}: {end_time - start_time:.4f} seconds")

if __name__ == "__main__":
    # Process and run Branch_Bound.py and Greedy.py for each dataset
    datasets = ["weighted_set_cover_small.txt", "weighted_set_cover_medium.txt", "weighted_set_cover_large.txt"]

    for dataset in datasets:
        m, subsets, weights = process_dataset(dataset)

        run_algorithm(m, subsets, weights, bb_main, "Branch_Bound")
        run_algorithm(m, subsets, weights, greedy_main, "Greedy")
