# Compute Distance with Preprocessing on Large Road Networks

## Description 
In this task you will solve the classical logistics problem called Travelling Salesman Problem: you are given the location of a depot and the location of a list of stores on a road network, and you need to find the shortest path for a truck to start in the depot, visit each of the stores to deliver the goods there, and return back to the depot.

## Details
**Task**<br>
Compute the distance between several pairs of nodes in the network.

**Input format**<br> 
You will be given the input for this problem in two parts. The first part contains the description of a road network, the second part contains the queries. You have a separate time limit for preprocessing the graph. Under this time limit, you need to read the graph and preprocess it. After you’ve preprocessed the graph, you need to output the string “Ready” (without quotes) and flush the output buffer (the starter files for C++, Java and Python3 do that for you; if you use another language, you will have to find out how to do this). Only after you output the string “Ready” you will be given the queries. You will have a time limit for the querying part, and under this time limit you will needto input all the queries and output the results for each of the quires.<br><br>
The first line of the road network description contains two integers 𝑛 and 𝑚 — the number of nodes and edges in the network, respectively. The nodes are numbered from 1 to 𝑛. Each of the following 𝑚 lines contains three integers 𝑢, 𝑣 and 𝑙 describing a directed edge (𝑢, 𝑣) of length 𝑙 from the node number 𝑢 to the node number 𝑣.<br><br>
The first line of the queries description contains an integer 𝑞 — the number of queries for computing the distance. Each of the following 𝑞 lines starts with the integer 𝑘 — the number of points the truck must visit, including all the stores and the depot. There are 𝑘 more integers on the same line. The first of them is the number of the node corresponding to the depot location. The next 𝑘 −1 integers are the numbers of the nodes corresponding to the store locations.

**Output format:**<br> 
After you’ve read the description of the road network and done your preprocessing, output one string “Ready” (without quotes) on a separate line and flush the output buffer. Then read the queries, and for each query, output one integer on a separate line. If there is no path starting in depot, visiting each store at least once and returning to the depot, output −1. Otherwise, output the length of the shortest path starting at a depot, visiting each store at least once and returning to the depot.

**Constraints:**<br>
1 ≤ 𝑛 ≤ 110 000<br> 
1 ≤ 𝑚 ≤ 250 000<br> 
1 ≤ 𝑢, 𝑣 ≤ 𝑛<br> 
1 ≤ 𝑙 ≤ 100 000<br> 
1 ≤ 𝑞 ≤ 100<br> 
1 ≤ 𝑘 ≤ 20.<br>
It is guaranteed that all the answers are less than 1 000 000 000. <br>
**For Python2, Python3, Ruby and Javascript**,<br>
1 ≤ 𝑛 ≤ 11 000<br> 
1 ≤ 𝑚 ≤ 25 000<br> 
1 ≤ 𝑘 ≤ 20.

## Samples.
Sample 1.

    Input:
        4 5
        1 2 1
        2 3 1
        3 4 1
        4 1 1
        2 1 1
        3
        2 1 2
        2 1 3
        4 1 2 3 4
    Output:
        Ready
        2
        4
        4
    
    Explanation:
    For the first query, we need to start in the node 1, visit node 2 and return to node 1. The shortest path for that is to get directly from 1 to 2 and then directly back from 2 to 1. The length is 2. 
    
    For the second query, we need to start in the node 1, visit node 3 and return to node 1. A shortest path for that is to get from 1 to 2, then from 2 to 3, then return from 3 to 2, then return from 2 to 1. Another shortest path would be to go from 1 to 2, then from 2 to 3, then from 3 to 4, then from 4 to 1. The length is 4. 
    
    For the third query, we need to start in the node 1, visit all the other nodes and return to node 1. The shortest path for that is to go from 1 to 2, then from 2 to 3, then from 3 to 4, then from 4 to 1. The length is 4.
