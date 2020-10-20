# Compute Distance Faster Using Coordinates

## Description 
In this task you will be given a description of a real-world road network with not just edges and their lengths, but also with the coordinates of the nodes. Your task is still to find the distance between some pairs of nodes, but you will need to use the additional information about coordinates to speedup your search.

## Details
**Task**<br>
Compute the distance between several pairs of nodes in the network using the A* algorithm.

**Input format**<br> 
The first line contains two integers 𝑛 and 𝑚 — the number of nodes and edges in the network, respectively. The nodes are numbered from 1 to 𝑛. Each of the following 𝑛 lines contains the coordinates 𝑥 and 𝑦 of the corresponding node. Each of the following 𝑚 lines contains three integers 𝑢, 𝑣 and 𝑙 describing a directed edge (𝑢, 𝑣) of length 𝑙 from the node number 𝑢 to the node number 𝑣. It is guaranteed that 𝑙 ≥ √︀ <sub>(𝑥(𝑢) − 𝑥(𝑣))<sup>2</sup> + (𝑦(𝑢) − 𝑦(𝑣))<sup>2</sup></sub> where (𝑥(𝑢), 𝑦(𝑢)) are the coordinates of 𝑢 and (𝑥(𝑣), 𝑦(𝑣)) are the coordinates of 𝑣. The next line contains an integer 𝑞 — the number of queries for computing the distance. Each of the following 𝑞 lines contains two integers 𝑢 and 𝑣 — the numbers of the two nodes to compute the distance from 𝑢 to 𝑣.


**Output format:**<br> 
For each query, output one integer. If there is no path from 𝑢 to 𝑣, output −1. Otherwise, output the distance from 𝑢 to 𝑣.

**Constraints:**<br>
1 ≤ 𝑛 ≤ 110 000<br> 
1 ≤ 𝑚 ≤ 250 000<br>
−10<sup>9</sup> ≤ 𝑥, 𝑦 ≤ 10<sup>9</sup><br>
1 ≤ 𝑢, 𝑣 ≤ 𝑛<br>
0 ≤ 𝑙 ≤ 100 000<br>
1 ≤ 𝑞 ≤ 10 000.<br> 
**For Python2, Python3, Ruby and Javascript**, 1 ≤ 𝑛 ≤ 11 000, 1 ≤ 𝑚 ≤ 30 000.

## Samples.
Sample 1.

    Input:
        2 1
        0 0
        0 1
        1 2 1
        4
        1 1
        2 2
        1 2
        2 1
    Output:
        0
        0
        1
        -1

    Explanation:
    The distance from a node to itself is always 0. The distance from 1 to 2 is 1, and there is no path from 2 to 1.

Sample 2.

    Input:
        4 4
        0 0
        0 1
        2 1
        2 0
        1 2 1
        4 1 2
        2 3 2
        1 3 6
        1
        1 3
    Output:
        3

    Explanation:
    There is a direct edge from node 1 to node 3 of length 6, but there is a shorter path 1 → 2 → 3 of length 1 + 2 = 3.
