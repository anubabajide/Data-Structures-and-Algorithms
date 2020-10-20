# Compute Distance with Preprocessing on Large Road Networks

## Description 
In this task you will be first given a graph of a real road network, and you can preprocess it as you wish under the preprocessing time limit. Then you will get a set of queries for computing distance, and you will need to answer all of them under the separate time limit for queries. You will have to respond to queries much faster than in the previous problem

## Details
**Task**<br>
Compute the distance between several pairs of nodes in the network.

**Input format**<br> 
You will be given the input for this problem in two parts. The first part contains the description of a road network, the second part contains the queries. You have a separate time limit for preprocessing the graph. Under this time limit, you need to read the graph and preprocess it. After you’ve preprocessed the graph, you need to output the string “Ready” (without quotes) and flush the output buffer (the starter files for C++, Java and Python3 do that for you; if you use another language, you will have to find out how to do this). Only after you output the string “Ready” you will be given the queries. You will have a time limit for the querying part, and under this time limit you will need to input all the queries and output the results for each of the quires. The first line of the road network description contains two integers 𝑛 and 𝑚 — the number of nodes and edges in the network, respectively. The nodes are numbered from 1 to 𝑛. Each of the following 𝑚 lines contains three integers 𝑢, 𝑣 and 𝑙 describing a directed edge (𝑢, 𝑣) of length 𝑙 from the node number 𝑢 to the node number 𝑣.<br><br>
The first line of the queries description contains an integer 𝑞 — the number of queries for computing the distance. Each of the following 𝑞 lines contains two integers 𝑢 and 𝑣 — the numbers of the two nodes to compute the distance from 𝑢 to 𝑣.

**Output format:**<br> 
After you’ve read the description of the road network and done your preprocessing, output one string “Ready” (without quotes) on a separate line and flush the output buffer. Then read the queries, and for each query, output one integer on a separate line. If there is no path from 𝑢 to 𝑣, output −1. Otherwise, output the distance from 𝑢 to 𝑣.

**Constraints:**<br>
1 ≤ 𝑛 ≤ 500 000<br> 
1 ≤ 𝑚 ≤ 1 100 000<br> 
1 ≤ 𝑢, 𝑣 ≤ 𝑛<br> 
1 ≤ 𝑙 ≤ 200 000<br> 
1 ≤ 𝑞 ≤ 10 000<br> 
It is guaranteed that the correct distances are less than 1 000 000 000.<br> 
**For Python2, Python3, Ruby and Javascript**, <br>
1 ≤ 𝑛 ≤ 11 000<br> 
1 ≤ 𝑚 ≤ 25 000<br> 
1 ≤ 𝑞 ≤ 1 000.

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
        Ready
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
        Ready
        3
    
    Explanation:
    There is a direct edge from node 1 to node 3 of length 5, but there is a shorter path 1 → 2 → 3 of length 1 + 2 = 3.
