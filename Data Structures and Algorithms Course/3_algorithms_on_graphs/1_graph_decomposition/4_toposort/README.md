# Determining the Order of Courses

## Description 
Now, when you are sure that there are no cyclic dependencies in the given CS curriculum, you would like to
find an order of all courses that is consistent with all dependencies. For this, you find a topological ordering
of the corresponding directed graph.

## Details
**Task**<br>
Compute a topological ordering of a given directed acyclic graph (DAG) with 𝑛 vertices and 𝑚 edges.

**Input format**<br> 
A graph is given in the standard format.

**Output format:**<br> 
Output any topological ordering of its vertices. (Many DAGs have more than just one
topological ordering. You may output any of them.)

**Constraints:**<br>
1 ≤ 𝑛 ≤ 10<sup>5</sup><br>
0 ≤ 𝑚 ≤ 10<sup>5</sup><br>
The given graph is guaranteed to be acyclic.

## Samples.
Sample 1.

    Input:
        4 3
        1 2
        4 1
        3 1
    Output:
        4 3 1 2

Sample 2.

    Input:
        4 1
        3 1
    Output:
        2 3 1 4

Sample 3.
    
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
        5 4 3 2 1
    