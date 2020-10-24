#  Construct the Suffix Array of a Long String

## Description 
The goal in this problem is to construct the suffix array of a given string again, but this time for a longer string. In particular, a quadratic algorithm will not fit into the time limit in this problem. This will require you to implement an almost linear algorithm bringing you close to the state-of-the-art algorithms for constructing suffix arrays.

## Details
**Task**<br>
Construct the suffix array of a string.

**Input format**<br> 
A string Text ending with a “$” symbol.

**Output format:**<br> 
SuffixArray(Text), that is, the list of starting positions of sorted suffixes separated by spaces.

**Constraints:**<br>
1 ≤ |Text| ≤ 10<sup>5</sup> except the Last symbol<br>
Text contains symbols A, C, G, T only.

## Samples.
Sample 1.

    Input:
        AAA$
    Output:
        3 2 1 0
    
    Sorted suffixes:
        3 $
        2 A$
        1 AA$
        0 AAA$

Sample 2.

    Input:
        GAC$
    Output:
        3 1 2 0
    
    Sorted suffixes:
        3 $
        1 AC$
        2 C$
        0 GAC$

Sample 3.

    Input:
        GAGAGAGA$
    Output:
        8 7 5 3 1 6 4 2 0
    
    Sorted suffixes:
        8 $
        7 A$
        5 AGA$
        3 AGAGA$
        1 AGAGAGA$
        6 GA$
        4 GAGA$
        2 GAGAGA$
        0 GAGAGAGA$

Sample 4.

    Input:
        AACGATAGCGGTAGA$
    Output:
        15 14 0 1 12 6 4 2 8 13 3 7 9 10 11 5

    Sorted suffixes:
        15 $
        14 A$
        0 AACGATAGCGGTAGA$
        1 ACGATAGCGGTAGA$
        12 AGA$
        6 AGCGGTAGA$
        4 ATAGCGGTAGA$
        2 CGATAGCGGTAGA$
        8 CGGTAGA$
        13 GA$
        3 GATAGCGGTAGA$
        7 GCGGTAGA$
        9 GGTAGA$
        10 GTAGA$
        11 TAGA$
        5 TAGCGGTAGA$
    