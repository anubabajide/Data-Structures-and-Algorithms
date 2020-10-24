# Pattern Matching with the Suffix Array

## Description 
In this problem, we will let you use the suffix array to solve the Multiple Pattern Matching Problem. This
is what actually happens when one needs to solve the pattern matching problem for a massive string like
the human genome: instead of downloading the genome itself, one downloads its suffix array and solves the
pattern matching problem using the array.


## Details
**Task**<br>
Find all occurrences of a given collection of patterns in a string.

**Input format**<br> 
The first line contains a string Text. The second line specifies an integer 𝑛. The last line
gives a collection of 𝑛 strings Patterns = {𝑝1, . . . , 𝑝𝑛} separated by spaces.

**Output format:**<br> 
All starting positions (in any order) in Text where a pattern appears as a substring (using 0-based indexing as usual). If several patterns occur at the same position of the Text, still output this
position only once.

**Constraints:**<br>
All strings contains symbols A, C, G, T only.<br>
1 ≤ |Text| ≤ 10<sup>5</sup> <br>
1 ≤ n ≤ 10<sup>4</sup><br>
∑︀<sup>𝑛</sup><sub>𝑖=1</sub> |𝑝𝑖| ≤ 10<sup>5</sup>

## Samples.
Sample 1.

    Input:
        AAA
        1
        A
    Output:
        0 1 2
    
    The pattern A appears at positions 0, 1, and 2 in the text.

Sample 2.

    Input:
        ATA
        3
        C G C
    Output:


    There are no occurrences of the patterns in the text

Sample 3.

    Input:
        ATATATA
        3
        ATA C TATAT
    Output:
        4 2 0 1
    
    The pattern ATA appears at positions 0, 2, and 4, the pattern TATAT appears at position 1.
