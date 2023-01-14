import sys
from itertools import product

def read_input(filename: str) -> tuple[int, int, list[str]]:
    with open(filename) as f:
        num_kingdom = int(f.readline())
        num_rank = int(f.readline())
        homes = f.readline().split()

    return num_kingdom, num_rank, homes

def write_output(lines: list[str], filename: str):
    with open(filename, 'w') as f:
        for line in lines:
            f.write(line + '\n')

def selection_sort() -> list[str]:
    output_lines = []
    for i in range(len(homes)):
        idx, smallest = min(
            enumerate(homes[i:], start=i),
            key=lambda homepair: homepair[1]
        )
        if idx == i:
            continue
        homes[i], homes[idx] = homes[idx], homes[i]
        output_lines.append(f"Swap {homes[idx]} and {homes[i]}")

    return output_lines

if __name__ == '__main__':
    test_cases = ['2a', '2b', '2c']
    for test in test_cases:
        num_kingdom, num_rank, homes = read_input(test + ".in")

        sorted_homes = sorted(homes)
        swaps = selection_sort()

        write_output(swaps, test + '.out')
