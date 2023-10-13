import os
import time


os.chdir("C:\Akshay")
with open("test2.txt","r") as f:
    givenArr = [int(x) for x in f]
c = 0


def quickSort(arr,l,r):
    n = r-l
    if n <= 1:
        return arr[l:r]
    else:
        global c
        c+=r-l-1
        i = partition(arr,l,r)
        return quickSort(arr,l,i-1) + [arr[i-1]] + quickSort(arr,i,r)

def partition(arr,l,r):
    p = arr[r-1]
    arr[l],arr[r-1] = arr[r-1],arr[l]
    i = l + 1
    for j in range(l+1,r):
        if arr[j] < p:
            arr[j],arr[i] = arr[i],arr[j]
            i+=1
    arr[l],arr[i-1] = arr[i-1],arr[l]
    return i

start = time.time()
arr = quickSort(givenArr,0,len(givenArr))
stop = time.time()
print(stop-start,c)
