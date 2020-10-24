# Find All Occurrences of a Pattern in a String

## Description 
In this problem, we ask a simple question: how many times one string occurs as a substring of another? Recall that different occurrences of a substring can overlap with each other. For example, ATA occurs three times in CGATATATCCATAG. This is a classical pattern matching problem in Computer Science solved millions times per day all over the world when computer users use the common “Find” feature in text/code editors and Internet browsers.

## Details
**Task**<br>
Find all occurrences of a pattern in a string.

**Input format**<br> 
Strings Pattern and Genome.

**Output format:**<br> 
All starting positions in Genome where Pattern appears as a substring (using 0-based indexing as usual).

**Constraints:**<br>
1 ≤ |Pattern| ≤ 10<sup>6</sup><br>
1 ≤ |Genome| ≤ 10<sup>6</sup><br>
; both strings are over A, C, G, T.


## Samples.
Sample 1.

    Input:
        TACG
        GT
    Output:


    The pattern is longer than the text and hence has no occurrences in the text.

Sample 2.

    Input:
        ATA
        ATATA
    Output:
        0 2
    
    The pattern appears at positions 1 and 3 (and these two occurrences overlap each other).

Sample 3.

    Input:
        ATAT
        GATATATGCATATACTT
    Output:
        1 3 9
    
    The pattern appears at positions 1, 3, and 9 in the text.
    