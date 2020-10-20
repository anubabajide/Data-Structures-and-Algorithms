#  Construct a Trie from a Collection of Patterns

## Description 
For a collection of strings Patterns, Trie(Patterns) is defined as follows.
1. The trie has a single root node with indegree 0.
2. Each edge of Trie(Patterns) is labeled with a letter of the alphabet.
3. Edges leading out of a given node have distinct labels.
4. Every string in Patterns is spelled out by concatenating the letters along some path from the root downward.
5. Every path from the root to a leaf (i.e, node with outdegree 0), spells a string from Patterns.


## Details
**Task**<br>
Construct a trie from a collection of patterns.

**Input format**<br> 
An integer 𝑛 and a collection of strings Patterns = {𝑝1, . . . , 𝑝𝑛} (each string is given on a separate line).

**Output format:**<br> 
The adjacency list corresponding to Trie(Patterns), in the following format. If Trie(Patterns) has 𝑛 nodes, first label the root with 0 and then label the remaining nodes with the integers 1 through 𝑛 − 1 in any order you like. Each edge of the adjacency list of Trie(Patterns) will be encoded by a triple: the first two members of the triple must be the integers 𝑖, 𝑗 labeling the initial and terminal nodes of the edge, respectively; the third member of the triple must be the symbol 𝑐 labeling the edge; output each such triple in the format u->v:c (with no spaces) on a separate line.


**Constraints:**<br>
1 ≤ 𝑛 ≤ 100<br> 
1 ≤ |𝑝<sub>𝑖</sub>| ≤ 100 for all 1 ≤ 𝑖 ≤ 𝑛<br> 
𝑝<sub>𝑖</sub>’s contain only symbols A, C, G, T<br> 
no 𝑝<sub>𝑖</sub> is a prefix of 𝑝<sub>𝑗</sub> for all 1 ≤ 𝑖 ̸= 𝑗 ≤ 𝑛.

## Samples.
Sample 1.

    Input:
        1
        ATA
    Output:
        0->1:A
        2->3:A
        1->2:T
    
        0
     (A)↓
        1
     (T)↓
        2
     (A)↓
        3
    
Sample 2.

    Input:
        3
        AT
        AG
        AC
    Output:
        0->1:A
        1->4:C
        1->3:G
        1->2:T

              0
           (A)↓
              1
       (T)↙(G)↓ ↘(C)
          2   3  4
        
Sample 3.

    Input:
        3
        ATAGA
        ATC
        GAT
    Output:
        0->1:A
        1->2:T
        2->3:A
        3->4:G
        4->5:A
        2->6:C
        0->7:G
        7->8:A
        8->9:T
