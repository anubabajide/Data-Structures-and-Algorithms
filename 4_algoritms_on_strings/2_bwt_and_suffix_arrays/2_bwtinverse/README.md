#  Reconstruct a String from its Burrows–Wheeler Transform

## Description 
In the previous problem, we introduced the Burrows–Wheeler transform of a string Text. It permutes the symbols of Text making it well compressible. However, there were no sense in this, if this process would not be reversible. It turns out that it is reversible, and your goal in this problem is to recover Text from BWT(Text).

## Details
**Task**<br>
Reconstruct a string from its Burrows–Wheeler transform.

**Input format**<br> 
The string Text such that BWT(Text) = Transform. (There exists a unique such string.)

**Output format:**<br> 
BWT(Text)

**Constraints:**<br>
1 ≤ |Transform| ≤ 1 000 000 except for the last symbol<br> 
Text contains symbols A, C, G, T only.

## Samples.
Sample 1.

    Input:
        AC$A
    Output:
        ACA$
    
                ⎡ $ 𝐴 𝐶 𝐴 ⎤
    M(Text) =   ⎢ 𝐴 $ 𝐴 𝐶 ⎥
                ⎢ 𝐴 𝐶 𝐴 $ ⎥
                ⎣ 𝐶 𝐴 $ 𝐴 ⎦    
    

Sample 2.

    Input:
        AGGGAA$
    Output:
        GAGAGA$
    
                ⎡ $ 𝐺 𝐴 𝐺 𝐴 𝐺 𝐴 ⎤
                ⎢ 𝐴 $ 𝐺 𝐴 𝐺 𝐴 𝐺 ⎥
                ⎢ 𝐴 𝐺 𝐴 $ 𝐺 𝐴 𝐺 ⎥
    M(Text) =   ⎢ 𝐴 𝐺 𝐴 𝐺 𝐴 $ 𝐺 ⎥
                ⎢ 𝐺 𝐴 $ 𝐺 𝐴 𝐺 𝐴 ⎥
                ⎢ 𝐺 𝐴 𝐺 𝐴 $ 𝐺 𝐴 ⎥
                ⎣ 𝐺 𝐴 𝐺 𝐴 𝐺 𝐴 $ ⎦
