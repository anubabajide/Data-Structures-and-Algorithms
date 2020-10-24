# Construct the Burrows–Wheeler Transform of a String

## Description 
The Burrows–Wheeler transform of a string Text permutes the symbols of Text so that it becomes well compressible. Moreover, the transformation is reversible: one can recover the initial string Text from its Burrows–Wheeler transform. However, data compression is not its only application: it is also used for solving the multiple pattern matching problem and the sequence alignment problem. BWT(Text) is defined as follows. First, form all possible cyclic rotations of Text; a cyclic rotation is defined by chopping off a suffix from the end of Text and appending this suffix to the beginning of Text. Then, order all the cyclic rotations of Text lexicographically to form a |Text| × |Text| matrix of symbols denoted by 𝑀(Text). BWT(Text) is the last column of 𝑀(Text)

## Details
**Task**<br>
Construct the Burrows–Wheeler transform of a string.

**Input format**<br> 
A string Text ending with a “$” symbol.

**Output format:**<br> 
BWT(Text)

**Constraints:**<br>
1 ≤ |Text| ≤ 1 000 except for the last symbol<br> 
Text contains symbols A, C, G, T only.

## Samples.
Sample 1.

    Input:
        AA$
    Output:
        AA$
    
                ⎡ $ 𝐴 𝐴 ⎤
    M(Text) =   ⎢ 𝐴 $ 𝐴 ⎥
                ⎣ 𝐴 𝐴 $ ⎦    
    

Sample 2.

    Input:
        ACACACAC$
    Output:
        CCCC$AAAA
    
                ⎡ $ 𝐴 𝐶 𝐴 𝐶 𝐴 𝐶 𝐴 𝐶 ⎤
                ⎢ 𝐴 𝐶 $ 𝐴 𝐶 𝐴 𝐶 𝐴 𝐶 ⎥
                ⎢ 𝐴 𝐶 𝐴 𝐶 $ 𝐴 𝐶 𝐴 𝐶 ⎥
                ⎢ 𝐴 𝐶 𝐴 𝐶 𝐴 𝐶 $ 𝐴 𝐶 ⎥
    M(Text) =   ⎢ 𝐴 𝐶 𝐴 𝐶 𝐴 𝐶 𝐴 𝐶 $ ⎥
                ⎢ 𝐶 $ 𝐴 𝐶 𝐴 𝐶 𝐴 𝐶 𝐴 ⎥
                ⎢ 𝐶 𝐴 𝐶 $ 𝐴 𝐶 𝐴 𝐶 𝐴 ⎥
                ⎢ 𝐶 𝐴 𝐶 𝐴 𝐶 $ 𝐴 𝐶 𝐴 ⎥
                ⎣ 𝐶 𝐴 𝐶 𝐴 𝐶 𝐴 𝐶 $ 𝐴 ⎦

Sample 3.

    Input:
        AGACATA$
    Output:
        ATG$CAAA
    
                ⎡ $ 𝐴 𝐺 𝐴 𝐶 𝐴 𝑇 𝐴 ⎤
                ⎢ 𝐴 $ 𝐴 𝐺 𝐴 𝐶 𝐴 𝑇 ⎥
                ⎢ 𝐴 𝐶 𝐴 𝑇 𝐴 $ 𝐴 𝐺 ⎥
                ⎢ 𝐴 𝐺 𝐴 𝐶 𝐴 𝑇 𝐴 $ ⎥
    M(Text) =   ⎢ 𝐴 𝑇 𝐴 $ 𝐴 𝐺 𝐴 𝐶 ⎥
                ⎢ 𝐶 𝐴 𝑇 𝐴 $ 𝐴 𝐺 𝐴 ⎥
                ⎢ 𝐺 𝐴 𝐶 𝐴 𝑇 𝐴 $ 𝐴 ⎥
                ⎣ 𝑇 𝐴 $ 𝐴 𝐺 𝐴 𝐶 𝐴 ⎦
