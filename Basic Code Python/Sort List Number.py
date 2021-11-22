Data = [-90,20,-1,-100,5,26,7,5,-93,10]
Data.sort()
print('Sorted list (in Ascending):', Data[::]) #Ascending
print('Sorted list by the least number:' ,Data[0]) #nilai terkecil
print('Sorted list by the largest number:' , Data[-1]) #nilai terbesar
Data.sort(reverse=True)
print('Sorted list (in Descending):', Data[::] ) #Descending