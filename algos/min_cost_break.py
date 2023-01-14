from swap_cost import swap_cost
from cycles import break_cycle_of_2, break_cycle

def min_cost_break(homes: list[str], sorted_homes: list[str], cycle: list[str]) -> int:
    # cycle length 1: no op, cost 0
    if len(cycle) == 1:
        return 0

    # cycle length 2: break cycle, return cost
    elif len(cycle) == 2:
        return break_cycle_of_2(homes, sorted_homes, cycle)

    # cycle length > 2
    # check all combinations (swaps), going through the cycle using for loops to check if cost 5 swap appears that break the loop
    else:
        for i in (range(len(cycle))):
           for j in (range(i, len(cycle))):
                cost = swap_cost(homes, sorted_homes, homes.index(cycle[i]), homes.index(cycle[j]))
                if cost == 5:
                    cycle1, cycle2 = break_cycle(homes, sorted_homes, cycle, cycle[i], cycle[j])
                    return cost + min_cost_break(homes, sorted_homes, cycle1) + min_cost_break(homes, sorted_homes, cycle2)
        #if cost 5 is not the minimum cost that breaks the cycle, return 10, whcih should be the minimum cost break
        cycle1, cycle2 = break_cycle(homes, sorted_homes, cycle, cycle[0], cycle[1])
        return 10 + min_cost_break(homes, sorted_homes, cycle1) + min_cost_break(homes, sorted_homes, cycle2)

if __name__ == "__main__":
    homes = ["b2", "a3", "b1", "a1", "b3", "a2"]
    sorted_homes = ["a1", "a2", "a3", "b1", "b2", "b3"]
    cycle = ["b1", "a1", "b2", "b3", "a2", "a3"]

    print(f"Total cost: {min_cost_break(homes, sorted_homes, cycle)}")
