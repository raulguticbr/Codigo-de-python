
def Fibonachi():
    a=0
    b=1
    c=0
    contador=0
    numeros=input("Dame la cantidad de numeros que quieres visualizar: ")
    numeros=int(numeros)
    def fibo(numeros):  
        global a,b,c,contador
        if contador<numeros:
            print(a)
            c=a
            a=a+b
            b=c   
            contador+=1
            fibo(numeros)
        
    fibo(numeros)