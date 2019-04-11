#!/bin/python

# Code to calculate the number of substrings of a string s
# String s only contains alphabets a to z, and its length cannot exceed 10000
# This code uses less memory even for very large s

def substringCalculator(s):
    
    init_s = str(s)
    l = len(init_s)

    if not init_s.isalpha():
        raise ValueError
    elif l>10000:
        raise ValueError
    
    result = 0
    
    for i in range(1,l+1): # Length of substring
        subs = set()
        for j in range (0,l-i+1): # First character of substring
            subs.add(s[j:j+i])
        result += len(subs)
        if '' in subs:
            result -= 1

    return result

if __name__ == '__main__':
    
    s = raw_input()
    result = substringCalculator(s)
    print result

