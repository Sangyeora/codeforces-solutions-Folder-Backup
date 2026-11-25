# 2253A. The Best Card

## Difficulty: Easy

## Platform: Codeforces

## Problem Link
[View Problem](https://codeforces.com/problemset/problem/2253/A)

## Solved On
25 Nov 2026 at 11:35 pm

A. The Best Card
time limit per test2 seconds
memory limit per test512 megabytes
In a card game, there are 𝑛
 cards with values 2,3,4,…,𝑛+1
.

To determine which of two cards with values 𝑥
 and 𝑦
 wins, apply the following rules:

if one of the numbers 𝑥
 and 𝑦
 is divisible by the other, the card with the smaller value wins;
otherwise, the card with the larger value wins.
For example, between cards 2
 and 6
, card 2
 wins because 6
 is divisible by 2
. Between cards 4
 and 6
, card 6
 wins because neither of these numbers is divisible by the other.

Determine whether there exists a card that wins against every other card.



## My Notes / Approach:
Input
The first line contains an integer 𝑡
 (1≤𝑡≤104
) — the number of test cases.

The only line of each test case contains an integer 𝑛
 (2≤𝑛≤2⋅105
) — the number of cards in the game.

Additional constraints on the input:

the sum of 𝑛
 over all test cases does not exceed 3⋅106
.
Output
For each test case, print YES if there is a card that wins against all other cards, and NO otherwise.

Each letter may be printed in either case. For example, YES, yes, and yEs are all recognized as a positive answer.