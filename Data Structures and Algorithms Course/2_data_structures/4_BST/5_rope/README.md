# Rope

## Description 
In this problem you will implement Rope — data structure that can store a string and efficiently cut a part (a substring) of this string and insert it in a different position. This data structure can be enhanced to become persistent — that is, to allow access to the previous versions of the string. These properties make it a suitable choice for storing the text in text editors.

## Details
**Task**<br>
You are given a string 𝑆 and you have to process 𝑛 queries. Each query is described by three integers 𝑖, 𝑗, 𝑘 and means to cut substring 𝑆[𝑖..𝑗] (𝑖 and 𝑗 are 0-based) from the string and then insert it after the
𝑘-th symbol of the remaining string (if the symbols are numbered from 1). If 𝑘 = 0, 𝑆[𝑖..𝑗] is inserted
in the beginning. See the examples for further clarification


**Input format**<br> 
The first line contains the initial string 𝑆.<br>
The second line contains the number of queries 𝑞.<br>
Next 𝑞 lines contain triples of integers 𝑖, 𝑗, 𝑘.

**Output format:**<br> 
Output the string after all 𝑞 queries.

**Constraints:**<br>
𝑆 contains only lowercase english letters.<br> 
1 ≤ |𝑆| ≤ 300 000<br>
1 ≤ 𝑞 ≤ 100 000<br>
0 ≤ 𝑖 ≤ 𝑗 ≤ 𝑛 − 1<br> 
0 ≤ 𝑘 ≤ 𝑛 − (𝑗 − 𝑖 + 1).


## Samples.
Sample 1.
    
    Input:
        hlelowrold
        2
        1 1 2
        6 6 7
    Output:
        helloworld
    
    Explanation:
    ℎ𝑙𝑒𝑙𝑜𝑤𝑟𝑜𝑙𝑑 → ℎ𝑒𝑙𝑙𝑜𝑤𝑟𝑜𝑙𝑑 → ℎ𝑒𝑙𝑙𝑜𝑤𝑜𝑟𝑙𝑑
    When 𝑖 = 𝑗 = 1, 𝑆[𝑖..𝑗] = 𝑙, and it is inserted after the 2-nd symbol of the remaining string ℎ𝑒𝑙𝑜𝑤𝑟𝑜𝑙𝑑, which gives ℎ𝑒𝑙𝑙𝑜𝑤𝑟𝑜𝑙𝑑. Then 𝑖 = 𝑗 = 6, so 𝑆[𝑖..𝑗] = 𝑟, and it is inserted after the 7-th symbol of the remaining string ℎ𝑒𝑙𝑙𝑜𝑤𝑜𝑙𝑑, which gives ℎ𝑒𝑙𝑙𝑜𝑤𝑜𝑟𝑙𝑑.
    
Sample 2.

    Input:
        abcdef
        2
        0 1 1
        4 5 0
    Output:
        efcabd
    
    𝑎𝑏𝑐𝑑𝑒𝑓 → 𝑐𝑎𝑏𝑑𝑒𝑓 → 𝑒𝑓𝑐𝑎𝑏𝑑