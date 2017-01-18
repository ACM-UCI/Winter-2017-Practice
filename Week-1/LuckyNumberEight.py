#!/bin/python3

import sys
n = int(input().strip())
number = input().strip()

# your code goes here
div = 8
countMod = 10**9 + 7
modCounts = [0 for i in range(div)]
modCounts[0] = 1

for i in range(n):
    #print(modCounts)
    digit = int(number[i])
    newModCounts = [modCounts[i] for i in range(div)]
    for j in range(div):
        newMod = (10*j + digit) % div
        #print (j, newMod)
        newModCounts[newMod] = (newModCounts[newMod] + modCounts[j]) % countMod
    modCounts = newModCounts
    
print(modCounts[0] - 1) # Remove empty subsequence
