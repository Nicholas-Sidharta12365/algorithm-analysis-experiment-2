import random

def generate_weighted_set_cover_data(num_elements, num_sets, max_cost_per_set):
    # Generate a universe of elements
    universe = set(range(1, num_elements + 1))

    # Generate sets with associated costs
    sets = []
    costs = []
    for i in range(1, num_sets + 1):
        # Ensure that each element appears in at least one set
        if universe:
            set_size = random.randint(1, min(num_elements // 2, len(universe)))
            elements_in_set = random.sample(universe, set_size)
            universe -= set(elements_in_set)
        else:
            # If all elements are already covered, create a set with a single element
            elements_in_set = [random.choice(range(1, num_elements + 1))]

        cost = random.randint(1, max_cost_per_set)
        sets.append(elements_in_set)
        costs.append(cost)

    return str(num_elements), sets, costs

def save_to_file(file_name, universe, sets, costs):
    with open(file_name, 'w') as file:
        file.write(f"{universe}\n")
        for elements_in_set in sets:
            file.write(" ".join(map(str, elements_in_set)) + "\n")
        file.write(" ".join(map(str, costs)))

# Generate and save data for small set
num_elements_small = 20
num_sets_small = 10
max_cost_per_set_small = 10
universe_small, sets_small, costs_small = generate_weighted_set_cover_data(num_elements_small, num_sets_small, max_cost_per_set_small)
save_to_file('weighted_set_cover_small.txt', universe_small, sets_small, costs_small)

# Generate and save data for medium set
num_elements_medium = 200
num_sets_medium = 50
max_cost_per_set_medium = 20
universe_medium, sets_medium, costs_medium = generate_weighted_set_cover_data(num_elements_medium, num_sets_medium, max_cost_per_set_medium)
save_to_file('weighted_set_cover_medium.txt', universe_medium, sets_medium, costs_medium)

# Generate and save data for large set
num_elements_large = 2000
num_sets_large = 500
max_cost_per_set_large = 50
universe_large, sets_large, costs_large = generate_weighted_set_cover_data(num_elements_large, num_sets_large, max_cost_per_set_large)
save_to_file('weighted_set_cover_large.txt', universe_large, sets_large, costs_large)
