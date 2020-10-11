# Greatest Commmon Divisor

## Description
The greatest common divisor GCD(𝑎, 𝑏) of two non-negative integers 𝑎 and 𝑏
(which are not both equal to 0) is the greatest integer 𝑑 that divides both 𝑎 and 𝑏.
Your goal in this problem is to implement the Euclidean algorithm for computing
the greatest common divisor.
Efficient algorithm for computing the greatest common divisor is an important
basic primitive of commonly used cryptographic algorithms like RSA.

    GCD(1344, 217)
    = GCD(217, 42)
    = GCD(42, 7)
    = GCD(7, 0)
    =7


## Details
**Task.** 
Given two integers 𝑎 and 𝑏, find their greatest common divisor

**Input format:** 
The two integers 𝑎, 𝑏 are given in the same line separated by space.

**Output format:** 
Output GCD(𝑎, 𝑏).

**Constraints:** 
1 ≤ 𝑎, 𝑏 ≤ 2 · 10<sup>9</sup>

## Samples.
Sample 1.

    Input:
        18 35
    Output:
        1
    
    18 and 35 do not have common non-trivial divisors.

Sample 2.
    
    Input:
        28851538 1183019
    Output:
        17657
    
    28851538 = 17657 · 1634, 1183019 = 17657 · 67
