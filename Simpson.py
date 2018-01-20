#!/usr/bin/python
# -*- coding: utf-8 -*-
#simpson 法计算积分
from math import *
def func(x):
    return 1/(1+x**2)#定义被积分函数
def Get_N(a,b,width):# width为步长
    N=int((b-a)/width + 1)
    if N%2 == 0:
        N=N+1
    return N

def GenerateData(a,b,n,width):
    datas = []
    r=a
    for i in range(0,n):
        datas.append(func(r))
        r = r+width
    return datas

def simpson_integral(datas,width,n):
    sum = datas[0]+datas[n-1]
    for i in range(2,n):
        if i%2== 0:
            sum = sum +4*datas[i-1]
        else:
            sum = sum +2*datas[i-1]
    return sum*width/3.0

if __name__ == "__main__":
    a=0.0 #积分上限
    b=1.0 #积分下限
    width=0.000000625
    N=Get_N(a,b,width)
    datas = GenerateData(a,b,N,width)
    print "simpson method:",simpson_integral(datas,width,N)
