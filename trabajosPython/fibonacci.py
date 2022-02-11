

a=0
b=1
c=0
contador=0
numeros=input("Dame la cantidad de numeros que quieres visualizar: ")
numeros=int(numeros)
print(a)
def fibo(contador,numeros,a,b,c):
    if contador<numeros:
        print(b)
        c=b
        b=b+a
        a=c
        
        
        contador+=1
        fibo(contador,numeros,a,b,c)
    
fibo(contador,numeros,a,b,c)