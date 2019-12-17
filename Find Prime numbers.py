#n개의 소수 찾기

import math as mt

MAX = 10000

prime=[True for i in range(MAX+1)] 
  
def SieveOfErastosthenes(): 
      
    prime[1]=False
      
    for p in range(2,mt.ceil(mt.sqrt(MAX))): 
        #if prime[p] is not changes, then it is a prime 

        if prime[p]: 
            #set all multiples of p to non-prime 
            for i in range(2*p,MAX+1,p): 
                prime[i]=False
           
def solve(n): 
    count,num=0,1
      
    prod=[]
    while count<n: 
        if prime[num]: 
            prod.append(num) 
              
            count+=1
        num+=1
    print(prod)
  
SieveOfErastosthenes() 
  
