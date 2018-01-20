# -*- coding: utf-8 -*-
import numpy as np
from numpy import *

#LU分解法
def printmat(mat,n):
    for i in range(n):
	for j in range(n):
	    print str(mat[i][j]),
	    print " ",
	print "\n"
	
def LU(A,n):
    L=[[0 for x in range(n)] for y in range(n)]
    U=[[0 for x in range(n)] for y in range(n)]
    for i in range(n,0,-1):
	for temp in range(n-i,n):
	    sumup = 0
	    for temp2 in range(n-i):
		sumup += L[temp][temp2] * U[temp2][n-i]
	    L[temp][n-i] = A[temp][n-i]-sumup

	    for temp in range(n-i+1,n):
		sumup = 0
		for temp2 in range(n-i):
		    sumup += L[n-i][temp2] * U[temp2][temp]
		U[n-i][temp] = (A[n-i][temp]-sumup) / float(L[n-i][n-i])

    for i in range(n):
	U[i][i] = 1
    print "L的矩阵为:"
    printmat(L,n)	
    print "U的矩阵为:"
    printmat(U,n)
    return (L,U)

def Solve(A,b,n):
    L=[[0 for x in range(n)] for y in range(n)]
    U=[[0 for x in range(n)] for y in range(n)]
    (L,U)=LU(A,n)
    Y=[0 for x in range(n)]
    X=[0 for x in range(n)]
    Y[0] = b[0] / float(L[0][0])
    for i in range(1,n):
	sumup = 0
	for tmp in range(0,i):
	    sumup += L[i][tmp]*Y[tmp]
	Y[i] = (b[i]-sumup) / float(L[i][i])
    X[n-1] = Y[n-1]
    for i in range(n-2,-1,-1):
	sumup = 0
	for tmp in range(i+1,n):
	    sumup += U[i][tmp] * X[tmp]
	X[i] = Y[i] - sumup
    return X

#雅考比迭代法
def jacobi(A, b):
    tolerance = 1e-4
    n = len(A)
    x = np.zeros(n)
    x1 = np.ones(n)
    iterations = 0
    diag = np.diag(A)
    remaining = A - np.diagflat(diag)
    while abs(x - x1).max() > tolerance:
        x1 = np.copy(x)
        x = (b - np.dot(remaining, x)) / diag
        iterations += 1
    print '迭代次数:',iterations
    return x
    

#高斯-赛德尔迭代法
def gauss_seidel(A, b):
    tolerance = 1e-4
    n = len(A)
    x = np.zeros(n)
    x1 = np.ones(n)
    iterations = 0
    while abs(x - x1).max() > tolerance and iterations < 25:
        x1 = np.copy(x)
        for i in range(0, n):
            x[i] = (b[i] - np.dot(A[i,0:i], x[0:i]) - np.dot(A[i, i+1:n], x[i+1:n])) / A[i, i]
        iterations += 1
    print '迭代次数:',iterations
    return x
    
   
#超松弛迭代法
def sor(A, b, w):
    tolerance = 1e-4
    n = len(A)
    x = np.zeros(n)
    x1 = np.ones(n)
    iterations = 0
    while abs(x - x1).max() > tolerance and iterations < 25:
        x1 = np.copy(x)
        for i in range(0, n):
            x[i] = w*(b[i] - np.dot(A[i,0:i], x[0:i]) - np.dot(A[i, i+1:n], x[i+1:n])) / A[i, i]
        iterations += 1
    print '迭代次数:',iterations
    return x
    
#生成矩阵
def matrix(n):
    b = np.arange(1,n+0.1,1)
    A = np.array([b for _ in range(n)])
    for i in range(n):
        A[i,i] = n**2
    return A,b.reshape([n,1])

n1 = [4,8,16,32]

for n in n1:
    print 'n=',n
    A,b = matrix(n)
    x = Solve(A,b,n)
    print "LU分解法:"
    print x
    x = jacobi(A,b)
    print '雅考比迭代法:'
    print unique(x)
    x = gauss_seidel(A, b)
    print '高斯-赛德尔迭代法:'
    print x
    print '超松弛迭代法:'
    w1 = [0.6,0.8,1.2,1.4]
    for w in w1:
        print 'w:',w
        x = sor(A, b, w)
        print x
    print '\n'
        
        
        
    
    
