# Checking Whether Any Intersection in a City is Reachable from Any Other

## Description 
The police department of a city has made all streets one-way. You would like
to check whether it is still possible to drive legally from any intersection to
any other intersection. For this, you construct a directed graph: vertices are
intersections, there is an edge (𝑢, 𝑣) whenever there is a (one-way) street from
𝑢 to 𝑣 in the city. Then, it suffices to check whether all the vertices in the
graph lie in the same strongly connected component.

## Details
**Task**<br>
Compute the number of strongly connected components of a given directed graph with 𝑛 vertices and 𝑚 edges.

**Input format**<br> 
A graph is given in the standard format.

**Output format:**<br> 
Output the number of strongly connected components

**Constraints:**<br>
1 ≤ 𝑛 ≤ 10<sup>4</sup><br>
0 ≤ 𝑚 ≤ 10<sup>4</sup>

## Samples.
Sample 1.

    Input:
        4 4
        1 2
        4 1
        2 3
        3 1
    Output:
        2
    
        4   3
        ↓ ↙ ↑
        1 → 2
    This graph has two strongly connected components: {1, 3, 2}, {4}.
    
Sample 2.

    Input:
        5 7
        2 1
        3 2
        3 1
        4 3
        4 1
        5 2
        5 3
    Output:
        5
        
        4 → 3 ← 5
         ↘ ↙ ↘ ↙
          1 ← 2
    This graph has five strongly connected components: {1}, {2}, {3}, {4}, {5}.