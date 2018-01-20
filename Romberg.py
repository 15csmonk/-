#!/usr/bin/python
# -*- coding: utf-8 -*-

import math;
def funct(x):
    return 1.0/(1+pow(x,2))

def modifier(T_n,T_two_n,C_S_R):
    tmp=(pow(4,C_S_R)*T_two_n-T_n)/float(pow(4,C_S_R)-1)
    return tmp

def printAns(ls):
    for x in range(len(ls)):
        if(x==17):    
            print "Romberg method:" "%-10.16f" % ls[x]

def  Romberg(down,up,right):
     T=[0  for i in range(right+3)]
     T[0]=(funct(up)+funct(down))*(up-down)/2.0
     for tmp in range(1,len(T)):
        sumup=0
        for x in range(1,pow(2,tmp-1)+1):
            sumup+=funct(down+(2*x-1)*(up-down)/(2.0*pow(2,tmp-1)))
        T[tmp]=0.5*T[tmp-1]+(up-down)*sumup/(2.0*pow(2,tmp-1))
     printAns(T)

Romberg(0,1,15)

