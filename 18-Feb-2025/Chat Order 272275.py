# Problem: Chat Order - https://codeforces.com/problemset/problem/637/B

Eureka

Student

    student

Hi, Eureka

Spot any bugs or have feedback?
Exercises

    Tracks

    Onboarding Phase

​
​
Personal Completion
54 Exercises | 42 Solved | 78% Completion | 12 Available

Tue Feb 18
constructive algorithms data structures sortings
Array
Greedy
Medium
Chat Order
constructive algorithms data structures sortings
codeforces
1
Medium
Gas Station
Array, Greedy
leetcode
2
Mon Feb 17
Array
Hash Table
Union Find
Medium
Longest Consecutive Sequence
Array, Hash Table, Union Find
leetcode
5
Fri Feb 14
Hash Table
Math
String
Array Hash Table Simulation
Array
Medium
Integer to Roman
Hash Table, Math, String
leetcode
5
Medium
Rabbits in Forest
LeetCode
6
Medium
Walking Robot Simulation
Array Hash Table Simulation
leetcode
5
Easy
Check if All the Integers in a Range Are Covered
Array, Hash Table
leetcode
12
Thu Feb 13
Hash Table
Design
Array
Simulation
Math
String
Medium
Frequency Tracker
Hash Table, Design
leetcode
6
Medium
Find the Number of Distinct Colors Among the Balls
Array, Hash Table, Simulation
leetcode
7
Easy
The Two Sneaky Numbers of Digitville
Array, Hash Table, Math
leetcode
12
Easy
Isomorphic Strings
String
Leetcode
12
Wed Feb 12
Array
Hash Table
Math
Design
Randomized
String
Hashtable
Medium
Insert Delete GetRandom O(1)
Array, Hash Table, Math, Design, Randomized
leetcode
7
Medium
Majority Element II
Hash Table
leetcode
11
Medium
Find All Duplicates in an Array
Array, Hash Table
leetcode
11
Easy
Roman to Integer
String, Math, Hashtable
leetcode
11
Tue Feb 11
Hash Table
Design
Array
Simulation
Counting
Medium
Design Authentication Manager
Hash Table, Design
leetcode
7
Medium
Replace Elements in an Array
Array, Hash Table, Simulation
leetcode
7
Easy
Maximum Number of Pairs in Array
Array, Hash Table, Counting
leetcode
12
Mon Feb 10
Hash Table
String
Design
Array
Sorting
Medium
Design Underground System
Hash Table, String, Design
leetcode
8
Medium
Apply Discount Every n Orders
Array, Hash Table, Design
leetcode
8
Medium
4Sum II
Array, Hash Table
leetcode
10
Medium
Group Anagrams
Array, Hash Table, String, Sorting
leetcode
10
Fri Feb 07
Array
Hash Table
String
Counting
Divide and Conquer
Sorting
Bit Manipulation
Maths
Medium
Subdomain Visit Count
Array, Hash Table, String, Counting
leetcode
10
Easy
Find Words That Can Be Formed by Characters
Array, Hash Table, String, Counting
leetcode
11
Easy
Majority Element
Array, Hash Table, Divide and Conquer, Sorting, Counting
leetcode
13
Easy
Count the Number of Consistent Strings
Array, Hash Table, String, Bit Manipulation, Counting
leetcode
11
Easy
Contains Duplicate
Array, Hash Table, Sorting
leetcode
14
Medium
Same Differences
Array, Hash Table, Maths
codeforces
11
Thu Feb 06
Array
String
Array Simulation
Medium
Remove Comments
Array, String
leetcode
8
Medium
Sum of Even Numbers After Queries
Array Simulation
leetcode
11
Wed Feb 05
Hash Table
String
Counting
Easy
Check if One String Swap Can Make Strings Equal
Hash Table, String ,Counting
leetcode
13
Tue Feb 04
Array
string
Math
Implementation
implementation
Easy
Build Array from Permutation
Array
leetcode
13
Medium
Masking Personal Information
string
leetcode
12
Medium
Rearrange Array Elements by Sign
Array
leetcode
12
Easy
Grading Students
Math, Implementation
HackerRank
13
Easy
Lists
Array
hackerrank
12
Easy
Presents
Array, implementation
codeforces
13
Easy
Maximum Product of Three Numbers
Array
leetcode
12
Mon Feb 03
Array
String
brute force
strings
Medium
Non-decreasing Array
Array
leetcode
12
Easy
Keyboard Row
String
leetcode
13
Easy
Team
brute force
codeforces
13
Easy
Way Too Long Words
strings
codeforces
13
Fri Jan 31
Array
Two Pointers
String
SImulation
bruteforce
math
Easy
Find Common Characters
Array
LeetCode
13
Easy
Reverse String
Two Pointers, String
leetcode
13
Easy
Concatenation of Array
Array, SImulation
leetcode
13
Easy
Watermelon
bruteforce, math
codeforces
13
Medium
Escape The Ghosts
Array
leetcode
11
Easy
Check If Two String Arrays are Equivalent
Array
leetcode
13
Medium
Reverse Words in a String
String
leetcode
13
Thu Jan 30
Math
String
Easy
Division
Math
hackerrank
13
Easy
Convert the Temperature
Math
leetcode
13
Easy
Palindrome Number
Math
leetcode
13
Easy
What's Your Name ?
String
hackerrank
13
Easy
Longest Common Prefix
String
leetcode
12
Created and maintained by Kenenisa Alemayehu.

Problems | A2SV Hub

Eureka
18 Feb 2025 4:15 PM

0
from collections import defaultdict



names = []

for i in range(int(input())):
    name = input()  
    names.append(name)


dd = defaultdict(int)

for i in range(len(names)-1,-1,-1):
    dd[names[i]] += 1



for key in dd.keys():
    print(key)




    
​
