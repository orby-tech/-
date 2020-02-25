import numpy as np
a=[]
z=100000
for i in range(90000,z-1):
    
    for j in range (i+1,z):
        i2=i*i
        j2=j*j
        n1= pow((i2+j2), 0.5)
        if n1%1==0:
            a.append(i2)
            a.append(j2)
            print(i)
a=np.array(a)            
np.save(r'C:\Users\1\Desktop\example_1.npy', a)
b=[]
for i in range(1,2*z):
    b.append(i*i)
np.save(r'C:\Users\1\Desktop\example_2.npy', b)
