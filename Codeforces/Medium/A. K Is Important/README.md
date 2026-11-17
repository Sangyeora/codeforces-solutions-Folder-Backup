# A. K Is Important

## Difficulty: Medium

## Platform: Codeforces

## Problem Link
[View Problem](https://codeforces.com/problemset/problem/2268/A)

## Solved On
17 Nov 2026 at 10:30 am

A. K Is Important
time limit per test2 seconds
memory limit per test256 megabytes

You are given an array 𝑎
 consisting of 𝑛
 positive integers, as well as an integer parameter 𝑘
.

While the array has at least 𝑘
 elements, you need to perform one of the following two types of operations on 𝑎
:

Remove 𝑎𝑘
 and add its value to your score, or
Remove 𝑎𝑚−𝑘+1
 and add its value to your score, where 𝑚
 is the length of 𝑎
 before this operation.
After removing an element, the remaining elements keep their relative order.

Your task is to determine the maximum possible score that can be obtained.

Input
Each test contains multiple test cases. The first line contains the number of test cases 𝑡
 (1≤𝑡≤104
). The description of the test cases follows.

The first line of each test case contains two integers 𝑛
 and 𝑘
 (1≤𝑘≤𝑛≤105
) — the length of 𝑎
 and the parameter.

The second line contains 𝑛
 integers 𝑎𝑖
 (1≤𝑎𝑖≤109
) — the elements of 𝑎.

It is guaranteed that the sum of 𝑛
 over all test cases does not exceed 105

Output
For each test case, output a single integer — the maximum score that can be obtained.

## My Notes / Approach:
Note
In the first test case, we can first remove 𝑎3=3
. The score becomes 3
, and the array becomes [1,2,4]
. Then we remove 𝑎2=2
, so the score becomes 5
, and the array becomes [1,4]
. Finally, we remove 𝑎2=4
, and the score becomes 9
. Now the length of the array is less than 𝑘=2
, so no more operations can be performed. It can be proven that the maximum score is 9

In the second test case, we can only perform one operation, either removing 𝑎1=3
 or 𝑎4=2
. Obviously, it is better to remove 𝑎1=3
 to get a score of 3