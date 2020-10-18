# Adding Exits to a Maze

## Description 
Now you decide to make sure that there are no dead zones in a maze, that is, that at least one exit is reachable from each cell. For this, you find connected components of the corresponding undirected graph and ensure that each component contains an exit cell.

## Details
**Task**<br>
Given an undirected graph with 𝑛 vertices and 𝑚 edges, compute the number of connected components in it.

**Input format**<br> 
A graph is given in the standard format.

**Output format:**<br> 
Output the number of connected components.

**Constraints:**<br>
2 ≤ 𝑛 ≤ 10<sup>3</sup><br>
1 ≤ 𝑚 ≤ 10<sup>3</sup>

## Samples.
Sample 1.

    Input:
        4 2
        1 2
        3 2
        1 4
    Output:
        2
    
    1    2
         |
    4 __ 3
    There are two connected components here: {1, 2, 3} and {4}.
