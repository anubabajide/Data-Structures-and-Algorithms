# Closest Points

## Description 
In this problem, your goal is to find the closest pair of points among the given 𝑛 points. This is a basic primitive in computational geometry having applications in, for example, graphics, computer vision, traffic-control systems.


## Details
**Task**<br> 
Given 𝑛 points on a plane, find the smallest distance between a pair of two (different) points. Recall that the distance between points (𝑥1, 𝑦1) and (𝑥2, 𝑦2) is equal to √︀((𝑥<sub>1</sub> − 𝑥<sub>2</sub>) <sup>2</sup> + (𝑦<sub>1</sub> − 𝑦<sub>2</sub>) <sup>2</sup>).

**Input format**<br> 
The first line contains the number 𝑛 of points. Each of the following 𝑛 lines defines a point (𝑥𝑖, 𝑦𝑖).

**Output format:**<br> 
Output 𝑝 non-negative integers 𝑘<sub>0</sub>, 𝑘<sub>1</sub>, . . . , 𝑘<sub>𝑝−1sub> where 𝑘<sub>𝑖</sub> is the number of segments which contain 𝑥<sub>𝑖</sub>. More formally,<br>
<b>𝑘<sub>𝑖</sub> = |{𝑗 : 𝑎<sub>𝑗</sub> ≤ 𝑥<sub>𝑖</sub> ≤ 𝑏<sub>𝑗</sub>}| .</b>

**Constraints:**<br> 
2 ≤ 𝑛 ≤ 10<sup>5</sup>
; −10<sup>9</sup> ≤ 𝑥<sub>𝑖</sub>
, 𝑦<sub>𝑖</sub> ≤ 10<sup>9</sup> are integers.


## Samples.
Sample 1.

    Input:
        2
        0 0
        3 4
    Output:
        5.0

    There are only two points here. The distance between them is 5.

Sample 2.

    Input:
    4
    7 7
    1 100
    4 8
    7 7
    Output:
    0.0

    There are two coinciding points among the four given points. Thus, the minimum distance is zero.

Sample 3.

    Input:
    11
    4 4
    -2 -2
    -3 -4
    -1 3
    2 3
    -4 0
    1 1
    -1 -1
    3 -1
    -4 2
    -2 4
    Output:
    1.414213

    The smallest distance is √2. There are two pairs of points at this distance: (−1, −1) and (−2, −2); (−2, 4) and (−1, 3).

