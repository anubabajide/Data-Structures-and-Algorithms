# Clustering

## Description 
Clustering is a fundamental problem in data mining. The goal is to partition a given set of objects into subsets (or clusters) in such a way that any two objects from the same subset are close (or similar) to each other, while any two objects from different subsets are far apart.

## Details
**Task**<br>
Given 𝑛 points on a plane and an integer 𝑘, compute the largest possible value of 𝑑 such that the given points can be partitioned into 𝑘 non-empty subsets in such a way that the distance between any two points from different subsets is at least 𝑑.

**Input format**<br> 
The first line contains the number 𝑛 of points. Each of the following 𝑛 lines defines a point (𝑥𝑖, 𝑦𝑖). The last line contains the number 𝑘 of clusters.

**Output format:**<br> 
Output the minimum total length of segments. The absolute value of the difference between the answer of your program and the optimal value should be at most 10<sup>−6</sup> . To ensure this, output your answer with at least seven digits after the decimal point (otherwise your answer, while being computed correctly, can turn out to be wrong because of rounding issues).

**Constraints:**<br>
2 ≤ 𝑘 ≤ 𝑛 ≤ 200<br> 
−10<sup>3</sup> ≤ 𝑥𝑖, 𝑦𝑖 ≤ 10<sup>3</sup> are integers. <br>
All points are pairwise different

## Samples.
Sample 1.

    Input:
        12
        7 6
        4 3
        5 1
        1 7
        2 7
        5 7
        3 3
        7 8
        2 8
        4 4
        6 7
        2 6
        3
    Output:
        2.828427124746

Sample 2.

    Input:
        8
        3 1
        1 2
        4 6
        9 8
        9 9
        8 9
        3 11
        4 12
        4
    Output:
        5.000000000
