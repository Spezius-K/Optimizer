# -*- coding: utf-8 -*-
"""
Created on Wed Jan 12 14:41:25 2022

@author: robin
"""

from scipy.interpolate import interp1d
import numpy as np
import matplotlib.pyplot as plt
import random as rd

#------------------------------------------------------------------
#Parameter
x1 = np.linspace(1, 6, num=50, endpoint=True)
x2 = np.linspace(0, 4, num=50, endpoint=True)
x3 = np.linspace(-6, 5, num=50, endpoint=True)
x4 = np.linspace(-4, 6, num=50, endpoint=True)
x5 = np.linspace(-4, 4, num=50, endpoint=True)

Anzahl_Testpunkte=100
iterationen=100
Schrittweite=0.95


#------------------------------------------------------------------
#Sensitivitätsanalyse

#------------------------------------------------------------------
#Funktionen
def fun1(x1,x2,x3,x4,x5):
    y = 1.5 + (x1-3.2)**2 + (x2-1.8)**2 + 3*np.cos(1.2*x3) + 0.2*(x4-0.5*x3)**2 + 0.3*x3 + 2*np.sin(3*x2) + np.cos(2*x5)
    return y


param=[x1,x2,x3,x4,x5]
#%%
def Sensi():
    Designarray=np.zeros((2,Anzahl_Testpunkte),dtype=object)
    # Best10design=[]
    for n in range(Anzahl_Testpunkte):
        Design=[]
        for i in param:
            rx=rd.uniform(min(i),max(i))
            Design.append(rx)
            # print(Design)
        Designarray[0,n]=Design
        x1,x2,x3,x4,x5=Design
        Designarray[1,n]=(fun1(x1,x2,x3,x4,x5))
        Bestdesign=Designarray[0,np.argmin(Designarray[1])]
    # Best10design=sorted(Designarray[1])[slice(10)]
    # sorted(Designarray)[slice(10)]
    return Designarray,Bestdesign


Sensi()
# Designlist=np.array([[1,2,3],[45,56,67]])

#%%
#--------------------------------------------------------------------
#Schleife
k=1
i=0
testpunkt=Sensi()[1]
while i<iterationen:
  y1=fun1(testpunkt[0]+k,testpunkt[1],testpunkt[2],testpunkt[3],testpunkt[4])
  y2=fun1(testpunkt[0]-k,testpunkt[1],testpunkt[2],testpunkt[3],testpunkt[4])
  y3=fun1(testpunkt[0],testpunkt[1]+k,testpunkt[2],testpunkt[3],testpunkt[4])
  y4=fun1(testpunkt[0],testpunkt[1]-k,testpunkt[2],testpunkt[3],testpunkt[4])
  y5=fun1(testpunkt[0],testpunkt[1],testpunkt[2]+k,testpunkt[3],testpunkt[4])
  y6=fun1(testpunkt[0],testpunkt[1],testpunkt[2]-k,testpunkt[3],testpunkt[4])
  y7=fun1(testpunkt[0],testpunkt[1],testpunkt[2],testpunkt[3]+k,testpunkt[4])
  y8=fun1(testpunkt[0],testpunkt[1],testpunkt[2],testpunkt[3]-k,testpunkt[4])
  y9=fun1(testpunkt[0],testpunkt[1],testpunkt[2],testpunkt[3],testpunkt[4]+k)
  y10=fun1(testpunkt[0],testpunkt[1],testpunkt[2],testpunkt[3],testpunkt[4]-k)

  if y1<y2 and y1<y3 and y1<y4 and y1<y5 and y1<y6 and y1<y7 and y1<y8 and y1<y9 and y1<y10:
      testpunkt=(testpunkt[0]+k,testpunkt[1],testpunkt[2],testpunkt[3],testpunkt[4])

  if y2<y1 and y2<y3 and y2<y4 and y2<y5 and y2<y6 and y2<y7 and y2<y8 and y2<y9 and y2<y10:
      testpunkt=(testpunkt[0]-k,testpunkt[1],testpunkt[2],testpunkt[3],testpunkt[4])

  if y3<y1 and y3<y2 and y3<y4 and y3<y5 and y3<y6 and y3<y7 and y3<y8 and y3<y9 and y3<y10:
      testpunkt=(testpunkt[0],testpunkt[1]+k,testpunkt[2],testpunkt[3],testpunkt[4])

  if y4<y1 and y4<y2 and y4<y3 and y4<y5 and y4<y6 and y4<y7 and y4<y8 and y4<y9 and y4<y10:
      testpunkt=(testpunkt[0],testpunkt[1]-k,testpunkt[2],testpunkt[3],testpunkt[4])

  if y5<y1 and y5<y2 and y5<y3 and y5<y4 and y5<y6 and y5<y7 and y5<y8 and y5<y9 and y5<y10:
      testpunkt=(testpunkt[0],testpunkt[1],testpunkt[2]+k,testpunkt[3],testpunkt[4])

  if y6<y1 and y6<y2 and y6<y3 and y6<y4 and y6<y5 and y6<y7 and y6<y8 and y6<y9 and y6<y10:
      testpunkt=(testpunkt[0],testpunkt[1],testpunkt[2]-k,testpunkt[3],testpunkt[4])

  if y7<y1 and y7<y2 and y7<y3 and y7<y4 and y7<y5 and y7<y6 and y7<y8 and y7<y9 and y7<y10:
      testpunkt=(testpunkt[0],testpunkt[1],testpunkt[2],testpunkt[3]+k,testpunkt[4])

  if y8<y1 and y8<y2 and y8<y3 and y8<y4 and y8<y5 and y8<y6 and y8<y7 and y8<y9 and y8<y10:
      testpunkt=(testpunkt[0],testpunkt[1],testpunkt[2],testpunkt[3]-k,testpunkt[4])

  if y9<y1 and y9<y2 and y9<y3 and y9<y4 and y9<y5 and y9<y6 and y9<y7 and y9<y8 and y9<y10:
      testpunkt=(testpunkt[0],testpunkt[1],testpunkt[2],testpunkt[3],testpunkt[4]+k)

  if y10<y1 and y10<y2 and y10<y3 and y10<y4 and y10<y5 and y10<y6 and y10<y7 and y10<y8 and y10<y9:
      testpunkt=(testpunkt[0],testpunkt[1],testpunkt[2],testpunkt[3],testpunkt[4]-k)


  k=k*Schrittweite
  i+=1

print('Optimum hat die Parameter bei\n x1: '+str(testpunkt[0])+
'\n x2: '+str(testpunkt[1])+'\n x3: '+str(testpunkt[2])+'\n x4: '+str(testpunkt[3])+'\n x5: '+str(testpunkt[4]))