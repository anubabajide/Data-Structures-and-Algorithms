# Is it a Binary Search Tree? Hard Version

## Description 
In this problem you are going to solve the same problem as the previous one, but for a more general case, when binary search tree may contain equal keys.

## Details
**Task**<br>
You are given a binary tree with integers as its keys. You need to test whether it is a correct binary search tree. Note that there can be duplicate integers in the tree, and this is allowed. The definition ofthe binary search tree in such case is the following: for any node of the tree, if its key is 𝑥, then for any node in its left subtree its key must be strictly less than 𝑥, and for any node in its right subtree its key must be greater than or equal to 𝑥. In other words, smaller elements are to the left, bigger elements are to the right, and duplicates are always to the right. You need to check whether the given binary tree structure satisfies this condition. You are guaranteed that the input contains a valid binary tree. That is, it is a tree, and each node has at most two children.

**Input format**<br> 
The first line contains the number of vertices 𝑛. The vertices of the tree are numbered from 0 to 𝑛 − 1. Vertex 0 is the root.<br>
The next 𝑛 lines contain information about vertices 0, 1, ..., 𝑛−1 in order. Each of these lines contains three integers 𝑘𝑒𝑦<sub>𝑖</sub>, 𝑙𝑒𝑓𝑡<sub>𝑖</sub> and 𝑟𝑖𝑔ℎ𝑡<sub>𝑖</sub> — 𝑘𝑒𝑦<sub>𝑖</sub> is the key of the 𝑖-th vertex, 𝑙𝑒𝑓𝑡<sub>𝑖</sub> is the index of the left child of the 𝑖-th vertex, and 𝑟𝑖𝑔ℎ𝑡<sub>𝑖</sub> is the index of the right child of the 𝑖-th vertex. If 𝑖 doesn’t have left or right child (or both), the corresponding 𝑙𝑒𝑓𝑡<sub>𝑖</sub> or 𝑟𝑖𝑔ℎ𝑡<sub>𝑖</sub> (or both) will be equal to −1.

**Output format:**<br> 
If the given binary tree is a correct binary search tree (see the definition in the problem description), output one word “CORRECT” (without quotes). Otherwise, output one word “INCORRECT” (without quotes).

**Constraints:**<br>
0 ≤ 𝑛 ≤ 10<sup>5</sup> <br>
−2<sup>31</sup> < 𝑘𝑒𝑦<sub>𝑖</sub> < 2<sup>31</sup>− 1<br> 
−1 ≤ 𝑙𝑒𝑓𝑡<sub>𝑖</sub>, 𝑟𝑖𝑔ℎ𝑡<sub>𝑖</sub> ≤ 𝑛 − 1.<br> 
It is guaranteed that the input represents a valid binary tree. In particular, if 𝑙𝑒𝑓𝑡<sub>𝑖</sub> ̸= −1 and 𝑟𝑖𝑔ℎ𝑡<sub>𝑖</sub> ̸= −1, then 𝑙𝑒𝑓𝑡<sub>𝑖</sub> ̸= 𝑟𝑖𝑔ℎ𝑡<sub>𝑖</sub>.<br>
Also, a vertex cannot be a child of two different vertices. Also, each vertex is a descendant of the root vertex. All keys in the input will be different.

## Samples.
Sample 1.

    Input:
    3
    2 1 2
    1 -1 -1
    3 -1 -1
    Output:
    CORRECT
    2
    1 3
    Left child of the root has key 1, right child of the root has key 3, root has key 2, so everything to the
    left is smaller, everything to the right is bigger.

Sample 2.

    Input:
        3
        1 1 2
        2 -1 -1
        3 -1 -1
    Output:
        INCORRECT
    
        1
       / \
      2   3
    The left child of the root must have smaller key than the root.

Sample 3.

    Input:
        3
        2 1 2
        1 -1 -1
        2 -1 -1
    Output:
        CORRECT
    
        2
       / \
      1   2
    Duplicate keys are allowed, and they should always be in the right subtree of the first duplicated element.

Sample 4.

    Input:
        3
        2 1 2
        2 -1 -1
        3 -1 -1
    Output:
        INCORRECT
    
        2
       / \
      2   3
    The key of the left child of the root must be strictly smaller than the key of the root.

Sample 5.

    Input:
        0
    Output:
        CORRECT
    
    Empty tree is considered correct.

Sample 6.

    Input:
        1
        2147483647 -1 -1
    Output:
        CORRECT
    
    Explanation:
        2147483647
    The maximum possible value of the 32-bit integer type is allowed as key in the tree.

Sample 7.
    
    Input:
        5
        1 -1 1
        2 -1 2
        3 -1 3
        4 -1 4
        5 -1 -1
    Output:
        CORRECT
    
    Explanation:
        1
         \
          2
           \
            3
             \
              4
               \
                5
    The tree doesn’t have to be balanced. We only need to test whether it is a correct binary search tree, which the tree in this example is.

Sample 8.

    Input:
        7
        4 1 2
        2 3 4
        6 5 6
        1 -1 -1
        3 -1 -1
        5 -1 -1
        7 -1 -1
    Output:
        CORRECT
    
    Explanation:
          4
        /   \
       /     \
      2       6
     / \     / \
    1   3   5   7
    This is a full binary tree, and the property of the binary search tree is satisfied in every node.
