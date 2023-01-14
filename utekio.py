def read_test_case(filename: str) -> tuple[int, int, list[str]]:
    with open(filename) as f:
        num_kingdom = int(f.readline())
        num_rank = int(f.readline())
        homes = f.readline().split()

    return num_kingdom, num_rank, homes

def write_output(lines: list[str], filename: str):
    with open(filename, 'w') as f:
        for line in lines:
            f.write(line + '\n')
