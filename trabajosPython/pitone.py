
import math
array=[6,7,34,8,5,9,0,1,2,4,10,11,12,13,14,3]
i=0

print(array)
while i<len(array):
    j=i
    while j<len(array):
        if array[i]>array[j]:
          aux=array[i]  
          array[i]=array[j]
          array[j]=aux

        j+=1    
    
       
    i+=1
print(array)

print("segunda parte de la actividad")

num_buscar=input("dame el numero a buscar:  ")
num_buscar=int(num_buscar)
mitad=len(array)/2
mitad=round(mitad)
tope_derecha=len(array)
tope_izda=0


def bucle(num_buscar,mitad,tope_derecha,tope_izda):
  
  if array[mitad]==num_buscar:
    print("El numero buscado esta en la posicion "+str(mitad))
    
  else:
    if num_buscar > mitad:
      tope_izda=mitad
      mitad=(mitad+round((tope_derecha-mitad)/2))
      mitad=round(mitad)
      bucle(num_buscar,mitad,tope_derecha,tope_izda)
      
    else:
      if num_buscar<mitad:
        tope_derecha=mitad    
        mitad=((mitad-tope_izda)/2)
        mitad=round(mitad)
        bucle(num_buscar,mitad,tope_derecha,tope_izda)
      else:
            print("El numero que has introducido no existe")
    
bucle(num_buscar,mitad,tope_derecha,tope_izda)