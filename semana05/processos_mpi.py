
from mpi4py import MPI


comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()
print ("Eu sou um processo (rank) ", rank," do grupo (size)",size)
MPI.Finalize()