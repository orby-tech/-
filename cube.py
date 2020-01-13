from tkinter import Tk, Canvas, Frame, BOTH 
import time
import math
from tkinter import *

x=[0, 0, 0, 0]
y=[0, 0, 0, 0, 0, 0, 0, 0]
R=100.0
wi=700
he=700
a=0
spe=0.001
const= 1.4
par=['','','']


  

root=Tk()

root.title("куб ебат")
c = Canvas(root, width=wi, height=he, bg='white')









fr1 = Entry(root,width=10)
fr2 = Entry(root,width=10)
fr3 = Entry(root,width=10)
fr1.place(x=5, y=5)
fr2.place(x=5, y=25)
fr3.place(x=5, y=45)

def getText(par):
    o1=fr1.get()
    o2=fr2.get()
    o3=fr3.get()
    return o1, o2, o3

b_get = Button(root, text="ввести новые параметры", command=getText(par))
b_get.pack()
b_get.place(x=100, y= 23)
if par[0]!='':
	R= float (par[0])
c.pack()
c.place(y=0)
line1= c.create_line(x[0],y[0],x[1],y[1],x[2],y[2],x[0],y[0])
line2= c.create_line(x[0],y[4],x[1],y[5],x[2],y[6],x[0],y[4])

line3=c.create_line(x[0],y[0],x[0],y[4])
line4=c.create_line(x[1],y[1],x[1],y[5])
line5=c.create_line(x[2],y[2],x[2],y[6])
line6=c.create_line(x[3],y[3],x[3],y[7])

for j in range(1,1000000):
	if par[0]!='':
		R= float (par[0])


	for i in range(0,4):
		a=j/100
		x[i] = 2*R+R*math.sin(a+math.pi/2*i)
		y[i] = 2*R+R*math.cos(a+math.pi/2*i)*math.cos(const)
		y[i+4]= (2+2*math.sin(const))*R+R*math.cos(a+math.pi/2*i)*math.cos(const)
	c.coords(line1,x[0],y[0],x[1],y[1],x[2],y[2],x[3],y[3],x[0],y[0])
	c.coords(line2,x[0],y[4],x[1],y[5],x[2],y[6],x[3],y[7],x[0],y[4])

	c.coords(line3,x[0],y[0],x[0],y[4])
	c.coords(line4,x[1],y[1],x[1],y[5])
	c.coords(line5,x[2],y[2],x[2],y[6])
	c.coords(line6,x[3],y[3],x[3],y[7])

	c.update()
	time.sleep(spe)
	i=0

root.mainloop()