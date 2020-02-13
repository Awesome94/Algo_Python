## Dynamic Programming.
Dynamic programing is a type of algorithm like brute force, divide and conquer and greedy algorithms. 
Dynamic programing and recursion go hand in hand.

#### Why dynamic programing?
Dynamic programing can help you solve recursive problems without maxing out your memory using the various approaches that come with dynamic programing and these include:
1. Top down approach.
2. Bottom Up approach.

### Bottom Up approach:
As the name suggests, the bottom up approach involves starting from the least most computation going up. Hence, the value of the current value n is determined by the preivious value of (n-1). 

below is an algorithm in python to find out how many denominations can be used to represent and given number(currency) n under the following conditions.
If the n = 25, should return 1
if n = 10, should return 1
if n == 5 should return 1 
if n < 5, should return n 

_example_
given n == 14 should return 5
step 1 14

### Top down approach:
As suggested in the name, the Top down approach starts from the top most value hence breaking it down into subproblems that can be computed to come  to the desired solution
