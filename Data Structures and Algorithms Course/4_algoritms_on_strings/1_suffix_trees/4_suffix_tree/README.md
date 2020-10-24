# Construct the Suffix Tree of a String

## Description 
A suffix tree is an extremely powerful indexing data structure having applications in areas like pattern matching, data compression, and bioinformatics. Your goal in this problem is to implement this data structure. <br>
Storing Trie(Patterns) requires a great deal of memory. So let’s process Text into a data structure instead. Our goal is to compare each string in Patterns against Text without needing to traverse Text from beginning to end. In more familiar terms, instead of packing Patterns onto a bus and riding the long distance down Text, our new data structure will be able to “teleport” each string in Patterns directly to its occurrences in Text. <br>
A suffix trie, denoted SuffixTrie(Text), is the trie formed from all suffixes of Text. From now on, we append the dollar-sign (“$”) to Text in order to mark the end of Text. We will also label each leaf of the resulting trie by the starting position of the suffix whose path through the trie ends at this leaf (using 0-based indexing). This way, when we arrive at a leaf, we will immediately know where this suffix came from in Text. <br>
However, the runtime and memory required to construct SuffixTrie(Text) are both equal to the combined length of all suffixes in Text. There are |Text| suffixes of Text, ranging in length from 1 to |Text| and having total length |Text| · (|Text| + 1)/2, which is Θ(|Text| 2). Thus, we need to reduce both the construction time and memory requirements of suffix tries to make them practical. <br>
Let’s not give up hope on suffix tries. We can reduce the number of edges in SuffixTrie(Text) by combining the edges on any non-branching path into a single edge. We then label this edge with the concatenation of symbols on the consolidated edges. The resulting data structure is called a suffix tree, written SuffixTree(Text). <br>
To match a single Pattern to Text, we thread Pattern into SuffixTree(Text) by the same process used for a suffix trie. Similarly to the suffix trie, we can use the leaf labels to find starting positions of successfully matched patterns. <br>
Suffix trees save memory because they do not need to store concatenated edge labels from each nonbranching path. For example, a suffix tree does not need ten bytes to store the edge labeled “mabananas$” in SuffixTree(“panamabananas$”); instead, it suffices to store a pointer to position 4 of “panamabananas$”, as well as the length of “mabananas$”. Furthermore, suffix trees can be constructed in linear time, without having to first construct the suffix trie! We will not ask you to implement this fast suffix tree construction algorithm because it is quite complex.

## Details
**Task**<br>
Construct the suffix tree of a string.

**Input format**<br> 
A string Text ending with a “$” symbol.

**Output format:**<br> 
The strings labeling the edges of SuffixTree(Text) in any order.

**Constraints:**<br>
1 ≤ |Text| ≤ 5 000 except the last symbol<br> 
Text contains symbols A, C, G, T only.

## Samples.
Sample 1.

    Input:
        A$
    Output:
        A$
        $

       $/ \A$
       1   0
    
Sample 2.

    Input:
        ACA$
    Output:
        $
        A
        $
        CA$
        CA$

Sample 3.

    Input:
        ATAAATG$
    Output:
        AAATG$
        G$
        T
        ATG$
        TG$
        A
        A
        AAATG$
        G$
        T
        G$
        $

