import numpy as np
import pandas as pd
#lis = np.identity(4)
lis=[[1,0,1,1],[1,1,0,1],[0,1,1,0],[1,1,0,0]]
res=[]
print(lis)
val=0
n=len(lis)
i=0
while i < n:
    j=0
    while j<n:
        if (i==0 and j ==0 ) :val=lis[1][1] + lis[0][1] + lis[1][0]
        elif(i == n-1 and j==n-1): val=lis[i-1][j-1] + lis[i-1][j] + lis[i][j-1]
        elif(i==0 and j>0 and j< n-1): 
                if j>1: x=j-1 
                else: x=1
                val=lis[0][j-1]+lis[0][j+1]+lis[1][j-1]+lis[1][j]+lis[1][j+1]
        elif(i==0 and j==n-1): val=lis[0][j-1]+lis[1][j]+lis[1][j-1]
        elif(j==0 and i>0 and i< n-1): 
                if i>1: x=i-1 
                else: x=1
                val=lis[0][i-1]+lis[0][i+1]+lis[i-1][1]+lis[1][i]+lis[1][i+1]
        elif(i==n-1 and j==0): val=lis[j-1][0]+lis[j][1]+lis[j-1][1]
        #elif(i==n-1 and j==n-1): val=lis[i-1][j-1]+lis[i-1][j]+lis[i][j-1] 
        elif(i!=n-1 and j!=n-1): val=lis[i-1][j-1]+lis[i-1][j]+lis[i-1][j+1]+lis[i][j-1]+lis[i][j+1]+lis[i+1][j-1]+lis[i+1][j]+lis[i+1][j+1]
        elif(i==n-1 and j<n-1): val= lis[i][j-1] + lis[i][j+1] + lis[i-1][j-1]+lis[i-1][j]+lis[i-1][j+1]
        else:  val= lis[i-1][j] + lis[i+1][j] + lis[i-1][j-1]+lis[i][j-1]+lis[i+1][j-1]
        #print(val)
        if(val%2==0) : l=1 
        else: l=0
        res.append(l)
        #print(i,j,val)
        j+=1
    #print(lis[i])
    i+=1
a=np.array(res)
x = a.reshape(n,n)
print("\n")
print(x)
print("\n")
