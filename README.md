# LeetCode-Solution-Python

## 说明

+ 这个代码仓库是我在学习《算法与数据结构》的时候，在 [LeetCode（英文版）](https://leetcode.com/problemset/all/) 和 [LeetCode（中文版）](https://leetcode-cn.com/) 上做的练习， 。
+ 所有的代码都是通过 LeetCode 在线测评系统检测的，至少是正确的代码，但不一定是时间复杂度和空间复杂度最优的。
+ 建议您安装 [Octotree 插件](https://www.octotree.io/?utm_source=lite&utm_medium=extension)，以获得最佳的阅读体验。

![Octotree 插件](https://liweiwei1419.github.io/images/leetcode-solution-new/Octotree.png)

## 配套资源

+ 对应的 Java 仓库的地址，传送门：[https://github.com/liweiwei1419/LeetCode-Solution-Java](https://github.com/liweiwei1419/LeetCode-Solution-Java)

说明：现在刷题，尤其是写题解，绝大多数问题都会写两个语言的代码，Java 是我的母语，Python 是我的新欢。

+ 发布在 LeetCode 中文版上的题解配图使用的 PPT，传送门：[https://github.com/liweiwei1419/LeetCode-Solution-PPT](https://github.com/liweiwei1419/LeetCode-Solution-PPT)

说明：做了 PPT 或者动画的题目，一般在 LeetCode 中文版的题解区都能看到我写的题解。

## 编码风格

在代码编写的过程中，我比较注意的地方有：

+ 保证语义清晰，这一点我认为是最重要的。代码虽然是运行在机器上，但更多时候是写给人看的，在逻辑正确，时间复杂度和空间复杂度都较优的前提下，语义清晰的代码更便于他人理解，也更利于不同观点的人之间的沟通。不以追求代码最短为目标，有时为了分割语义，我还会加上空格，体现逻辑的层次。代码也不是在纸上写，没有必要节约代码空间，这意义不大；
+ 变量和方法的命名尽量有意义，并且是见名知义的；
+ Python 相比 Java 而言，语法比较灵活，可能会有一些比较 pythonista 的写法，让你的代码更简短更“好”，但刷题这件事情，应该更注重于常用算法数据结构和思想的应用，而少用例如 Python 这种有一些高度封装过后的代码库，相对而言 Java 和 C++ 更适合刷题。我工作以后，先会的 Java ，然后才会 Python，在 Python 中有 Java 中没有的语法，我就不会在刷题中用了；
+ 所有的代码在提交到 LeetCode 在线测评系统之前，都使用了 PyCharm 提供的自动格式化功能（快捷键：alt + command + L），有些还使用了 autopep8 工具进行格式化，我个人还是比较看重代码颜值的，况且这样做成本也很低；
+ 为了保证易读性，编码的时候会写上注释，有时注释甚至是啰嗦且多余的，还有一点，我怕以后自己再看的时候都看不懂当初是怎么写的。

对于一些比较经典的问题，我还写了题解，制作了动画，可以在以下的链接中找到。

## 刷题过程中形成的文章

| 第 1 章 数组                                                 | [代码文件夹](https://github.com/liweiwei1419/LeetCode-Solution-Python/tree/master/03-%E6%95%B0%E7%BB%84%E9%97%AE%E9%A2%98) |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| LeetCode 数组专题 1：二分查找                                | [链接地址](https://liweiwei1419.github.io/blog/2018/10/14/leetcode-solution/array1/) |
| LeetCode 数组专题 2：一些关于数组的问题                      | [链接地址](https://liweiwei1419.github.io/blog/2018/10/15/leetcode-solution/array2/) |
| LeetCode 数组专题 3：三路快排 partition 的应用               | [链接地址](https://liweiwei1419.github.io/blog/2018/10/16/leetcode-solution/array3/) |
| LeetCode 数组专题 4：双索引技术之一：对撞指针                | [链接地址](https://liweiwei1419.github.io/blog/2018/10/17/leetcode-solution/two-pointers/) |
| LeetCode 数组专题 5：双索引技术之二：滑动窗口                | [链接地址](https://liweiwei1419.github.io/blog/2018/10/18/leetcode-solution/array5/) |
| LeetCode 数组专题 6：其它数组问题                            | [链接地址](https://liweiwei1419.github.io/blog/2018/10/19/leetcode-solution/array6/) |
| **第 2 章 查找表**                                           | [代码文件夹](https://github.com/liweiwei1419/LeetCode-Solution-Python/tree/master/04-%E6%9F%A5%E6%89%BE%E8%A1%A8%E9%97%AE%E9%A2%98) |
| LeetCode 查找表专题 1：查找问题简介                          | [链接地址](https://liweiwei1419.github.io/blog/2018/10/06/leetcode-solution/hash-table-1/) |
| LeetCode 查找表专题 2：哈希表的使用                          | [链接地址](https://liweiwei1419.github.io/blog/2018/10/07/leetcode-solution/hash-table-2/) |
| LeetCode 查找表专题 3：set 和 map 不同底层实现的区别         | [链接地址](https://liweiwei1419.github.io/blog/2018/10/08/leetcode-solution/hash-table-3/) |
| LeetCode 查找表专题 4：使用查找表的经典问题：Two Sum         | [链接地址](https://liweiwei1419.github.io/blog/2018/10/09/leetcode-solution/hash-table-4/) |
| LeetCode 查找表专题 5：灵活选择键值：4Sum II                 | [链接地址](https://liweiwei1419.github.io/blog/2018/10/10/leetcode-solution/hash-table-5/) |
| LeetCode 查找表专题 6：灵活选择键值：Number of Boomerangs    | [链接地址](https://liweiwei1419.github.io/blog/2018/10/11/leetcode-solution/hash-table-6/) |
| LeetCode 查找表专题 7：查找表和滑动窗口                      | [链接地址](https://liweiwei1419.github.io/blog/2018/10/12/leetcode-solution/hash-table-7/) |
| LeetCode 查找表专题 8：使用树结构                            | [链接地址](https://liweiwei1419.github.io/blog/2018/10/13/leetcode-solution/hash-table-8/) |
| **第 3 章 单链表**                                           | [代码文件夹]()                                               |
| LeetCode 链表专题 1：在链表中穿针引线                        | [链接地址](https://liweiwei1419.github.io/blog/2018/09/01/leetcode-solution/linked-list-1/) |
| LeetCode 链表专题 2：测试你的链表程序                        | [链接地址](https://liweiwei1419.github.io/blog/2018/09/02/leetcode-solution/linked-list-2/) |
| LeetCode 链表专题 3：设立链表的虚拟头结点                    | [链接地址](https://liweiwei1419.github.io/blog/2018/09/03/leetcode-solution/linked-list-3/) |
| LeetCode 链表专题 4：复杂的穿针引线                          | [链接地址](https://liweiwei1419.github.io/blog/2018/09/04/leetcode-solution/linked-list-4/) |
| LeetCode 链表专题 5：不仅仅是穿针引线                        | [链接地址](https://liweiwei1419.github.io/blog/2018/09/05/leetcode-solution/linked-list-5/) |
| LeetCode 链表专题 6：链表与双指针                            | [链接地址](https://liweiwei1419.github.io/blog/2018/09/06/leetcode-solution/linked-list-6/) |
| **第 4 章 栈、队列、优先队列**                               | [代码文件夹](https://github.com/liweiwei1419/LeetCode-Solution-Python/tree/master/06-%E6%A0%88%E3%80%81%E9%98%9F%E5%88%97%E3%80%81%E4%BC%98%E5%85%88%E9%98%9F%E5%88%97) |
| LeetCode 栈、队列、优先队列专题 1：栈和队列的使用            | [链接地址](https://liweiwei1419.github.io/blog/2018/09/30/leetcode-solution/stack-1/) |
| LeetCode 栈、队列、优先队列专题 2：二叉树的三种非递归实现    | [链接地址](https://liweiwei1419.github.io/blog/2018/10/01/leetcode-solution/stack-2/) |
| LeetCode 栈、队列、优先队列专题 3：使用自己编写的模拟系统栈，写出非递归的程序 | [链接地址](https://liweiwei1419.github.io/blog/2018/10/02/leetcode-solution/stack-3/) |
| LeetCode 栈、队列、优先队列专题 4：队列 Queue 与广度优先遍历 | [链接地址](https://liweiwei1419.github.io/blog/2018/10/03/leetcode-solution/queue-1/) |
| LeetCode 栈、队列、优先队列专题 5：广度优先遍历和图的最短路径问题 | [链接地址](https://liweiwei1419.github.io/blog/2018/10/04/leetcode-solution/queue-2/) |
| LeetCode 栈、队列、优先队列专题 6：优先队列也是队列          | [链接地址](https://liweiwei1419.github.io/blog/2018/10/05/leetcode-solution/priority-queue/) |
| **第 5 章 二叉树和递归**                                     | [代码文件夹](https://github.com/liweiwei1419/LeetCode-Solution-Python/tree/master/07-%E4%BA%8C%E5%8F%89%E6%A0%91%E5%92%8C%E9%80%92%E5%BD%92) |
| LeetCode 二叉树和递归专题 1：从二叉树的角度看递归            | [链接地址](https://liweiwei1419.github.io/blog/2018/09/24/leetcode-solution/binary-tree-1/) |
| LeetCode 二叉树和递归专题 2：一个简单的二叉树引发的血案      | [链接地址](https://liweiwei1419.github.io/blog/2018/09/25/leetcode-solution/binary-tree-2/) |
| LeetCode 二叉树和递归专题 3：注意递归的终止条件              | [链接地址](https://liweiwei1419.github.io/blog/2018/09/26/leetcode-solution/binary-tree-3/) |
| LeetCode 二叉树和递归专题 4：如何使用递归函数的返回值        | [链接地址](https://liweiwei1419.github.io/blog/2018/09/27/leetcode-solution/binary-tree-4/) |
| LeetCode 二叉树和递归专题 5：稍复杂的递归逻辑 Path Sum III   | [链接地址](https://liweiwei1419.github.io/blog/2018/09/28/leetcode-solution/binary-tree-5/) |
| LeetCode 二叉树和递归专题 6：二分搜索树中的问题              | [链接地址](https://liweiwei1419.github.io/blog/2018/09/29/leetcode-solution/binary-tree-6/) |
| **第 6 章 回溯问题**                                         | [代码文件夹](https://github.com/liweiwei1419/LeetCode-Solution-Python/tree/master/08-%E9%80%92%E5%BD%92%E5%92%8C%E5%9B%9E%E6%BA%AF%E6%B3%95) |
| LeetCode 回溯专题 1：在树形问题中使用递归                    | [链接地址](https://liweiwei1419.github.io/blog/2018/09/07/leetcode-solution/backtracking-1/) |
| LeetCode 回溯专题 2：回溯法是暴力解法的一个主要的实现手段    | [链接地址](https://liweiwei1419.github.io/blog/2018/09/08/leetcode-solution/backtracking-2/) |
| LeetCode 回溯专题 3：排列问题 Permutations                   | [链接地址](https://liweiwei1419.github.io/blog/2018/09/09/leetcode-solution/backtracking-3/) |
| LeetCode 回溯专题 4：组合问题 Combinations                   | [链接地址](https://liweiwei1419.github.io/blog/2018/09/10/leetcode-solution/backtracking-4/) |
| LeetCode 回溯专题 5：回溯法解决组合问题的优化                | [链接地址](https://liweiwei1419.github.io/blog/2018/09/11/leetcode-solution/backtracking-5/) |
| LeetCode 回溯专题 6：二维平面上使用回溯法                    | [链接地址](https://liweiwei1419.github.io/blog/2018/09/12/leetcode-solution/backtracking-6/) |
| LeetCode 回溯专题 7：floodfill 解决一类经典问题              | [链接地址](https://liweiwei1419.github.io/blog/2018/09/13/leetcode-solution/backtracking-7/) |
| LeetCode 回溯专题 8：回溯法是经典的人工智能的基础            | [链接地址](https://liweiwei1419.github.io/blog/2018/09/14/leetcode-solution/backtracking-8/) |
| **第 7 章 动态规划问题**                                     | [代码文件夹](https://github.com/liweiwei1419/LeetCode-Solution-Python/tree/master/09-%E5%8A%A8%E6%80%81%E8%A7%84%E5%88%92) |
| LeetCode 动态规划专题 1：“重叠子问题”和“记忆化搜索”          | [链接地址](https://liweiwei1419.github.io/blog/2018/09/15/leetcode-solution/dynamic-programming-1/) |
| LeetCode 动态规划专题 2：第 1 个动态规划问题的 3 种实现      | [链接地址](https://liweiwei1419.github.io/blog/2018/09/16/leetcode-solution/dynamic-programming-2/) |
| LeetCode 动态规划专题 3：第 2 个动态规划问题：整数分割       | [链接地址](https://liweiwei1419.github.io/blog/2018/09/16/leetcode-solution/dynamic-programming-3/) |
| LeetCode 动态规划专题 4：状态和状态转移方程                  | [链接地址](https://liweiwei1419.github.io/blog/2018/09/16/leetcode-solution/dynamic-programming-4/) |
| LeetCode 动态规划专题 5：0-1 背包问题                        | [链接地址](https://liweiwei1419.github.io/blog/2018/09/16/leetcode-solution/dynamic-programming-5/) |
| LeetCode 动态规划专题 6：0-1 背包问题在空间复杂度上的两个优化 | [链接地址](https://liweiwei1419.github.io/blog/2018/09/16/leetcode-solution/dynamic-programming-6/) |
| LeetCode 动态规划专题 7：面试中的 0-1 背包问题               | [链接地址](https://liweiwei1419.github.io/blog/2018/09/16/leetcode-solution/dynamic-programming-7/) |
| LeetCode 动态规划专题 8：最长上升子序列问题                  | [链接地址](https://liweiwei1419.github.io/blog/2018/09/16/leetcode-solution/dynamic-programming-8/) |
| **第 8 章 贪心算法**                                         | [代码文件夹](https://github.com/liweiwei1419/LeetCode-Solution-Python/tree/master/10-%E8%B4%AA%E5%BF%83%E7%AE%97%E6%B3%95) |
| LeetCode 专题：贪心算法                                      | [链接地址](https://liweiwei1419.github.io/blog/2018/09/04/leetcode-tag/greedy/) |
| **第 9 章 拓扑排序**                                         | [代码文件夹](https://github.com/liweiwei1419/LeetCode-Solution-Python/tree/master/11-%E6%8B%93%E6%89%91%E6%8E%92%E5%BA%8F) |
| LeetCode 专题：拓扑排序                                      | [链接地址](https://liweiwei1419.github.io/blog/2019/02/16/leetcode-tag/topological-sort/) |
| **第 10 章 字典树**                                          | [代码文件夹](https://github.com/liweiwei1419/LeetCode-Solution-Python/tree/master/12-trie) |
| 【算法日积月累】20-高级数据结构：字典树                      | [链接地址](https://liweiwei1419.github.io/blog/2019/01/21/algorithms-and-data-structures/trie/) |
| **第 11 章 并查集**                                          | [代码文件夹](https://github.com/liweiwei1419/LeetCode-Solution-Python/tree/master/13-%E5%B9%B6%E6%9F%A5%E9%9B%86) |
| 【算法日积月累】17-高级数据结构：并查集                      | [链接地址](https://liweiwei1419.github.io/blog/2019/01/18/algorithms-and-data-structures/union-find-set/) |
| **第 12 章 位运算**                                          | [代码文件夹](https://github.com/liweiwei1419/LeetCode-Solution-Python/tree/master/14-%E4%BD%8D%E8%BF%90%E7%AE%97) |
| LeetCode 专题：位运算                                        | [链接地址](https://liweiwei1419.github.io/blog/2018/09/25/leetcode-tag/bit-manipulation/) |
| **第 13 章 树状数组**                                        | [代码文件夹](https://github.com/liweiwei1419/LeetCode-Solution-Python/tree/master/15-%E6%A0%91%E7%8A%B6%E6%95%B0%E7%BB%84) |
| 【算法日积月累】19-高级数据结构：树状数组                    | [链接地址](https://liweiwei1419.github.io/blog/2019/01/20/algorithms-and-data-structures/fenwick-tree/) |
| **第 14 章 分治算法**                                        | [代码文件夹](https://github.com/liweiwei1419/LeetCode-Solution-Python/tree/master/16-%E5%88%86%E6%B2%BB) |
| [整理中]                                                     |                                                              |
| **第 15 章 二分查找**                                        | [代码文件夹](https://github.com/liweiwei1419/LeetCode-Solution-Python/tree/master/17-%E4%BA%8C%E5%88%86%E6%9F%A5%E6%89%BE) |
| LeetCode 专题：二分查找                                      | [链接地址](https://liweiwei1419.github.io/blog/2019/01/13/algorithms-and-data-structures/binary-search/) |
| **第 16 章 线段树**                                          | [代码文件夹](https://github.com/liweiwei1419/LeetCode-Solution-Python/tree/master/18-%E7%BA%BF%E6%AE%B5%E6%A0%91) |
| 【算法日积月累】18-高级数据结构：线段树                      | [链接地址](https://liweiwei1419.github.io/blog/2019/01/19/algorithms-and-data-structures/segment-tree/) |
| **第 17 章 数学问题**                                        | [代码文件夹](https://github.com/liweiwei1419/LeetCode-Solution-Python/tree/master/19-%E6%95%B0%E5%AD%A6) |
| [整理中]                                                     |                                                              |
| **第 18 章 优先队列**                                        | [代码文件夹](https://github.com/liweiwei1419/LeetCode-Solution-Python/tree/master/20-%E4%BC%98%E5%85%88%E9%98%9F%E5%88%97) |
| [整理中]                                                     |                                                              |
| **第 19 章 字符串**                                          | [代码文件夹](https://github.com/liweiwei1419/LeetCode-Solution-Python/tree/master/21-%E5%AD%97%E7%AC%A6%E4%B8%B2) |
| [整理中]                                                     |                                                              |

