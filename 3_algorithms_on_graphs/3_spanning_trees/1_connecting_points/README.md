#  Building Roads to Connect Cities

## Description 
In this problem, the goal is to build roads between some pairs of the
given cities such that there is a path between any two cities and the
total length of the roads is minimized.

## Details
**Task**<br>
Given 𝑛 points on a plane, connect them with segments of minimum total length such that there is a path between any two points. Recall that the length of a segment with endpoints (𝑥<sub>1</sub>, 𝑦<sub>1</sub>) and (𝑥<sub>2</sub>, 𝑦<sub>2</sub>)
is equal to √︀<sub>(𝑥<sub>1</sub> − 𝑥<sub>2</sub>)<sup>2</sup> + (𝑦<sub>1</sub> − 𝑦<sub>2</sub>)<sup>2</sup>.</sub>

**Input format**<br> 
The first line contains the number 𝑛 of points. Each of the following 𝑛 lines defines a point (𝑥<sub>𝑖</sub>, 𝑦<sub>𝑖</sub>)

**Output format:**<br> 
Output the minimum total length of segments. The absolute value of the difference between the answer of your program and the optimal value should be at most 10<sup>−6</sup> . To ensure this, output your answer with at least seven digits after the decimal point (otherwise your answer, while being computed correctly, can turn out to be wrong because of rounding issues).

**Constraints:**<br>
1 ≤ 𝑛 ≤ 200<br> 
−10<sup>3</sup> ≤ 𝑥𝑖, 𝑦𝑖 ≤ 10<sup>3</sup> are integers.<br> 
All points are pairwise different, no three points lie on the same line.

## Samples.
Sample 1.

    Input:
        4
        0 0
        0 1
        1 0
        1 1
    Output:
        3.000000000

Sample 2.

    Input:
        5
        0 0
        0 2
        1 1
        3 0
        3 2
    Output:
        7.064495102
