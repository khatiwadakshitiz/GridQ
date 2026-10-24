from itertools import product

# 1. Store the problem data.
costs = [3, 5, 6, 8]
capacities = [2, 4, 5, 7]
demand = 9

# We have not found a solution yet.
best_combination = None

# Infinity ensures any feasible cost can become our first best cost.
best_cost = float("inf")
best_capacity = None

print("Combination | Capacity | Cost | Feasible")
print("-" * 43)

# 2. Generate all 16 four-bit combinations.
for combination in product([0, 1], repeat=4):

    # 3. Calculate capacity and cost for this combination.
    total_capacity = sum(
        bit * capacity
        for bit, capacity in zip(combination, capacities)
    )

    total_cost = sum(
        bit * cost
        for bit, cost in zip(combination, costs)
    )

    # 4. Check whether this combination meets demand.
    feasible = total_capacity >= demand

    bit_string = "".join(str(bit) for bit in combination)

    print(
        f"{bit_string:^11} | {total_capacity:^8} | "
        f"{total_cost:^4} | {'Yes' if feasible else 'No'}"
    )

    # 5. Keep the cheapest feasible combination found so far.
    if feasible and total_cost < best_cost:
        best_combination = combination
        best_cost = total_cost
        best_capacity = total_capacity

# 6. Print the final answer.
print("\nFINAL RESULT")

if best_combination is None:
    print("No feasible combination can meet the demand.")
else:
    selected_generators = [
        index + 1
        for index, bit in enumerate(best_combination)
        if bit == 1
    ]

    print("Best combination:", best_combination)
    print("Selected generators:", selected_generators)
    print("Total capacity:", best_capacity)
    print("Total cost:", best_cost)
    print("Demand:", demand)