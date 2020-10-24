# Generalized Multiple Pattern Matching

## Description 
The goal in this problem is to extend the solution for the previous problem such that it will be able to handle cases when one of the patterns is a prefix of another pattern. In this case, some patterns are spelled in a trie by traversing a path from the root to an internal vertex, but not to a leaf.


## Details
**Input format**<br> 
The first line of the input contains a string Text, the second line contains an integer 𝑛, each of the following 𝑛 lines contains a pattern from Patterns = {𝑝1, . . . , 𝑝𝑛}.


**Output format:**<br> 
All starting positions in Text where a string from Patterns appears as a substring in increasing order (assuming that Text is a 0-based array of symbols). **If more than one pattern appears starting at position 𝑖, output 𝑖 once.**

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
        ACATA
        3
        AT
        A
        AG
    Output:
        0 2 4
    
    Text contains occurrences of A at positions 0, 2, and 4, as well as an occurrence of AT at position 2. 
    Note that the trie looks as follows in this case:
        |
        A
        |
       / \
      T   G
     /     \
    When spelling Text from position 0, we don’t reach a leaf. Still, there is an occurrence of the pattern A at this position.
    