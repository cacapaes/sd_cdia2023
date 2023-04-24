from mpi4py import MPI
import time

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank==0:
	print("Estou atrasado para a barreira! Processo",rank)
	time.sleep(10)

comm.Barrier()
print("Passei pela barreira! Processo",rank)
MPI.Finalize()




	
