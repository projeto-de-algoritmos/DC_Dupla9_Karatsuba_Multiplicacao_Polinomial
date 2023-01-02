import timeit as ti
import numpy as np

def simpleMultiply(A, B, m, n):
    prod = [0] * (m + n - 1);
    for i in range(m):
        for j in range(n):
            prod[i + j] += A[i] * B[j];
    return prod

def multiplyDivideAndConquer(p, q, n):
    if (n == 1):
        return [p[0] * q[0]]
    df= n / 2
    d = int(df)
    pHigh = np.empty(d, dtype=float)
    qHigh = np.empty(d, dtype=float)
    pLow = np.empty((d-n%2), dtype=float)
    qLow = np.empty((d-n%2), dtype=float)
    for i in range(d):
        pHigh[i] = p[i+d]
        qHigh[i] = q[i+d]
        pLow[i] = p[i]
        qLow[i] = q[i]
    lowPQ = multiplyDivideAndConquer(pLow, qLow, d)
    lowPHighQ = multiplyDivideAndConquer(pLow, qHigh, d)
    lowQHighP = multiplyDivideAndConquer(pHigh, qLow, d)
    highPQ = multiplyDivideAndConquer(pHigh, qHigh, d)
    pq = np.empty((2*n) - 1, dtype=float)
    for i in range(n-1):
        pq[i] = pq[i] + lowPQ[i]
        pq[i+d] = pq[i+d] + lowPHighQ[i] + lowQHighP[i]
        pq[i+2*d] = pq[i+2*d] + highPQ[i]
    return pq

A = [1,1,1,1];
B = [2,7,5,3];
start = ti.default_timer()
result = simpleMultiply(A, B, len(A), len(B))
stop = ti.default_timer()
print("Resultado da multiplicação simples")
print(result)
print("Tempo de execução com multiplicação simples", stop - start)

start = ti.default_timer()
result = multiplyDivideAndConquer(A, B, len(A))
stop = ti.default_timer()
print("Resultado da Multiplicação com Dividir e Conquistar")
print(result)
print("Tempo de execução com multiplicação com dividir e conquistar", stop - start)