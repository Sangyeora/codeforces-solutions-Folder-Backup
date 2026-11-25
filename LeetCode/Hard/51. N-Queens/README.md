# 51. N-Queens

## Difficulty: Hard

## Platform: LeetCode

## Problem Link
[View Problem](https://leetcode.com/problems/n-queens/)

## Solved On
25 Nov 2026 at 11:37 pm

The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.

## My Notes / Approach:
Input:
n = 4

Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above
Example 2:

Input:
n = 1

Output: [["Q"]]
 

Constraints:

1 <= n <= 9
两个queen不能在一行一列或斜线，回溯法，试，撤回。
cols.append(col) 
place(row + 1)尝试下一行
cols.pop() 尝试结束，撤回当前皇后，换一列试
-cols记录【x，y】
判断斜线（非负数）：abs(cols[ i ] - col) == row - i