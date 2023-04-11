import multiprocessing
from time import sleep 
from multiprocessing import Process


def print_func(id):
    for i in range(100):
        print("Eu sou um processo! ",id)
        sleep(5)

if __name__ == "__main__":  # confirms that the code is under main function
    print("Number of cpu : ", multiprocessing.cpu_count())
    procs = []
    proc1 = Process(target=print_func, args=(1,))
    procs.append(proc1)
    proc2 = Process(target=print_func, args=(2,))
    procs.append(proc2)
    proc1.start()
    proc2.start()