import numpy
from mpi4py import MPI

a = numpy.array(['O','l'])

if MPI.COMM_WORLD.rank == 0:
        print("send: ",a)
        MPI.COMM_WORLD.Send(a, dest = 1)
else:
        MPI.COMM_WORLD.Recv(a, source = 0)
        print("receive: ",a)