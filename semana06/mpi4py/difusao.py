from mpi4py import MPI
import time

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank==0:
    time.sleep(5)
    data = 100
    print("Processo ",rank," enviando o dado: ",data)
else:
    data = None

data = comm.bcast(data, root=0)
print("O processo de rank ",rank, "recebeu o dado: ",data)
MPI.Finalize()

