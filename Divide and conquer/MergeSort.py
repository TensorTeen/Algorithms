import os
import time


os.chdir("C:\Akshay")
with open("test.txt","r") as f:
    givenArr = [int(x) for x in f]
sort_l = []
c = 0
def merge(l,r):
    tmp = []
    i,j = 0,0
    n1,n2 = len(l), len(r)
    while i < n1 and j < n2:
        if l[i] <= r[j]:
            tmp.append(l[i])
            i += 1
        else:
            global c
            c+=(n1-i)
            #print(l,r)
            tmp.append(r[j])
            j += 1
    for x in range(i,n1):
        tmp.append(l[x])
    for x in range(j,n2):
        tmp.append(r[x])    

    return tmp 

def sort(l):
    if len(l) == 1:
        return l
    elif len(l) == 2:
        if l[0] > l[1] :
            #print("add 1")
            global c
            c+=1
            return [l[1],l[0]]
        else:
            return l
    else :
        n = len(l)//2
        arr_l = sort(l[:n])
        arr_r = sort(l[n:])
        Merged = merge(arr_l,arr_r)
        return Merged
start = time.time()
sort_l = sort(givenArr)
stop1 = time.time()
print(stop1-start)
