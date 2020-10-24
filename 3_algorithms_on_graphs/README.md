# Algorithms on Graphs

## Graph Representation in Questions
In the exercises, graphs are given as follows. The first line contains non-negative integers 𝑛 and 𝑚 — the number of vertices and the number of edges respectively. <br>
The vertices are always numbered from 1 to 𝑛. Each of the following 𝑚 lines defines an edge in the format u v where 1 ≤ 𝑢, 𝑣 ≤ 𝑛 are endpoints of the edge. <br>
If the problem deals with an undirected graph this defines an undirected edge between 𝑢 and 𝑣. <br>
In case of a directed graph this defines a directed edge from 𝑢 to 𝑣. <br>
If the problem deals with a weighted graph then each edge is given as u v w where 𝑢 and 𝑣 are vertices and 𝑤 is a weight.<br>
It is guaranteed that a given graph is simple. That is, it does not contain self-loops (edges going from a vertex to itself) and parallel edges.
←↑→↓↔↕↖↗↘ ↙

## Examples

An undirected graph with four vertices and five edges:

    4 5
    2 1
    4 3
    1 4
    2 4
    3 2

    4---3
    | \ |
    1---2
    
A directed graph with five vertices and eight edges.

    5 8
    4 3
    1 2
    3 1
    3 4
    2 5
    5 1
    5 4
    5 3

    2 → 5 → 4
     ↖ ↙ ↘↗↙
      1 ← 3
    
A directed graph with five vertices and one edge.

    5 1
    4 3

    2   5   4
           ↙
      1   3
    
    Note that the vertices 1, 2, and 5 are isolated (have no adjacent edges), but they are still present in the graph.

A weighted directed graph with three vertices and three edges.

    3 3
    2 3 9
    1 3 5
    1 2 -2
    
        3
    (5)↗ ↖(9)
      1 → 2
       (-2)
       