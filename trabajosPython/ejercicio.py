array=[6,7,34,8,5,9,0,3]
i=0
while i<len(array):
    if array[i]>array[i+1]:
       aux1=array[i] 
       aux2=array[i+1]
       array[i]=aux2
       array[i]=aux1
       
    
       
    i+=1
print(array)