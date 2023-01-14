import sys
import io
from typing import Callable
from contextlib import redirect_stdout

from cycles import make_cycles
from utekio import read_test_case

from algos.selection import selection_sort, haphazard_selection_sort
from algos.min_cost_break import min_cost_break
from algos.five_cost_break import five_cost_break
from algos.equal_break import equal_break

def run_all(infile: str, outfile: str) -> None:
    strategies: list[Callable[[list[str], list[str], list[str]], int]] = [
        selection_sort,
        haphazard_selection_sort,
        min_cost_break,
        # five_cost_break,
        equal_break,
    ]
    _, _, original_homes = read_test_case(infile)
    sorted_homes = sorted(original_homes)

    # find cycles and make swaps for 2-cycles
    base_output = io.StringIO()
    with redirect_stdout(base_output):
        base_cost, cycles = make_cycles(original_homes, sorted_homes)

    # try each strategy in turn
    results: list[tuple[int, str]] = [] # cost, output
    for strategy in strategies:
        homes = original_homes[:]
        output = io.StringIO()
        with redirect_stdout(output):
            # run the strategy on every cycle
            cost = sum(strategy(homes, sorted_homes, cycle)
                       for cycle in cycles)
        if homes == sorted_homes:
            results.append((base_cost + cost,
                            base_output.getvalue() + output.getvalue()))
        else:
            print(f'WARNING: {strategy.__name__} is incorrect!', homes)

    for (cost, output), strategy in zip(results, strategies):
        print(f'{strategy.__name__}: {cost}')

    # show the best strategy
    best_idx = min(range(len(strategies)), key=lambda i: results[i][0])
    best_cost, best_output = results[best_idx]
    print(f'Best strategy was {strategies[best_idx].__name__}; it cost {best_cost}')
    with open(outfile, 'w') as f:
        f.write(best_output)
    print(best_output)

if __name__ == '__main__':

    run_all(sys.argv[1], sys.argv[1].replace('.in', '.out').replace('input', 'output'))
