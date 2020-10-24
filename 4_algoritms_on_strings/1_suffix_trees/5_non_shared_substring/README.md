# Shortest Non-Shared Substring of Two Strings

## Description 
Find the shortest substring of one string that does not appear in another string.

## Details
**Input format**<br> 
Strings Text<sub>1</sub> and Text<sub>2</sub>.

**Output format:**<br> 
The shortest (non-empty) substring of Text1 that does not appear in Text2. (Multiple solutions may exist, in which case you may return any one.)

**Constraints:**<br>
1 ≤ |Text1|, |Text2| ≤ 2 000<br> 
strings have equal length (|Text1| = |Text2|), are not equal (Text1 ̸= Text2), and contain symbols A, C, G, T only.

## Samples.
Sample 1.

    Input:
        A
        T
    Output:
        A

    Text2 does not contain the string A, hence it is clearly a shortest such string.

Sample 2.

    Input:
        AAAAAAAAAAAAAAAAAAAA
        TTTTTTTTTTTTTTTTTTTT
    Output:
        A

    Again, Text2 does not contain the string A, so it is a shortest one.

Sample 3.

    Input:
        CCAAGCTGCTAGAGG
        CATGCTGGGCTGGCT
    Output:
        AA

    In this case, Text2 contains all symbols A, C, G, T, that is, all substrings of Text1 of length 1. At the same time, Text2 does not contain AA, hence it is a shortest substring of Text1 that does not appear in Text2.

Sample 4.

    Input:
        ATGCGATGACCTGACTGA
        CTCAACGTATTGGCCAGA
    Output:
        ATG
    
    The string ATG is a substring of Text1 and it does not appear in Text2. At the same time, Text2 contains all 16 strings of length 2 and all 4 strings of length 1.
