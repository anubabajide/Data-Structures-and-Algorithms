# Construct the Suffix Tree from the Suffix Array

## Description 
As we’ve mentioned earlier, known algorithms for constructing suffix trees in linear time are quite complex.
It turns out, however, that one can first construct a suffix array in near-linear time (say, 𝑂(𝑛 log 𝑛)) and
then transform it into a suffix tree in linear time. This gives a near-linear time algorithm for constructing
a suffix tree!
SuffixTree(Text) can be constructed in linear time from SuffixArray(Text) by using the longest common
prefix (LCP) array of Text, LCP(Text), which stores the length of the longest common prefix shared by
consecutive lexicographically ordered suffixes of Text. For example,

    LCP(“panamabananas$”) = (0, 1, 1, 3, 3, 1, 0, 0, 0, 2, 2, 0, 0).


## Details
**Task**<br>
Construct a suffix tree from the suffix array and LCP array of a string

**Input format**<br> 
The first line contains a string Text ending with a “$” symbol, the second line contains
SuffixArray(Text) as a list of |Text| integers separated by spaces, the last line contains LCP(Text) as
a list of |Text| − 1 integers separated by spaces.

**Output format:**<br> 
The output format in this problem differs from the output format in the problem “Suffix
Tree” from the Programming Assignment 2 and is somewhat tricky. It is because this problem is
harder: the input string can be longer, so it would take too long to output all the edge labels directly
and compare them with the correct ones, as their combined length can be Θ(|Text|
2
), which is too
much when the Text can be as long as 200 000 characters.
Output the 𝑇 𝑒𝑥𝑡 from the input on the first line. Then output all the edges of the suffix tree in a
specific order (see below), each on its own line. Output each edge as a pair of integers (start, end),
where start is the position in Text corresponding to the start of the edge label substring in the Text
and end is the position right after the end of the edge label in the Text. Note that start must be a
valid position in the Text, that is, 0 ≤ 𝑠𝑡𝑎𝑟𝑡 ≤ |Text| − 1, and end must be between 1 and |Text|
inclusive. Substring Text[start..end − 1] must be equal to the edge label of the corresponding edge. For
example, if Text = “ACACAA$” and the edge label is “CA”, you can output this edge either as (1, 3)
corresponding to Text[1..2] = “CA” or as (3, 5) corresponding to Text[3..4] = “CA” — both variants
will be accepted.
The order of the edges is important here — if you output all the correct edges in the wrong order, your
solution will not be accepted. However, you don’t need to construct this order yourself if you
write in C++, Java or Python3, because it is implemented for you in the starter files.
Output all the edges in the order of sorted suffixes: first, take the leaf of the suffix tree corresponding
to the smallest suffix of Text and output all the edges on the path from the root to this leaf. Then
take the leaf corresponding to the second smallest suffix of Text and output all the edges on the path
9
from the root to this leaf except for those edges which were printed before. Then take the leaf
corresponding to the third smallest suffix, fourth smallest suffix and so on. Print each edge only once
— as a part of the path corresponding to the smallest suffix of Text where this edge appears. This way,
you will only output 𝑂(|Text|) integers. See the examples below for clarification.


**Constraints:**<br>
1 ≤ |Text(Text)| ≤ 2 . 10<sup>5</sup> except the last symbol<br>
Text contains symbols A, C, G, T only.

## Samples.
Sample 1.

    Input:
        A$
        1 0
        0
    Output:
        A$
        1 2
        0 2

|𝑖 |𝑆𝐴[𝑖] |𝐿𝐶𝑃[𝑖]| suffix|
|-|------|------|-------|
|0 |1 |0 |$|
|1 |0 | |A$| 

       $/ \A$
       1   0
     

Sample 2.
    
    Input:
        AAA$
        3 2 1 0
        0 1 2
    Output:
        AAA$
        3 4
        0 1
        3 4
        1 2
        3 4
        2 4

|𝑖 |𝑆𝐴[𝑖] |𝐿𝐶𝑃[𝑖]| suffix|
|-|------|------|-------|
|0 |3 |0 |$
|1 |2 |1 |A$
|2 |1 |2 |AA$
|3 |0 | |AAA$

          /\
         $  A
        /    \
       3     /\
            $  A
           /    \
          2     /\
               $  A$
              /    \
             1      0

Sample 3.

    Input:
        GTAGT$
        5 2 3 0 4 1
        0 0 2 0 1
    Output:
        GTAGT$
        5 6
        2 6
        3 5
        5 6
        2 6
        4 5
        5 6
        2 6
