# Multiple Pattern Matching

## Description 
Another problem that can be solved efficiently with tries is the following


## Details
**Task**<br>
Find all occurrences of a collection of patterns in a text.

**Input format**<br> 
The first line of the input contains a string Text, the second line contains an integer 𝑛, each of the following 𝑛 lines contains a pattern from Patterns = {𝑝1, . . . , 𝑝𝑛}.


**Output format:**<br> 
All starting positions in Text where a string from Patterns appears as a substring in increasing order (assuming that Text is a 0-based array of symbols).

**Constraints:**<br>
1 ≤ |Text| ≤ 10 000<br> 
1 ≤ 𝑛 ≤ 5 000<br> 
1 ≤ |𝑝<sub>𝑖</sub>| ≤ 100 for all 1 ≤ 𝑖 ≤ 𝑛<br> 
all strings contain only symbols A, C, G, T<br> 
no 𝑝<sub>𝑖</sub> is a prefix of 𝑝<sub>𝑗</sub> for all 1 ≤ 𝑖 ̸= 𝑗 ≤ 𝑛.


## Samples.
Sample 1.

    Input:
        AAA
        1
        AA
    Output:
        0 1

    The pattern AA appears at positions 0 and 1. Note that these two occurrences of the pattern overlap.

Sample 2.

    Input:
        AA
        1
        T
    Output:
        There are no occurrences of the pattern in the text.

Sample 3.

    Input:
        AATCGGGTTCAATCGGGGT
        2
        ATCG
        GGGT
    Output:
        1 4 11 15
    
    The pattern ATCG appears at positions 1 and 11, the pattern GGGT appears at positions 4 and 15.
