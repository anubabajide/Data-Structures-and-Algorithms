# Substring Equality

## Description 
In this problem, you will use hashing to design an algorithm that is able to preprocess a given string 𝑠 to answer any query of the form “are these two substrings of 𝑠 equal?” efficiently. This, in turn, is a basic building block in many string processing algorithms.

## Details
**Input format**<br> 
The first line contains a string 𝑠 consisting of small Latin letters. The second line contains the number of queries 𝑞. Each of the next 𝑞 lines specifies a query by three integers 𝑎, 𝑏, and 𝑙.

**Output format:**<br> 
For each query, output “Yes” if 𝑠𝑎𝑠𝑎+1. . .𝑠𝑎+𝑙−1 = 𝑠𝑏𝑠𝑏+1. . .𝑠𝑏+𝑙−1 are equal, and “No” otherwise.

**Constraints:**<br>
1 ≤ |𝑠| ≤ 500 000<br> 
1 ≤ 𝑞 ≤ 100 000 <br> 
0 ≤ 𝑎, 𝑏 ≤ |𝑠| − 𝑙 (hence the indices 𝑎 and 𝑏 are 0-based).


## Samples.
Sample 1.

    Input:
        trololo
        4
        0 0 7
        2 4 3
        3 5 1
        1 3 2
    Output:
        Yes
        Yes
        Yes
        No
    
0 0 7 → **trololo** = **trololo**<br>
2 4 3 → tr**olo**lo = trol**olo**<br>
3 5 1 → tro**l**olo = trolo**l**o<br>
1 3 2 → t**ro**lolo ̸= tro**lo**lo<br>
