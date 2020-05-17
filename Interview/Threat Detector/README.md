Threat Detector
1. Problem: Given a Sequence of Strings, Check for Palindromes greater than length 2 and return the score of the threat of a string. The score of a palindrome is it's length, and the score of the threat is the sum of the scores of all palindromes in the string.
2. Solution: Using two moving pointers to get length of the longest palindrome with it's centre at a point. 
Repeat this step for every point in the string.
Repeat this process for every string in the sequence.
3. Complexity: 
N - number of strings in sequence
M - Average length of strings in sequence
K - Average length of All Palindromes
Time - O(NMK)
Only Pointers are used, hence.
Space - O(1)