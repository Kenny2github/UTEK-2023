from swap_cost import swap_cost
from cycles import break_cycle_of_2

def selection_sort(homes: list[str], sorted_homes: list[str], cycle: list[str]) -> int:
    # N.B. no-op if already sorted, so safe to call again
    cost = 0
    for i in range(len(homes)):
        idx = min(
            range(i, len(homes)),
            key=lambda idx: (homes[idx], swap_cost(
                homes, sorted_homes, i, idx))
        )
        cost += break_cycle_of_2(homes, sorted_homes, [homes[i], homes[idx]])
    return cost

def haphazard_selection_sort(
    homes: list[str], sorted_homes: list[str], cycle: list[str]
) -> int:
    cost = 0
    is_sorted = 0 # bitfield
    for _ in range(len(homes)):
        remaining_dests = (dest for dest in range(len(homes))
                           if not (is_sorted & (1 << dest)))
        # find the destination that costs the least
        dest = min(remaining_dests, key=lambda dest:
            swap_cost(homes, sorted_homes, homes.index(sorted_homes[dest]), dest))
        is_sorted |= 1 << dest # mark it sorted in advance
        # find the item that goes here
        source = homes.index(sorted_homes[dest])
        cost += break_cycle_of_2(homes, sorted_homes, [homes[source], homes[dest]])
    return cost
