#  Computing the Minimum Cost of a Flight

## Description 
Now, you are interested in minimizing not the number of segments, but the total cost of a flight. For this
you construct a weighted graph: the weight of an edge from one city to another one is the cost of the
corresponding flight.

## Details
**Task**<br>
Given an directed graph with positive edge weights and with 𝑛 vertices and 𝑚 edges as well as two
vertices 𝑢 and 𝑣, compute the weight of a shortest path between 𝑢 and 𝑣 (that is, the minimum total
weight of a path from 𝑢 to 𝑣).

**Input format**<br> 
A graph is given in the standard format. The next line contains two vertices 𝑢 and 𝑣.

**Output format:**<br> 
Output the minimum weight of a path from 𝑢 to 𝑣, or −1 if there is no path.

**Constraints:**<br>
1 ≤ 𝑛 ≤ 10<sup>4</sup><br>
0 ≤ 𝑚 ≤ 10<sup>5</sup><br>
1 ≤ 𝑢, 𝑣 ≤ 𝑛<br> 
𝑢 ̸= 𝑣.<br>
Edge weights are non-negative integers not
exceeding 10<sup>8</sup>

## Samples.
Sample 1.

    Input:
        4 4
        1 2 1
        4 1 2
        2 3 2
        1 3 5
        1 3
    Output:
        3

        4     3
        ↓  5↗ ↑
       2↓ ↗   ↑2
        1 → → 2
          1
    There is a unique shortest path from vertex 1 to vertex 3 in this graph (1 → 2 → 3), and it has weight 3.

Sample 2.

    Input:
       5 9
        1 2 4
        1 3 2
        2 3 2
        3 2 1
        2 4 2
        3 5 4
        5 4 1
        2 5 3
        3 4 4
        1 5
    Output:
        6
    
    There are two paths from 1 to 5 of total weight 6: 1 → 3 → 5 and 1 → 3 → 2 → 5.

Sample 3.
    Input:
        3 3
        1 2 7
        1 3 5
        2 3 2
        3 2
    Output:
        -1
    
    There is no path from 3 to 2.
    