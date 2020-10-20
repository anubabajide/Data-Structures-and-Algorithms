#  Detecting Anomalies in Currency Exchange Rates

## Description 
You are given a list of currencies 𝑐<sub>1</sub>, 𝑐<sub>2</sub>, . . . , 𝑐<sub>*n*</sub> together with a list of exchange rates: 𝑟<sub>𝑖𝑗</sub> is the number of units of currency 𝑐<sub>𝑗</sub> that one gets for one unit of 𝑐<sub>𝑖</sub> . You would like to check whether it is possible to start with one unit of some currency, perform a sequence of exchanges, and get more than one unit of the same currency. In other words, you would like to find currencies 𝑐<sub>𝑖1</sub> , 𝑐<sub>𝑖2</sub> , . . . , 𝑐<sub>𝑖𝑘</sub> such that 𝑟<sub>𝑖1,𝑖2</sub> · 𝑟<sub>𝑖2,𝑖3</sub> · 𝑟<sub>𝑖𝑘−1,𝑖𝑘</sub> , 𝑟<sub>𝑖𝑘,𝑖1</sub> > 1. For this, you construct the following graph: vertices are currencies 𝑐<sub>1</sub>, 𝑐<sub>2</sub>, . . . , 𝑐<sub>*n*</sub>, the weight of an edge from 𝑐<sub>𝑖</sub> to 𝑐<sub>𝑗</sub> is equal to − log 𝑟<sub>𝑖𝑗</sub> . There it suffices to check whether is a negative cycle in this graph. Indeed, assume that a cycle 𝑐<sub>𝑖</sub> → 𝑐<sub>𝑗</sub> → 𝑐<sub>𝑘</sub> → 𝑐<sub>𝑖</sub> has negative weight. This means that −(log 𝑐<sub>𝑖𝑗</sub> + log 𝑐<sub>𝑗𝑘</sub> + log 𝑐<sub>𝑘𝑖</sub>) < 0 and hence log 𝑐<sub>𝑖𝑗</sub> + log 𝑐<sub>𝑗𝑘</sub> + log 𝑐<sub>𝑘𝑖</sub> > 0. This, in turn, means that 𝑟<sub>𝑖𝑗</sub> 𝑟<sub>𝑗𝑘</sub>𝑟<sub>𝑘𝑖</sub> = 2<sup>log 𝑐<sub>𝑖𝑗</sub></sup> 2<sup>log 𝑐<sub>𝑗𝑘</sub></sup> 2<sup>log 𝑐<sub>𝑘𝑖</sub></sup> = 2<sup>log 𝑐<sub>𝑖𝑗</sub>+log 𝑐<sub>𝑗𝑘</sub>+log 𝑐<sub>𝑘𝑖</sub></sup> > 1 .

## Details
**Task**<br>
Given an directed graph with possibly negative edge weights and with 𝑛 vertices and 𝑚 edges, check whether it contains a cycle of negative weight.

**Input format**<br> 
A graph is given in the standard format.

**Output format:**<br> 
Output 1 if the graph contains a cycle of negative weight and 0 otherwise.

**Constraints:**<br>
1 ≤ 𝑛 ≤ 10<sup>3</sup><br>
0 ≤ 𝑚 ≤ 10<sup>4</sup><br>
Edge weights are absolute valued integers not
exceeding 10<sup>3</sup>

## Samples.
Sample 1.

    Input:
        4 4
        1 2 -5
        4 1 2
        2 3 2
        3 1 1
    Output:
        1

        4    3
        ↓ 1 ↙↑
       2↓ ↙  ↑2
        1 →→ 2
          -5
    The weight of the cycle 1 → 2 → 3 is equal to −2, that is, negative.