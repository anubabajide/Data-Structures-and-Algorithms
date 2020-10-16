# Hashing With Chains

## Description 
In this problem you will implement a hash table using the chaining scheme. Chaining is one of the most popular ways of implementing hash tables in practice. The hash table you will implement can be used to implement a phone book on your phone or to store the password table of your computer or web service (but don’t forget to store hashes of passwords instead of the passwords themselves, or you will get hacked!).

## Details
**Task**<br>
In this task your goal is to implement a hash table with lists chaining. You are already given the
number of buckets 𝑚 and the hash function. It is a polynomial hash function
   
   <br>
⎛ℎ(𝑆) = ∑︁<sup>|𝑆|−1</sup> <sub>𝑖=0</sub> 𝑆[𝑖]𝑥<sup>𝑖</sup>⎞ mod 𝑚<br>
⎝
    ..........................................⎠ ,<br>
where 𝑆[𝑖] is the ASCII code of the 𝑖-th symbol of 𝑆, 𝑝 = 1 000 000 007 and 𝑥 = 263. Your program
should support the following kinds of queries:

1. add string — insert string into the table. If there is already such string in the hash table, then just ignore the query.
2. del string — remove string from the table. If there is no such string in the hash table, then just ignore the query.
3. find string — output “yes" or “no" (without quotes) depending on whether the table contains string or not.
4. check 𝑖 — output the content of the 𝑖-th list in the table. Use spaces to separate the elements of the list. **If 𝑖-th list is empty, output a blank line**.

When inserting a new string into a hash chain, you must insert it in the beginning of the chain


**Input format**<br> 
There is a single integer 𝑚 in the first line — the number of buckets you should have. The next line contains the number of queries 𝑁. It’s followed by 𝑁 lines, each of them contains one query in the format described above.

**Output format:**<br> 
Print the result of each of the find and check queries, one result per line, in the same order as these queries are given in the input.

**Constraints:**<br>
1 ≤ 𝑁 ≤ 10<sup>5</sup> <br>
𝑁/5 ≤ 𝑚 ≤ 𝑁. <br>
All the strings consist of latin letters. Each of them is non-empty and has length at most 15.


## Samples.
Sample 1.

    Input:
        5
        12
        add world
        add HellO
        check 4
        find World
        find world
        del world
        check 4
        del HellO
        add luck
        add GooD
        check 2
        del good
    Output:
        HellO world
        no
        yes
        HellO
        GooD luck
  
    The ASCII code of ’w’ is 119, for ’o’ it is 111, for ’r’ it is 114, for ’l’ it is 108, and for ’d’ it is 100. Thus, ℎ(“world") = (119 + 111 × 263 + 114 × 2632 + 108 × 2633 + 100 × 2634 mod 1 000 000 007) mod 5 = 4. It turns out that the hash value of 𝐻𝑒𝑙𝑙𝑂 is also 4. Recall that we always insert in the beginning of the chain, so after adding “world" and then “HellO" in the same chain index 4, first goes “HellO" and then goes “world". Of course, “World" is not found, and “world" is found, because the strings are case-sensitive, and the codes of ’W’ and ’w’ are different. After deleting “world", only “HellO" is found in the chain 4. Similarly to “world" and “HellO", after adding “luck" and “GooD" to the same chain 2, first goes “GooD" and then “luck".

Sample 2.

    Input:
        4
        8
        add test
        add test
        find test
        del test
        find test
        find Test
        add Test
        find Test
    Output:
        yes
        no
        no
        yes
    
    Adding “test" twice is the same as adding “test" once, so first find returns “yes". After del, “test" is 6 no longer in the hash table. First time find doesn’t find “Test” because it was not added before, and strings are case-sensitive in this problem. Second time “Test” can be found, because it has just been added.

Sample 3.

    Input:
        3
        12
        check 0
        find help
        add help
        add del
        add add
        find add
        find del
        del del
        find del
        check 0
        check 1
        check 2
    Output:
        no
        yes
        yes
        no
        add help
    
    Explanation:
    Note that you need to output a blank line when you handle an empty chain. Note that the strings stored in the hash table can coincide with the commands used to work with the hash table.
