#!/usr/bin/python
# -*- coding: utf-8 -*-
import math  
def fun(x):  
    return 1/(1+x**2)  
  
def main():  
    GauFive={0.9061798459:0.2369268851,0.5384693101:0.4786286705,0:0.5688888889}  
    GauSum=0.0  
    a=0.0  
    b=1.0 
    for key,value in GauFive.items():  
        GauSum+=fun(((b-a)*key+a+b)/2)*value  
        if(key>0):  
            GauSum+=fun(((a-b)*key+a+b)/2)*value  
    GauSum=GauSum*(b-a)/2  
    print "Gauss-Legendre:",GauSum  

main() 
