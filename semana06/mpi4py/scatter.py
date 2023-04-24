from mpi4py import MPI
import time
import numpy as np

tamanho = 10

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

if rank==0:
    time.sleep(5)
    data = np.random.randint(0,100,10*size)
    print("Processo ",rank," enviando o dado: ",data)
else:
    data = None

data = comm.scatter(data, root=0)
print("O processo de rank ",rank, "recebeu o dado: ",data)
MPI.Finalize()

