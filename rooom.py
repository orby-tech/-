from numba import jit
@jit

def po(c,v):
    return pow(c+v, 0.5)%1
def dub(c):
    return 2*c+1

i_sit=True
j_sit=True
k_sit=True
i=137902
j=0
k=0
while i_sit==True:
    j=i+1
    i2=i*i
    while j_sit==True:
        j2=j*j
        if dub(j)<=i2:
            if i%3==0 and j%3==0:
                j+=1
                break
            elif i%3!=0 and j%3!=0:
                j+=1
                break
            if i%4==0 and j%4==0:
                j+=1
                break
            elif i%4!=0 and j%4!=0:
                j+=1
                break
            if po(i2,j2)==0:
                k=j+1
                while k_sit==True:
                    k2=k*k
                    if i%2==0 and j%2==0 and k%2==0:
                        k+=1
                        break
                    if i%3==0 and j%3==0 and k%3==0:
                        k+=1
                        break
                    
                    if dub(k)<=i2:
                        if po(i2,k2)==0 and po(k2,j2)==0:
                            print(i,j,k)
                            if po(i2+j2,k2)==0:
                                print(i2,j2,k2, "lgjsdfkjghldsfkgl")
                                i_sit=False
                                j_sit=False
                                k_sit=False
                            

                    else:
                        break
                    k+=1
        else:
            break
        j+=1
    print(i)
    i+=1
