# Matching Against a Compressed String

## Description 
Not only the Burrows–Wheeler transform makes the input string Text well compressible, it also allows one
to solve the pattern matching problem using the compressed strings instead of the initial string! This is
another beautiful property of the Burrows–Wheeler transform which allows us to avoid decompressing the
string, and thus to save lots of memory, while still solving the problem at hand.
The algorithm BWMatching counts the total number of matches of Pattern in Text, where the
only information that we are given is FirstColumn and LastColumn = BWT(Text) in addition to the
Last-to-First mapping. The pointers top and bottom are updated by the green lines in the following
pseudocode.

    BWMatching(FirstColumn, LastColumn, Pattern, LastToFirst):
        top ← 0
        bottom ← |LastColumn| − 1
        while top ≤ bottom:
            if Pattern is nonempty:
                symbol ← last letter in Pattern
                remove last letter from Pattern
                if positions from top to bottom in LastColumn contain occurrence of symbol:
                    topIndex ← first position of symbol among positions from top to bottom in LastColumn
                    bottomIndex ← last position of symbol among positions from top to bottom in LastColumn
                    top ← 𝐿𝑎𝑠𝑡𝑇𝑜𝐹𝑖𝑟𝑠𝑡(𝑡𝑜𝑝𝐼𝑛𝑑𝑒𝑥)
                    bottom ← 𝐿𝑎𝑠𝑡𝑇𝑜𝐹𝑖𝑟𝑠𝑡(𝑏𝑜𝑡𝑡𝑜𝑚𝐼𝑛𝑑𝑒𝑥)
                else:
                    return 0
            else:
                return bottom − top + 1

The Last-to-First array, denoted LastToFirst(𝑖), answers the following question: given a symbol at position 𝑖 in LastColumn, what is its position in FirstColumn? For example, if Text = panamabananas$ , BWT(Text) = smnpbnnaaaaa$a, FirstCol(Text) = $aaaaaabmnnnps, then we can rewrite BWT(Text) = s<sub>1</sub>m<sub>1</sub>n<sub>1</sub>p<sub>1</sub>b<sub>1</sub>n<sub>2</sub>n<sub>3</sub>a<sub>1</sub>a<sub>2</sub>a<sub>3</sub>a<sub>5</sub>a<sub>5</sub> $<sub>1</sub>a<sub>6</sub> and FirstCol(𝑇𝑒𝑥𝑡) = $<sub>1</sub>a<sub>1</sub>a<sub>2</sub>a<sub>3</sub>a<sub>4</sub>a<sub>5</sub>a<sub>6</sub>b<sub>1</sub>m<sub>1</sub>n<sub>1</sub>n<sub>2</sub>n<sub>3</sub>p<sub>1</sub>s<sub>1</sub>, and
now we see that a<sub>3</sub> in BWT(Text) corresponds to a3 in FirstCol(Text). If you implement BWMatching, you probably will find the algorithm to be slow. The reason for its sluggishness is that updating the pointers top and bottom is time-intensive, since it requires examining every symbol in LastColumn between top and bottom at each step. To improve BWMatching, we introduce a function Countsymbol(𝑖, LastColumn), which returns the number of occurrences of symbol in the first 𝑖 positions of LastColumn. For example,

Count<sub>“n”</sub>(10, “smnpbnnaaaaa $a”) = 3 and Count<sub>“a”</sub>(4, “smnpbnnaaaaa $ a”) = 0 .

The green lines from BWMatching can be compactly described without the First-to-Last mapping by the following two lines: 
    
    top ← (Countsymbol + 1)-th occurrence of character symbol in FirstColumn
    bottom ← position of symbol with rank Countsymbol(bottom + 1, LastColumn) in FirstColumn

Define *FirstOccurrence(symbol)* as the first position of symbol in FirstColumn. If Text = “panamabananas$ ”, then FirstColumn is “$aaaaaabmnnnps”, and the array holding all values of FirstOccurrence is [0, 1, 7, 8, 9, 12, 13]. For DNA strings of any length, the array FirstOccurrence contains only five elements. The two lines of pseudocode from the previous step can now be rewritten as follows:

    top ← FirstOccurrence(symbol) + Countsymbol(top, LastColumn)
    bottom ← FirstOccurrence(symbol) + Countsymbol(bottom + 1, LastColumn) − 1

In the process of simplifying the green lines of pseudocode from BWMatching, we have also eliminated the need for both FirstColumn and LastToFirst, resulting in a more efficient algorithm called **BetterBWMatching**.

    BWMatching(FirstOccurrence, LastColumn, Pattern, Count):
        top ← 0
        bottom ← |LastColumn| − 1
        while top ≤ bottom:
            if Pattern is nonempty:
                symbol ← last letter in Pattern
                remove last letter from Pattern
                if positions from top to bottom in LastColumn contain occurrence of symbol:
                    top ← FirstOccurrence(symbol) + Countsymbol(top, LastColumn)
                    bottom ← FirstOccurrence(symbol)+Countsymbol(bottom + 1, LastColumn)−1
                else:
                    return 0
            else:
                return bottom − top + 1


## Details
**Task**<br>
Implement BetterBWMatching algorithm

**Input format**<br> 
A string BWT(Text), followed by an integer 𝑛 and a collection of 𝑛 strings Patterns = {𝑝1, . . . , 𝑝𝑛} (on one line separated by spaces).

**Output format:**<br> 
A list of integers, where the 𝑖-th integer corresponds to the number of substring matches of the 𝑖-th member of Patterns in Text.

**Constraints:**<br>
1 ≤ |BWT(Text)| ≤ 10<sup>6</sup> except for the one $ symbol, BWT(Text) contains symbols A, C, G, T only<br> 
1 ≤ 𝑛 ≤ 5 000<br> 
for all 1 ≤ 𝑖 ≤ 𝑛, 𝑝<sub>𝑖</sub> is a string over A, C, G, T<br> 
1 ≤ |𝑝<sub>𝑖</sub>| ≤ 1 000.


## Samples.
Sample 1.

    Input:
        AGGGAA$
        1
        GA
    Output:
        3

    In this case, Text = GAGAGA$. The pattern GA appears three times in it.

Sample 2.

    Input:
        ATT$AA
        2
        ATA A
    Output:
        2 3
    
    Text = ATATA$ contains two occurrences of ATA and three occurrences of A.

Sample 3.

    Input:
        AT$TCTATG
        2
        TCT TATG
    Output:
        0 0
    
    Text = ATCGTTTA does not contain any occurrences of two given patterns.
    