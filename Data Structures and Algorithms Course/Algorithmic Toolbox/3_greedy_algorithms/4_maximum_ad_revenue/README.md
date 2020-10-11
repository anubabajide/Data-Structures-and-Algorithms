# Maximum Advertisment Revenue
**Description**
You have 𝑛 ads to place on a popular Internet page. For each ad, you know how much is the advertiser willing to pay for one click on this ad. You have set up 𝑛 slots on your page and estimated the expected number of clicks per day for each slot. Now, your goal is to distribute the ads among the slots to maximize the total revenue.

## Details
**Task.** 
. Given two sequences 𝑎1, 𝑎2, . . . , 𝑎𝑛 (𝑎𝑖 is the profit per click of the 𝑖-th ad) and 𝑏1, 𝑏2, . . . , 𝑏𝑛 (𝑏𝑖 is the average number of clicks per day of the 𝑖-th slot), we need to partition them into 𝑛 pairs (𝑎𝑖, 𝑏𝑗 ) such that the sum of their products is maximized.

**Input format:** 
The first line contains an integer 𝑛, the second one contains a sequence of integers
𝑎1, 𝑎2, . . . , 𝑎𝑛, the third one contains a sequence of integers 𝑏1, 𝑏2, . . . , 𝑏𝑛.

**Output format:** 
Output the maximum value of ∑︀<sub>𝑛<sub>𝑖=1</sub></sub>𝑎<sub>𝑖</sub>𝑐<sub>𝑖</sub>, where 𝑐1, 𝑐2, . . . , 𝑐𝑛 is a permutation of
𝑏1, 𝑏2, . . . , 𝑏𝑛.

**Constraints:** 
<br>1 ≤ 𝑛 ≤ 10<sup>3</sup> 
<br>−10<sup>5</sup> ≤ 𝑎𝑖, 𝑏𝑖 ≤ 10<sup>5</sup> 
<br>for all 1 ≤ 𝑖 ≤ 𝑛.



## Samples.
Sample 1.

    Input:
        1
        23
        39
    Output:
        897
        897 = 23 · 39.

Sample 2.

    Input:
        3
        1 3 -5
        -2 4 1
    Output:
        23
        23 = 3 · 4 + 1 · 1 + (−5) · (−2).
