# Friend Suggestion

## Description 
Social networks are live on the connections between people, so friend suggestions is one of the most important features of Facebook. One of the most important inputs of the algorithm for friend suggestion is most probably the current distance between you and the suggested person in the graph of friends connections. Your task is to implement efficient computation of this distance. The grader will test your algorithm against different real-world networks, such as a part of internet, a network of scientific citations or coauthorship, a social network of jazz musicians or even a social network of dolphins :) You need to compute the distance between two nodes in such network.

## Details
**Task**<br>
Compute the distance between several pairs of nodes in the network using Bi-directional Dijkstra.

**Input format**<br> 
The first line contains two integers 𝑛 and 𝑚 — the number of nodes and edges in the network, respectively. The nodes are numbered from 1 to 𝑛. Each of the following 𝑚 lines contains three integers 𝑢, 𝑣 and 𝑙 describing a directed edge (𝑢, 𝑣) of length 𝑙 from the node number 𝑢to the node number 𝑣. (Note that some social networks are represented by directed graphs while some other correspond naturally to undirected graphs. For example, Twitter is a directed graph (with a directed edge (𝑢, 𝑣) meaning that 𝑢 follows 𝑣), while Facebook is an undirected graph (where an undirected edge {𝑢, 𝑣} means that 𝑢 and 𝑣 are friends). In this problem, we work with directed graphs only for a simple reason. It is easy to turn an undirected graph into a directed one: just replace each undirected edge {𝑢, 𝑣} with a pair of directed edges (𝑢, 𝑣) and (𝑣, 𝑢).) The next line contains an integer 𝑞 — the number of queries for computing the distance. Each of the following 𝑞 lines contains two integers 𝑢 and 𝑣 — the numbers of the two nodes to compute the distance from 𝑢 to 𝑣.

**Output format:**<br> 
For each query, output one integer on a separate line. If there is no path from 𝑢 to 𝑣, output −1. Otherwise, output the distance from 𝑢 to 𝑣.

**Constraints:**<br>
1 ≤ 𝑛 ≤ 1 000 000<br> 
1 ≤ 𝑚 ≤ 2 000 000<br>
1 ≤ 𝑢, 𝑣 ≤ 𝑛<br> 
1 ≤ 𝑙 ≤ 1 000<br> 
1 ≤ 𝑞 ≤ 1 000.<br> 
**For Python2, Python3, Ruby and Javascript**,<br> 
1 ≤ 𝑚 ≤ 2 000 000.

## Samples.
Sample 1.
    
    Input:
        2 1
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
        1 2 1
        4 1 2
        2 3 2
        1 3 5
        1
        1 3
    Output:
        3
    
    Explanation:
    There is a direct edge from node 1 to node 3 of length 5, but there is a shorter path 1 → 2 → 3 of length 1 + 2 = 3.
