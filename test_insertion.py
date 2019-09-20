def Insertion(a,n):
    for x in range(1,n):
        i=x-1
        j=a[x]
        while i>=0 and j<a[i]:
            a[i+1]=a[i]
            i=i-1
        a[i+1]=j

def Open_File(name):
    f = open (name,'r')
    lista = f.readlines()
    f.close()
    return  lista

def main():    
    A=list(map(int,Open_File('archivo.txt')))
    N=len(A)
    print("Original list:", A)
    Insertion(A,N)
    print("Insertion Sort result:", A)

main()

