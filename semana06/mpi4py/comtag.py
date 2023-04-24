import numpy
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()



if rank==0:
	shared_data1 = 23
	comm.send(shared_data1,dest=1,tag=1)
	shared_data2 = 34
	comm.send(shared_data2,dest=1,tag=2)
if rank==1:
	recv_data1 = comm.recv(source=0,tag=2)
	print(recv_data1)
	recv_data2 = comm.recv(source=0,tag=1)
	print(recv_data2)