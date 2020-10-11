# Car Fueling
**Description**
You are going to travel to another city that is located 𝑑 miles away from your home city. Your car can travel at most 𝑚 miles on a full tank and you start with a full tank. Along your way, there are gas stations at distances stop 1, stop 2, . . . ,stop 𝑛 from your home city. What is the minimum number of refills needed?

## Details
**Task.** 
The goal of this code problem is to implement an algorithm for the fractional knapsack problem

**Input format:** 
The first line contains an integer 𝑑. The second line contains an integer 𝑚. The third line specifies an integer 𝑛. Finally, the last line contains integers stop 1
,stop 2 , . . . ,stop 𝑛.

**Output format:** 
Assuming that the distance between the cities is 𝑑 miles, a car can travel at most 𝑚 miles on a full tank, and there are gas stations at distances stop 1
,stop 2, . . . ,stop 𝑛 along the way, output the minimum number of refills needed. Assume that the car starts with a full tank. If it is not possible to reach the destination, output −1.

**Constraints:** 
<br>1 ≤ 𝑑 ≤ 10<sup>5</sup> 
<br>1 ≤ 𝑚 ≤ 400 
<br>1 ≤ 𝑛 ≤ 300 
<br>0 < stop 1 < stop 2 < · · · < stop 𝑛 < 𝑑.


## Samples.
Sample 1.

    Input:
        950
        400
        4
        200 375 550 750
    Output:
        2
    
    The distance between the cities is 950, the car can travel at most 400 miles on a full tank. It suffices to make two refills: at points 375 and 750. This is the minimum number of refills as with a single refill one would only be able to travel at most 800 miles.

Sample 2.

    Input:
        10
        3
        4
        1 2 5 9
    Output:
        -1

    One cannot reach the gas station at point 9 as the previous gas station is too far away. 

Sample 3.

    Input:
        200
        250
        2
        100
        150
    Output:
        0
    
    There is no need to refill the tank as the car starts with a full tank and can travel for 250 miles whereas the distance to the destination point is 200 miles.
