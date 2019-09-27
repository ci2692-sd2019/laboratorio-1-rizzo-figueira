import sys
import time
import random
import Sorts

def Crear_arreglo_random(n):
    A=[random.randint(1,1000) for i in range(n)]
    return A

def main():
    N,s=int(sys.argv[2]),sys.argv[1]
    Arr= Crear_arreglo_random(N)
    if s=="InsertionSort":
        inicio =time.time()
        Sorts.InsertionSort(Arr,N)
        fin=time.time()
    elif s=="MergeSort":
        inicio=time.time()
        Sorts.MergeSort(Arr,0,N-1)
        fin=time.time()

    tiempoTranscurrido=(fin-inicio)*1000
    print(s,N,tiempoTranscurrido)

main()
