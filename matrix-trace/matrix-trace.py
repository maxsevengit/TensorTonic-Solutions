import numpy as np

def matrix_trace(A):
    """
    Compute the trace of a square matrix (sum of diagonal elements).
    """
    sum = 0
    a = len(A[0])
    for i in range (0,a):
        for j in range(0,a):
            if(i==j):
                sum+=A[i][j]


    return sum           