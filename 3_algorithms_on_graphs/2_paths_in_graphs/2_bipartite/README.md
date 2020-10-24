# Checking whether a Graph is Bipartite

## Description 
An undirected graph is called bipartite if its vertices can be split into two parts such that each edge of the
graph joins to vertices from different parts. Bipartite graphs arise naturally in applications where a graph
is used to model connections between objects of two different types (say, boys and girls; or students and
dormitories).<br>
An alternative definition is the following: a graph is bipartite if its vertices can be colored with two colors
(say, black and white) such that the endpoints of each edge have different colors.

## Details
**Task**<br>
Given an undirected graph with 𝑛 vertices and 𝑚 edges, check whether it is bipartite.

**Input format**<br> 
A graph is given in the standard format. 

**Output format:**<br> 
Output 1 if the graph is bipartite and 0 otherwise.

**Constraints:**<br>
1 ≤ 𝑛 ≤ 10<sup>5</sup><br>
0 ≤ 𝑚 ≤ 10<sup>5</sup>

## Samples.
Sample 1.

    Input:
        4 4
        1 2
        4 1
        2 3
        3 1
    Output:
        0

        4   3
        | / |
        1 _ 2
    This graph is not bipartite. To see this assume that the vertex 1 is colored white. Then the vertices 2 and 3 should be colored black since the graph contains the edges {1, 2} and {1, 3}. But then the edge {2, 3} has both endpoints of the same color.


Sample 2.

    Input:
        5 4
        5 2
        1 3
        3 4
        1 4
    Output:
        1
    
        3 _ 4   5
           / \ /
          1   2
    This graph is bipartite: assign the vertices 4 and 5 the white color, assign all the remaining vertices the black color.
    