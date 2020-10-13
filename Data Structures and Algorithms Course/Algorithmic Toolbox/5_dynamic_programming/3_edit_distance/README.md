# Edit Distance

## Description 
The edit distance between two strings is the minimum number of operations (insertions, deletions, and substitutions of symbols) to transform one string into another. It is a measure of similarity of two strings. Edit distance has applications, for example, in computational biology, natural language processing, and spell checking. Your goal in this problem is to compute the edit distance between two strings.

## Details
**Task**<br>
The goal of this problem is to implement the algorithm for computing the edit distance between two strings.

**Input format**<br> 
Each of the two lines of the input contains a string consisting of lower case latin letters.

**Output format:**<br> 
Output the edit distance between the given two strings.

**Constraints:**<br> 
The length of both strings is at least 1 and at most 100.

## Samples.
Sample 1.

    Input:
        ab
        ab
    Output:
       0

Sample 2.

    Input:
        short
        ports
    Output:
        3
    
    An alignment of total cost 3:

|   |   |   |   |   |   |
|---|---|---|---|---|---|    
| s | h | o | r | t | − |
| − | p | o | r | t | s |

Sample 3.

    Input:
        editing
        distance
    Output:
        5
    
    An alignment of total cost 5:

|   |   |   |   |   |   |   |   |   |
|---|---|---|---|---|---|---|---|---|
| e | d | i | − | t | i | n | g | − | 
| − | d | i | s | t | a | n | c | e | 
