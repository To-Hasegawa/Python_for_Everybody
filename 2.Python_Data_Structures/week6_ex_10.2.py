#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
10.2 Write a program to read through the mbox-short.txt 
and figure out the distribution by hour of the day for 
each of the messages. 
You can pull the hour out from the 'From ' line by finding 
the time and then splitting the string a second time 
using a colon.

From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

Once you have accumulated the counts for each hour, 
print out the counts, sorted by hour as shown below.
"""
name = input("Enter file:")
handle = open(name)

lst=list()
counts =dict()

for line in handle:
    if not line.startswith("From ") : 
        continue
    #print(line.strip())
    time = line.split()
    time = time[5]
    #print(time)
    hp = time.find(":")
    h = time[:hp]
    
    lst.append(h)

for i in lst:
    counts[i]=counts.get(i,0) + 1

lines = list()
for key,val in counts.items():
    newtup = (key, val)
    lines.append(newtup)
    #lines = sorted(lines, reverse=False)
    ines.sort()

for k,v in lines:
    print(k,v)