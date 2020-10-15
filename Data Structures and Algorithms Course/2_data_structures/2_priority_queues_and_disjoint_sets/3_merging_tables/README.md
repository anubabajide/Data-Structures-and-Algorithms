# Merging Tables

## Description 
In this problem, your goal is to simulate a sequence of merge operations with tables in a database.

## Details
**Task**<br>
There are 𝑛 tables stored in some database. The tables are numbered from 1 to 𝑛. All tables share
the same set of columns. Each table contains either several rows with real data or a symbolic link to
another table. Initially, all tables contain data, and 𝑖-th table has 𝑟𝑖 rows. You need to perform 𝑚 of
the following operations:
1. Consider table number 𝑑𝑒𝑠𝑡𝑖𝑛𝑎𝑡𝑖𝑜𝑛𝑖
. Traverse the path of symbolic links to get to the data. That is,
while 𝑑𝑒𝑠𝑡𝑖𝑛𝑎𝑡𝑖𝑜𝑛𝑖 contains a symbolic link instead of real data do
𝑑𝑒𝑠𝑡𝑖𝑛𝑎𝑡𝑖𝑜𝑛𝑖 ← symlink(𝑑𝑒𝑠𝑡𝑖𝑛𝑎𝑡𝑖𝑜𝑛𝑖)
2. Consider the table number 𝑠𝑜𝑢𝑟𝑐𝑒𝑖 and traverse the path of symbolic links from it in the same
manner as for 𝑑𝑒𝑠𝑡𝑖𝑛𝑎𝑡𝑖𝑜𝑛𝑖
.
3. Now, 𝑑𝑒𝑠𝑡𝑖𝑛𝑎𝑡𝑖𝑜𝑛𝑖 and 𝑠𝑜𝑢𝑟𝑐𝑒𝑖 are the numbers of two tables with real data. If 𝑑𝑒𝑠𝑡𝑖𝑛𝑎𝑡𝑖𝑜𝑛𝑖 ̸=
𝑠𝑜𝑢𝑟𝑐𝑒𝑖
, copy all the rows from table 𝑠𝑜𝑢𝑟𝑐𝑒𝑖 to table 𝑑𝑒𝑠𝑡𝑖𝑛𝑎𝑡𝑖𝑜𝑛𝑖
, then clear the table 𝑠𝑜𝑢𝑟𝑐𝑒𝑖
and instead of real data put a symbolic link to 𝑑𝑒𝑠𝑡𝑖𝑛𝑎𝑡𝑖𝑜𝑛𝑖
into it.
4. Print the maximum size among all 𝑛 tables (recall that size is the number of rows in the table).
If the table contains only a symbolic link, its size is considered to be 0.

See examples and explanations for further clarifications.


**Input format**<br> 
The first line of the input contains two integers 𝑛 and 𝑚 — the number of tables in the
database and the number of merge queries to perform, respectively.
The second line of the input contains 𝑛 integers 𝑟<sub>𝑖</sub> — the number of rows in the 𝑖-th table.
Then follow 𝑚 lines describing merge queries. Each of them contains two integers 𝑑𝑒𝑠𝑡𝑖𝑛𝑎𝑡𝑖𝑜𝑛𝑖 and
𝑠𝑜𝑢𝑟𝑐𝑒<sub>𝑖</sub> — the numbers of the tables to merge.

**Output format:**<br> 
For each query print a line containing a single integer — the maximum of the sizes of all tables (in terms of the number of rows) after the corresponding operation.

**Constraints:**<br>
1 ≤ 𝑛, 𝑚 ≤ 100 000 <br> 
0 ≤ 𝑟𝑖 ≤ 10 000; <br> 
1 ≤ 𝑑𝑒𝑠𝑡𝑖𝑛𝑎𝑡𝑖𝑜𝑛<sub>𝑖</sub>, 𝑠𝑜𝑢𝑟𝑐𝑒<sub>𝑖</sub> ≤ 𝑛. <br>

## Samples.
Sample 1.

    Input:
        5 5
        1 1 1 1 1
        3 5
        2 4
        1 4
        5 4
        5 3
    Output:
        2
        2
        3
        5
        5

In this sample, all the tables initially have exactly 1 row of data. Consider the merging operations:
1. All the data from the table 5 is copied to table number 3. Table 5 now contains only a symbolic yyylink to table 3, while table 3 has 2 rows. 2 becomes the new maximum size.
2. 2 and 4 are merged in the same way as 3 and 5.
3. We are trying to merge 1 and 4, but 4 has a symbolic link pointing to 2, so we actually copy all the data from the table number 2 to the table number 1, clear the table number 2 and put a symbolic link to the table number 1 in it. Table 1 now has 3 rows of data, and 3 becomes the new maximum size.
4. Traversing the path of symbolic links from 4 we have 4 → 2 → 1, and the path from 5 is 5 → 3. So we are actually merging tables 3 and 1. We copy all the rows from the table number 1 into the table number 3, and now the table number 3 has 5 rows of data, which is the new maximum.
5. All tables now directly or indirectly point to table 3, so all other merges won’t change anything.

Sample 2.

    Input:
        6 4
        10 0 5 0 3 3
        6 6
        6 5
        5 4
        4 3
    Output:
        10
        10
        10
        11

In this example tables have different sizes. Let us consider the operations:
1. Merging the table number 6 with itself doesn’t change anything, and the maximum size is 10 (table number 1).
1. After merging the table number 5 into the table number 6, the table number 5 is cleared and has size 0, while the table number 6 has size 6. Still, the maximum size is 10.
3. By merging the table number 4 into the table number 5, we actually merge the table number 4 into the table number 6 (table 5 now contains just a symbolic link to table 6), so the table number
4 is cleared and has size 0, while the table number 6 has size 6. Still, the maximum size is 10.
4. By merging the table number 3 into the table number 4, we actually merge the table number 3 into the table number 6 (table 4 now contains just a symbolic link to table 6), so the table number 3 is cleared and has size 0, while the table number 6 has size 11, which is the new maximum size.
