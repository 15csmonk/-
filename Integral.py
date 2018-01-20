#!/usr/bin/python
# -*- coding: utf-8 -*-

def integral(a, b, n, func):
    h = (b - a)/float(n)
    xk = [a + i*h for i in range(1, n)]
    return h/2 * (func(a) + 2 * sum_fun_xk(xk, func) + func(b))

def sum_fun_xk(xk, func):
    return sum([func(each) for each in xk])

if __name__ == "__main__":    
    func = lambda x: 1/(1+x**2)
    a, b = 0,1 #a为积分下限，b为积分上限
    n = 10000  #积分分为n等份
    print "Integral method:",integral(a, b, n, func)
