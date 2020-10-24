# Money Change
## Description
A thief finds much more loot than his bag can fit. Help him to find the most valuable combination of items assuming that any fraction of a loot item can be put into his bag.


## Details
**Task.**<br> 
The goal of this code problem is to implement an algorithm for the fractional knapsack problem

**Input format** <br>
The first line of the input contains the number 𝑛 of items and the capacity 𝑊 of a knapsack. The next 𝑛 lines define the values and weights of the items. The 𝑖-th line contains integers 𝑣<sub>𝑖</sub> and 𝑤<sub>𝑖</sub> — the value and the weight of 𝑖-th item, respectively.


**Output format** <br>
Output the maximal value of fractions of items that fit into the knapsack. The absolute value of the difference between the answer of your program and the optimal value should be at most 10<sup>-3</sup>. To ensure this, output your answer with at least four digits after the decimal point 

**Constraints** <br>
1 ≤ 𝑛 ≤ 10<sup>3</sup> 
<br>0 ≤ 𝑊 ≤ 2 · 10<sup>6</sup>
<br>0 ≤ 𝑣<sub>𝑖</sub> ≤ 2 · 10<sup>6</sup> 
<br>0 < 𝑤<sub>𝑖</sub> ≤ 2 · 10<sup>6</sup>
<br>for all 1 ≤ 𝑖 ≤ 𝑛. 
<br>All the numbers are integers.

## Samples.
Sample 1.

    Input:
        3 50
        60 20
        100 50
        120 30
    Output:
        180.0000
    
    To achieve the value 180, we take the first item and the third item into the bag.

Sample 2.

    Input:
        1 10
        500 30
    Output:
        166.6667
    
    Here, we just take one third of the only available item.
