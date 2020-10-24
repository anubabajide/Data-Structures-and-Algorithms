# Construct the Suffix Array of a String

## Description 
We saw that suffix trees can be too memory intensive to apply in practice. This becomes a serious issue for the case of massive datasets like the ones arising in bioinformatics. In 1993, Udi Manber and Gene Myers introduced suffix arrays as a memory-efficient alternative to suffix trees. To construct SuffixArray(Text), we first sort all suffixes of Text lexicographically, assuming that “$” comes first in the alphabet. The suffix array is the list of starting positions of these sorted suffixes. For example,

    SuffixArray(“panamabananas$”) = (13, 5, 3, 1, 7, 9, 11, 6, 4, 2, 8, 10, 0, 12)

E.g., the suffix tree of a human genome requires about 60 Gb, while the suffix array occupies around 12 Gb.


## Details
**Task**<br>
Construct the suffix array of a string.

**Input format**<br> 
A string Text ending with a “$” symbol.

**Output format:**<br> 
SuffixArray(Text), that is, the list of starting positions (0-based) of sorted suffixes separated by spaces.

**Constraints:**<br>
1 ≤ |Text| ≤ 10<sup>4</sup> except for the last symbol, Text contains symbols A, C, G, T only.


## Samples.
Sample 1.

    Input:
        GAC$
    Output:
        3 1 2 0
    
    Sorted suffixes:
        3 $
        1 AC$
        2 C$
        0 GAC$

Sample 2.

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

Sample 3.

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
    