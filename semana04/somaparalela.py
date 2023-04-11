from numba import config,prange, njit, threading_layer
import numpy as np
import numpy.random as np
from time import perf_counter

@njit(parallel=True, cache=True)
def parallel_sum(A):
    sum = 0.0
    for i in prange(A.shape[0]):
        sum += A[i]

    return sum

if __name__ == "__main__":
    vetor = np.randint(0,100,100000)
    soma = parallel_sum(vetor)
    t1_start = perf_counter()
    soma = parallel_sum(vetor)
    t1_stop = perf_counter()
    print("Resultado = ",soma)
    print("Tempo de execução em segundos: ",t1_stop-t1_start)