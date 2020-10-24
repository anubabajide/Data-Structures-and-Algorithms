# Maximum Salary
## Description
As the last question of a successful interview, your boss gives you a few pieces of paper with numbers on it and asks you to compose a largest number from these numbers. The resulting number is going to be your salary, so you are very much interested in maximizing this number. How can you do this?



## Details
**Task** <br>
Compose the largest number out of a set of integers.


**Input format** <br>
The first line of the input contains an integer 𝑛. The second line contains integers 𝑎1, 𝑎2, . . . , 𝑎𝑛.


**Output format** <br>
Output the largest number that can be composed out of 𝑎1, 𝑎2, . . . , 𝑎𝑛.


**Constraints** <br>
1 ≤ 𝑛 ≤ 100 
<br>0 ≤ 𝑎𝑖 ≤ 10<sup>3</sup> 
<br>for all 1 ≤ 𝑖 ≤ 𝑛.



## Samples.
Sample 1.

    Input:
        2
        21 2
    Output:
        221
    
    Note that in this case the above algorithm also returns an incorrect answer 212.

Sample 2.
    
    Input:
        5
        9 4 6 1 9
    Output:
        99641

    In this case, the input consists of single-digit numbers only, so the algorithm above computes the right answer.

Sample 3.

    Input:
        3
        23 39 92
    Output:
        923923

    As a coincidence, for this input the above algorithm produces the right result, though the input does not have any single-digit numbers
