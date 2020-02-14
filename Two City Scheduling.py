def twoCitySchedCost(self, costs: List[List[int]]) -> int:
    t=len(costs)//2
    s1=0
    # sort list according to difference between two costs
    costs = sorted(costs, key=lambda x: x[0]-x[1])
    #sum half of all costs[0] with half of all costs[1] in sorted list
    for x in costs[:t]:
        s1+=x[0] 
    for x in costs[t:]:
        s1+=x[1] 
    return s1
