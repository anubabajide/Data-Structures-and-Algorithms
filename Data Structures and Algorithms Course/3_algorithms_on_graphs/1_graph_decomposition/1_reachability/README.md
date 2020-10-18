# Finding an Exit from a Maze

## Description 
A maze is a rectangular grid of cells with walls between some of adjacent cells. You would like to check whether there is a path from a given cell to a given exit from a maze where an exit is also a cell that lies on the border of the maze (in the example shown to the right there are two exits: one on the left border and one on the right border). For this, you represent the maze as an undirected graph: vertices of the graph are cells of the maze, two vertices are connected by an undirected edge if they are adjacent and there is no wall between them. Then, to check whether there is a path between two given cells in the maze, it suffices to check that there is a path between the corresponding two vertices in the graph.

## Details
**Task**<br>
Given an undirected graph and two distinct vertices 𝑢 and 𝑣, check if there is a path between 𝑢 and 𝑣.

**Input format**<br> 
An undirected graph with 𝑛 vertices and 𝑚 edges. The next line contains two vertices 𝑢 and 𝑣 of the graph.

**Output format:**<br> 
Output 1 if there is a path between 𝑢 and 𝑣 and 0 otherwise.

**Constraints:**<br>
2 ≤ 𝑛 ≤ 10<sup>3</sup><br>
1 ≤ 𝑚 ≤ 10<sup>3</sup><br>
1 ≤ 𝑢, 𝑣 ≤ 𝑛<br> 
𝑢 ̸= 𝑣.

## Samples.
Sample 1.
    
    Input:
        4 4
        1 2
        3 2
        4 3
        1 4
        1 4
    Output:
        1

    1 __ 2
    |    |
    4 __ 3
    In this graph, there are two paths between vertices 1 and 4: 1-4 and 1-2-3-4.

Sample 2.
    Input:
        4 2
        1 2
        3 2
        1 4
    Output:
        0
    
    1    2
         |
    4 __ 3
    In this case, there is no path from 1 to 4.