# -*- coding: utf-8 -*-
def computepay(h,r):
    if h <40:
        pay = h*r
    else:
        pay = 40*r + (h-40)*r*1.5
    return pay

h = input("Enter Hours:")
r = input("Enter Rate:")

h=float(h)
r=float(r)

p = computepay(h,r)
print("Pay",p)

