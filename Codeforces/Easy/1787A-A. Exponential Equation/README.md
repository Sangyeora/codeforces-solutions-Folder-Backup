# 1787A-A. Exponential Equation

## Difficulty: Easy

## Platform: Codeforces

## Problem Link
[View Problem](https://codeforces.com/problemset/problem/1787/A)

## Solved On
20 Nov 2026 at 05:09 pm


You are given an integer 𝑛
.

Find any pair of integers (𝑥,𝑦)
 (1≤𝑥,𝑦≤𝑛
) such that 𝑥𝑦⋅𝑦+𝑦𝑥⋅𝑥=𝑛
.

Input
The first line contains a single integer 𝑡
 (1≤𝑡≤104
) — the number of test cases.

Each test case contains one line with a single integer 𝑛
 (1≤𝑛≤109
).

Output
For each test case, if possible, print two integers 𝑥
 and 𝑦
 (1≤𝑥,𝑦≤𝑛
). If there are multiple answers, print any.

Otherwise, print −1
.

## My Notes / Approach:
Note
In the third test case, 23⋅3+32⋅2=42
, so (2,3),(3,2)
 will be considered as legal solutions.

In the fourth test case, 55⋅5+55⋅5=31250
, so (5,5)
 is a legal solution.


11
