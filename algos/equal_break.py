from math import floor
from swap_cost import swap_cost

def equal_break(homes: list[str], sorted_homes: list[str], cycle: list[str]) -> int:
    # base cases #
    if len(cycle) == 1: return 0

    # create indices for cycle and home
    mid = floor(len(cycle) / 2) - 1
    right = len(cycle) - 1
    mid_in_home = homes.index(cycle[mid])
    right_in_home = homes.index(cycle[right])

    cost = swap_cost(homes, sorted_homes, mid_in_home, right_in_home)
    homes[mid_in_home], homes[right_in_home] = homes[right_in_home], homes[mid_in_home]
    cycle[mid], cycle[right] = cycle[right], cycle[mid]
    print(f"Swap {homes[mid_in_home]} and {homes[right_in_home]}")
    return cost \
        + equal_break(homes, sorted_homes, cycle[:mid + 1]) \
        + equal_break(homes, sorted_homes, cycle[mid + 1:])

if __name__ == "__main__":
    homes = ["b2", "a3", "b1", "a1", "b3", "a2"]
    sorted_homes = ["a1", "a2", "a3", "b1", "b2", "b3"]
    cycle = ["b1", "a1", "b2", "b3", "a2", "a3"]

    print(f"Total cost: {equal_break(homes, sorted_homes, cycle)}")
