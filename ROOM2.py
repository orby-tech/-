def po(c,v,b):
    return pow(c+v+b, 0.5)%1
def dub(c):
    return 2*c+1
i_sit=True
j_sit=True
k_sit=True
i=1
j=0
k=0
while i_sit==True:
    j=i+1
    i2=i*i
    while j_sit==True:
        j2=j*j
        if dub(j)<=i2:
            k=j+1
            while k_sit==True:
                k2=k*k
                    
                if dub(k)<=i2:
                        
                        if po(i2,j2,k2)==0:
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
