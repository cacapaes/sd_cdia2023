import sys
import os

idproc = os.fork()
if idproc == 0:
     fpid = os.getpid()
     while(True):
        print("Eu sou o proceso filho e meu pid",fpid)
else:
     ppid = os.getpid()
     while(True):
        print("Processo pai",ppid,"aguardando o processo filho",idproc)
     
