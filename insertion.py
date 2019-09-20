N=int(input("Tamano de la lista: "))
A=[int(input("Inserte un numero: ")) for x in range(N)]

for x in range(1,N):
        i=x-1
        j=A[x]
        while i>=0 and j<A[i]:
            A[i+1]=A[i]
            i=i-1
        A[i+1]=j

print (A)

