'''CYCLE TEST CASES
[a2,b1,a1,b2]
[b1,a1,b2,b3,a2,a3]
[c1,c2,a1,a2,b3,c3,a3,b1,b2]
'''

from swap_cost import swap_cost
from cycles import break_cycle



def five_cost_break(homes, sorted_homes, cycle):
    #base case
    if len(cycle)==1:
        return 0
    if len(cycle) == 3:
        cost = swap_cost(homes, sorted_homes, homes.index(cycle[0]), homes.index(cycle[1]))
        print(f"Swap {cycle[0]} and {cycle[1]}")
        print(f"Swap {cycle[1]} and {cycle[2]}")
        return cost
    if len(cycle) == 2:
        #print("2 base case", cycle)
        cost = swap_cost(homes, sorted_homes, homes.index(cycle[0]),homes.index(cycle[1]))
        print(f"Swap {cycle[0]} and {cycle[1]}")
        return cost

    #choose min cost (5 cost) that breaks cycle into parts of 2 each
    #candidate_swaps = []
    did_not_find = True
    for i in range(len(cycle)-2):
        home1 = cycle[i]
        if i+2 < len(cycle): #if the second elem is off the edge
            home2 = cycle[i+2]
        #else:  #Don't deal with this case for now
        #    home2 = cycle[i-len(cycle)]
        cost = swap_cost(homes, sorted_homes, homes.index(home1), homes.index(home2))
        if cost == 5:
            #print(f"Swap {cycle[i]} and {cycle[i+2]}, cost: {cost}")
            did_not_find = False
            #print(did_not_find)
            #print(i, len(cycle))
            #print(home1, home2)
            #print(homes, sorted_homes,cycle,home1,home2)
            [cycle1, cycle2] = break_cycle(homes, sorted_homes, cycle, home1, home2)

            break #we found it, break out of loop
    #print(did_not_find)
    #print(cost)
    if did_not_find:
        #print(homes, homes.index(cycle[0]), homes.index(cycle[2]))
        cost = swap_cost(homes, sorted_homes, homes.index(cycle[0]), homes.index(cycle[2]))
        #print("DID NOT FIND", cycle)
        #print(f"Swap {homes[0]} and {homes[2]}, cost: {cost}")

        [cycle1, cycle2] = break_cycle(homes, sorted_homes, cycle, cycle[0], cycle[2])
    #print(cycle)
    #print(cycle1, cycle2)
    cost += five_cost_break(homes, sorted_homes, cycle1) + five_cost_break(homes,sorted_homes, cycle2)
    return cost

if __name__ == "__main__":
    homes = ["a2", "a3", "b1", "b2", "b3", "a1"]
    sorted_homes = ["a1", "a2", "a3", "b1", "b2", "b3"]
    cycle = ["b1", "b2", "b3", "a1", "a2", "a3"]
    #print(break_cycle(homes, sorted_homes, cycle, "a1","b2"))
    print(f"Total cost: {five_cost_break(homes, sorted_homes, cycle)}")
