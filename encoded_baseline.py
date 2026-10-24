from itertools import product

# Example problem data.
costs = [3, 5, 6, 8]
capacities = [2, 4, 5, 7]
demand = 9

penalty_strength = 24
slack_weights = [1, 2, 4, 8]

best_energy = float("inf")
best_solutions = []

# Try all generator selections.
for generator_bits in product([0, 1], repeat=4):

    total_cost = sum(
        bit * cost
        for bit, cost in zip(generator_bits, costs)
    )

    total_capacity = sum(
        bit * capacity
        for bit, capacity in zip(generator_bits, capacities)
    )

    # For each selection, try every encoded slack value.
    for slack_bits in product([0, 1], repeat=4):

        slack = sum(
            bit * weight
            for bit, weight in zip(slack_bits, slack_weights)
        )

        residual = total_capacity - demand - slack
        penalty = penalty_strength * residual ** 2
        energy = total_cost + penalty

        solution = {
            "generator_bits": generator_bits,
            "slack_bits": slack_bits,
            "capacity": total_capacity,
            "cost": total_cost,
            "slack": slack,
            "residual": residual,
            "energy": energy,
        }

        if energy < best_energy:
            best_energy = energy
            best_solutions = [solution]

        elif energy == best_energy:
            best_solutions.append(solution)

print("Minimum energy:", best_energy)

for solution in best_solutions:
    print("\nOptimal encoded solution:")
    for name, value in solution.items():
        print(f"{name}: {value}")