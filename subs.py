#!/bin/python

# Code to calculate the number of substrings of a string s
# String s only contains alphabets a to z, and its length cannot exceed 10000
# This code may give memory error for very large s

def substringCalculator(s):
    
    init_s = str(s)
    l = len(init_s)

    if not init_s.isalpha():
        raise ValueError
    elif l>10000:
        raise ValueError
    
    subs = set()

    for i in range(0,l): # First character of substring
        for j in range(l,0,-1): # Last character of substring
             subs.add(init_s[i:j])
    
    result = len(subs)
    if '' in subs:
        result -= 1

    return result

if __name__ == '__main__':
    
    s = raw_input()
    result = substringCalculator(s)
    print result

