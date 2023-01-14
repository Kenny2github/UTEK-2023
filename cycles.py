from swap_cost import swap_cost
from utekio import read_test_case

def break_cycle_of_2(
    homes: list[str], sorted_homes: list[str], cycle: list[str]
) -> int:
    """Break a cycle of 2 by swapping its elements."""
    home1, home2 = cycle
    idx1, idx2 = homes.index(home1), homes.index(home2)
    if idx1 == idx2:
        return 0
    cost = swap_cost(homes, sorted_homes, idx1, idx2)
    homes[idx1], homes[idx2] = homes[idx2], homes[idx1]
    print(f'Swap {home1} and {home2}')
    return cost

def break_cycle(
    homes: list[str], sorted_homes: list[str], cycle: list[str],
    home1: str, home2: str,
) -> tuple[list[str], list[str]]:
    """Break a cycle by swapping two of its items.
    Returns the two broken subcycles and swaps the items in homes.
    """
    # swap in homes
    print(f'Swap {home1} and {home2}')
    hidx1, hidx2 = homes.index(home1), homes.index(home2)
    homes[hidx1], homes[hidx2] = homes[hidx2], homes[hidx1]
    # rearrange cycle so that a swapped element is first
    cidx1, cidx2 = cycle.index(home1), cycle.index(home2)
    if cidx2 < cidx1:
        cidx1, cidx2 = cidx2, cidx1
    cycle = cycle[cidx1:] + cycle[:cidx1]
    cidx2 -= cidx1
    cidx1 = 0
    # split cycle where the swap happened
    return cycle[:cidx2], cycle[cidx2:]

def make_cycles(homes: list[str], sorted_homes: list[str]
                ) -> tuple[int, list[list[str]]]:
    """Return cycles of length at least 3 in the list.
    Swap cycles of 2.
    """
    cycles: list[list[str]] = []
    waiting = (1 << len(homes)) - 1 # bitfield
    while waiting:
        cycle: list[str] = []
        idx = next(i for i in range(len(homes))
                   if waiting & (1 << i))
        home = homes[idx]
        if sorted_homes[idx] == home:
            waiting ^= 1 << idx
            continue # skip cycles of 1
        while len(cycle) <= 1 or cycle[0] != home:
            waiting ^= 1 << idx
            cycle.append(home)
            idx = sorted_homes.index(home)
            home = homes[idx]
        cycles.append(cycle)
    cost = 0
    for cycle in cycles:
        if len(cycle) == 2:
            cost += break_cycle_of_2(homes, sorted_homes, cycle)
    cycles = [cycle for cycle in cycles if len(cycle) > 2]
    return cost, cycles

if __name__ == '__main__':
    from pprint import pprint
    _, _, homes = read_test_case(input())
    sorted_homes = sorted(homes)
    _, cycles = make_cycles(homes, sorted_homes)
    cycle = cycles[0]
    home1, home2 = cycle[0], cycle[len(cycle) // 2]
    print(cycle, home1, home2)
    pprint(break_cycle(homes, sorted_homes, cycle, home1, home2))
