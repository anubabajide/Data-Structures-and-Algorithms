# Checking Consistency of CS Curriculum

## Description 
A Computer Science curriculum specifies the prerequisites for each course as a list of courses that should be
taken before taking this course. You would like to perform a consistency check of the curriculum, that is,
to check that there are no cyclic dependencies. For this, you construct the following directed graph: vertices
correspond to courses, there is a directed edge (𝑢, 𝑣) is the course 𝑢 should be taken before the course 𝑣.
Then, it is enough to check whether the resulting graph contains a cycle.

## Details
**Task**<br>
Check whether a given directed graph with 𝑛 vertices and 𝑚 edges contains a cycle.

**Input format**<br> 
A graph is given in the standard format.

**Output format:**<br> 
Output 1 if the graph contains a cycle and 0 otherwise.

**Constraints:**<br>
1 ≤ 𝑛 ≤ 10<sup>3</sup><br>
0 ≤ 𝑚 ≤ 10<sup>3</sup>

## Samples.
Sample 1.

    Input:
        4 4
        1 2
        4 1
        2 3
        3 1
    Output:
        1
    
        4   3
        ↓ ↙ ↑
        1 → 2
    This graph contains a cycle: 3 → 1 → 2 → 3.

Sample 2.

    Input:
        5 7
        1 2
        2 3
        1 3
        3 4
        1 4
        2 5
        3 5
    Output:
        0

        4 ← 3 → 5
         ↖ ↗ ↖ ↗
          1 → 2
    
    There is no cycle in this graph. This can be seen, for example, by noting that all edges in this graph go from a vertex with a smaller number to a vertex with a larger number.
    