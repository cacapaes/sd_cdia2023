from numba import config, njit, threading_layer
import numpy as np
from numba import set_num_threads, prange

# set the threading layer before any parallel target compilation
config.THREADING_LAYER = 'threadsafe'

@njit(parallel=True)
def tarefa(a):
    for i in prange(a):
        print("Eu sou uma thread executando...#",i)

set_num_threads(4)
tarefa(100)

print("Threading layer chosen: %s" % threading_layer())
