# Find Pattern in Text

## Description 
In this problem, your goal is to implement the Rabin–Karp’s algorithm.

## Details
**Task**<br>
In this problem your goal is to implement the Rabin–Karp’s algorithm for searching the given pattern in the given text.

**Input format**<br> 
There are two strings in the input: the pattern 𝑃 and the text 𝑇.

**Output format:**<br> 
Print all the positions of the occurrences of 𝑃 in 𝑇 in the ascending order. Use 0-based indexing of positions in the the text 𝑇.

**Constraints:**<br>
1 ≤ |𝑃| ≤ |𝑇| ≤ 5 · 10<sup>5</sup> <br>
The total length of all occurrences of 𝑃 in 𝑇 doesn’t exceed 10<sup>8</sup>. The pattern and the text contain only latin letters.



## Samples.
Sample 1.

    Input:
        aba
        abacaba
    Output:
        0 4
    
    Explanation:
    The pattern 𝑎𝑏𝑎 can be found in positions 0 (abacaba) and 4 (abacaba) of the text 𝑎𝑏𝑎𝑐𝑎𝑏𝑎.

Sample 2.
    
    Input:
        Test
        testTesttesT
    Output:
        4

    Explanation:
    Pattern and text are case-sensitive in this problem. Pattern 𝑇 𝑒𝑠𝑡 can only be found in position 4 in
    the text 𝑡𝑒𝑠𝑡𝑇 𝑒𝑠𝑡𝑡𝑒𝑠𝑇.

Sample 3.

    Input:
        aaaaa
        baaaaaaa
    Output:
        1 2 3
    
    Note that the occurrences of the pattern in the text can be overlapping, and that’s ok, you still need
    to output all of them.
