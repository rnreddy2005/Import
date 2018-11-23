import pandas as pd
import numpy as np
import math as mt

#create the sample data frame as below.
df = pd.DataFrame({"HPI":[80,90,70,60],"Int_Rate":[2,1,2,3], "IND_GDP":[50,45,45,67]})
#print(df) 

#read the column name for which we have to calculate entropy.
a=np.array(df["Int_Rate"]) 
# calculate total number of elements in the array
tot=len(a)
# identify the unique values and the count of each value from the array
unique_elements, counts_elements = np.unique(a, return_counts=True)
#create an array of unique elements and their counts
un=np.asarray((unique_elements, counts_elements))

#count the number of unique elements in the array
l=len(un[0])
#below logic to calculate entropy of the array
i=0
v=0
while i<l:
    p=un[1][i]
    #print(un[0][i],p,tot,)
    f=int(un[1][i])/(tot*1.0)
    v+=(f*mt.log(f,2))
    i+=1
e=-1*v
#print the entropy of the given array
print(e)
