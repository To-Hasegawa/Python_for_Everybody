#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
6.5 Write code using find() and string slicing (see section 6.10)
to extract the number at the end of the line below. 
Convert the extracted value to a floating point number 
and print it out.
"""
text = "X-DSPAM-Confidence:    0.8475";
s=text.find(":")
#print(s)

num = text[s+1:]
#print(num)

num = num.strip()
num=float(num)
print(num)