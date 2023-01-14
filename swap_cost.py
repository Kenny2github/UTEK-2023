def swap_cost(homes: list[str], sorted_homes: list[str],
              idx1: int, idx2: int) -> int:
    """Return the cost of swapping idx1 with idx2."""
    if idx1 == idx2:
        return 0
    swapped_homes = homes[:]
    swapped_homes[idx1], swapped_homes[idx2] \
        = home1, home2 = swapped_homes[idx2], swapped_homes[idx1]
    # home[0] is the city in which it resides
    if home1[0] != sorted_homes[idx1][0]:
        return 10
    if home2[0] != sorted_homes[idx2][0]:
        return 10
    return 5
