#!/bin/python

# Script to test the code for finding number of unique substrings of a string

import random
import string
import subs
import subs2

# Test string composed only of alphabets
s1 = ''
for i in range(0,10000):
    s1 += random.choice(string.ascii_letters)

print subs2.substringCalculator(s1)
print subs.substringCalculator(s1)

# Test string composed of alphanumeric characters (should raise an error)
s2 = ''
for i in range(0,100):
    s2 += random.choice(string.printable)

print subs2.substringCalculator(s2)
print subs.substringCalculator(s2)
