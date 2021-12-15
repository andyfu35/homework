import numpy as np
from tkinter import *
from tqdm import trange

root = Tk()
root.geometry('+200+200')
mycanvas = Canvas(root, width=1000, height=1000)
mycanvas.pack()
T, r, h, k, x, y = 150, 150, 0, 0, 500, 500     #可更改參數 T = 圖形初始角度 r = 圓形路徑中的半徑 x,y = 初始位置
def Diameter(theta):                            #徑度主換
    diameter = theta*np.pi/180
    return diameter

# pincers 1~4 分別對映著螯的前端、中端、左螯、右螯
Lpincers_1 = mycanvas.create_line(x, y, x - 125*np.cos(Diameter(T+40)), y - 125*np.sin(Diameter(T+40)), width=20, fill='red')
Lpincers_2 = mycanvas.create_line(x - 125*np.cos(Diameter(T+40)), y - 125*np.sin(Diameter(T+40)), x - 200*np.cos(Diameter(T+70)), y - 200*np.sin(Diameter(T+70)), width=20, fill='red')
Lpincers_3 = mycanvas.create_polygon(x - 200*np.cos(Diameter(T+70)), y - 200*np.sin(Diameter(T+70)), x - 250*np.cos(Diameter(T+75)), y - 250*np.sin(Diameter(T+75)), x - 275*np.cos(Diameter(T+80)), y - 275*np.sin(Diameter(T+80)), fill='red')
Lpincers_4 = mycanvas.create_polygon(x - 200*np.cos(Diameter(T+70)), y - 200*np.sin(Diameter(T+70)), x - 235*np.cos(Diameter(T+80)), y - 235*np.sin(Diameter(T+80)), x - 275*np.cos(Diameter(T+80)), y - 275*np.sin(Diameter(T+80)), fill='red')
Rpincers_1 = mycanvas.create_line(x, y, x - 125*np.cos(Diameter(T+110)), y - 125*np.sin(Diameter(T+110)), width=20, fill='red')
Rpincers_2 = mycanvas.create_line(x - 125*np.cos(Diameter(T+110)), y - 125*np.sin(Diameter(T+110)), x - 200*np.cos(Diameter(T+90)), y - 200*np.sin(Diameter(T+90)), width=20, fill='red')
Rpincers_3 = mycanvas.create_polygon(x - 200*np.cos(Diameter(T+90)), y - 200*np.sin(Diameter(T+90)), x - 225*np.cos(Diameter(T+85)), y - 225*np.sin(Diameter(T+85)), x - 275*np.cos(Diameter(T+85)), y - 275*np.sin(Diameter(T+85)), fill='red')
Rpincers_4 = mycanvas.create_polygon(x - 200*np.cos(Diameter(T+90)), y - 200*np.sin(Diameter(T+90)), x - 225*np.cos(Diameter(T+93)), y - 225*np.sin(Diameter(T+93)), x - 275*np.cos(Diameter(T+90)), y - 275*np.sin(Diameter(T+90)), fill='red')
leg_1 =  mycanvas.create_line(x - 125*np.cos(Diameter(T+5)), y - 125*np.sin(Diameter(T+5)), x + 125*np.cos(Diameter(T+5)), y + 125*np.sin(Diameter(T+5)), width=10, fill='red')
leg_2 =  mycanvas.create_line(x - 125*np.cos(Diameter(T+35)), y - 125*np.sin(Diameter(T+35)), x + 125*np.cos(Diameter(T+35)), y + 125*np.sin(Diameter(T+35)), width=10, fill='red')
leg_3 =  mycanvas.create_line(x - 125*np.cos(Diameter(T-25)), y - 125*np.sin(Diameter(T-25)), x + 125*np.cos(Diameter(T-25)), y + 125*np.sin(Diameter(T-25)), width=10, fill='red')
leg_11 =  mycanvas.create_line(x - 160*np.cos(Diameter(T-10)), y - 160*np.sin(Diameter(T-10)), x - 125*np.cos(Diameter(T+5)), y - 125*np.sin(Diameter(T+5)), width=10,fill='red')
leg_21 =  mycanvas.create_line(x - 160*np.cos(Diameter(T+20)), y - 160*np.sin(Diameter(T+20)), x - 125*np.cos(Diameter(T+35)), y - 125*np.sin(Diameter(T+35)), width=10, fill='red')
leg_31 =  mycanvas.create_line(x - 160*np.cos(Diameter(T-40)), y - 160*np.sin(Diameter(T-40)), x - 125*np.cos(Diameter(T-25)), y - 125*np.sin(Diameter(T-25)), width=10, fill='red')
leg_12 =  mycanvas.create_line(x + 125*np.cos(Diameter(T+5)), y + 125*np.sin(Diameter(T+5)), x + 160*np.cos(Diameter(T+20)), y + 160*np.sin(Diameter(T+20)), width=10, fill='red')
leg_22 =  mycanvas.create_line(x + 125*np.cos(Diameter(T+35)), y + 125*np.sin(Diameter(T+35)), x + 160*np.cos(Diameter(T+50)), y + 160*np.sin(Diameter(T+50)), width=10, fill='red')
leg_32 =  mycanvas.create_line(x + 125*np.cos(Diameter(T-25)), y + 125*np.sin(Diameter(T-25)), x + 160*np.cos(Diameter(T-10)), y + 160*np.sin(Diameter(T-10)), width=10, fill='red')
main_body = mycanvas.create_oval(x-50, y-50, x+50, y+50, fill='red')

for x in trange(-150,150):          # -150~150為可更改參數，不可大於r (r^2 >= 150^2)
    T = T-180/300                   #隨圓周運動時轉換自身身體角度
    y = (r**2 - (x-h)**2)**0.5 + k  #圓周運動公式，可更換任意曲線公式
    x = x+500
    y = y+500
                    #清除初始化位置
    mycanvas.delete(Lpincers_1), mycanvas.delete(Lpincers_2), mycanvas.delete(Lpincers_3), mycanvas.delete(Lpincers_4)
    mycanvas.delete(Rpincers_1), mycanvas.delete(Rpincers_2), mycanvas.delete(Rpincers_3), mycanvas.delete(Rpincers_4)
    mycanvas.delete(leg_1), mycanvas.delete(leg_2), mycanvas.delete(leg_3)
    mycanvas.delete(leg_11), mycanvas.delete(leg_21), mycanvas.delete(leg_31)
    mycanvas.delete(leg_12), mycanvas.delete(leg_22), mycanvas.delete(leg_32)
    mycanvas.delete(main_body)

    if x % 2 == 0:          #動作狀態一，可視自身需求更改動作
        Lpincers_1 = mycanvas.create_line(x, y, x - 125*np.cos(Diameter(T+50)), y - 125*np.sin(Diameter(T+50)), width=20, fill='red')
        Lpincers_2 = mycanvas.create_line(x - 125*np.cos(Diameter(T+50)), y - 125*np.sin(Diameter(T+50)), x - 200*np.cos(Diameter(T+80)), y - 200*np.sin(Diameter(T+80)), width=20, fill='red')
        Lpincers_3 = mycanvas.create_polygon(x - 200*np.cos(Diameter(T+80)), y - 200*np.sin(Diameter(T+80)), x - 250*np.cos(Diameter(T+80)), y - 250*np.sin(Diameter(T+80)), x - 275*np.cos(Diameter(T+85)), y - 275*np.sin(Diameter(T+85)), fill='red')
        Lpincers_4 = mycanvas.create_polygon(x - 200*np.cos(Diameter(T+80)), y - 200*np.sin(Diameter(T+80)), x - 250*np.cos(Diameter(T+90)), y - 250*np.sin(Diameter(T+90)), x - 275*np.cos(Diameter(T+90)), y - 275*np.sin(Diameter(T+90)), fill='red')
        Rpincers_1 = mycanvas.create_line(x, y, x - 125*np.cos(Diameter(T+120)), y - 125*np.sin(Diameter(T+120)), width=20, fill='red')
        Rpincers_2 = mycanvas.create_line(x - 125*np.cos(Diameter(T+120)), y - 125*np.sin(Diameter(T+120)), x - 200*np.cos(Diameter(T+100)), y - 200*np.sin(Diameter(T+100)), width=20, fill='red')
        Rpincers_3 = mycanvas.create_polygon(x - 200*np.cos(Diameter(T+100)), y - 200*np.sin(Diameter(T+100)), x - 225*np.cos(Diameter(T+95)), y - 225*np.sin(Diameter(T+95)), x - 275*np.cos(Diameter(T+95)), y - 275*np.sin(Diameter(T+95)), fill='red')
        Rpincers_4 = mycanvas.create_polygon(x - 200*np.cos(Diameter(T+100)), y - 200*np.sin(Diameter(T+100)), x - 225*np.cos(Diameter(T+100)), y - 225*np.sin(Diameter(T+100)), x - 275*np.cos(Diameter(T+95)), y - 275*np.sin(Diameter(T+95)), fill='red')
        leg_1 =  mycanvas.create_line(x - 125*np.cos(Diameter(T+5)), y - 125*np.sin(Diameter(T+5)), x + 125*np.cos(Diameter(T+5)), y + 125*np.sin(Diameter(T+5)), width=10, fill='red')
        leg_2 =  mycanvas.create_line(x - 125*np.cos(Diameter(T+35)), y - 125*np.sin(Diameter(T+35)), x + 125*np.cos(Diameter(T+35)), y + 125*np.sin(Diameter(T+35)), width=10, fill='red')
        leg_3 =  mycanvas.create_line(x - 125*np.cos(Diameter(T-25)), y - 125*np.sin(Diameter(T-25)), x + 125*np.cos(Diameter(T-25)), y + 125*np.sin(Diameter(T-25)), width=10, fill='red')
        leg_11 =  mycanvas.create_line(x - 160*np.cos(Diameter(T-10)), y - 160*np.sin(Diameter(T-10)), x - 125*np.cos(Diameter(T+5)), y - 125*np.sin(Diameter(T+5)), width=10,fill='red')
        leg_21 =  mycanvas.create_line(x - 160*np.cos(Diameter(T+20)), y - 160*np.sin(Diameter(T+20)), x - 125*np.cos(Diameter(T+35)), y - 125*np.sin(Diameter(T+35)), width=10, fill='red')
        leg_31 =  mycanvas.create_line(x - 160*np.cos(Diameter(T-40)), y - 160*np.sin(Diameter(T-40)), x - 125*np.cos(Diameter(T-25)), y - 125*np.sin(Diameter(T-25)), width=10, fill='red')
        leg_12 =  mycanvas.create_line(x + 125*np.cos(Diameter(T+5)), y + 125*np.sin(Diameter(T+5)), x + 160*np.cos(Diameter(T+20)), y + 160*np.sin(Diameter(T+20)), width=10, fill='red')
        leg_22 =  mycanvas.create_line(x + 125*np.cos(Diameter(T+35)), y + 125*np.sin(Diameter(T+35)), x + 160*np.cos(Diameter(T+50)), y + 160*np.sin(Diameter(T+50)), width=10, fill='red')
        leg_32 =  mycanvas.create_line(x + 125*np.cos(Diameter(T-25)), y + 125*np.sin(Diameter(T-25)), x + 160*np.cos(Diameter(T-10)), y + 160*np.sin(Diameter(T-10)), width=10, fill='red')
        main_body = mycanvas.create_oval(x-50, y-50, x+50, y+50, fill='red')
    else:                   #動作狀態二，可視自身需求更改動作
        Lpincers_1 = mycanvas.create_line(x, y, x - 125*np.cos(Diameter(T+40)), y - 125*np.sin(Diameter(T+40)), width=20, fill='red')
        Lpincers_2 = mycanvas.create_line(x - 125*np.cos(Diameter(T+40)), y - 125*np.sin(Diameter(T+40)), x - 200*np.cos(Diameter(T+70)), y - 200*np.sin(Diameter(T+70)), width=20, fill='red')
        Lpincers_3 = mycanvas.create_polygon(x - 200*np.cos(Diameter(T+70)), y - 200*np.sin(Diameter(T+70)), x - 250*np.cos(Diameter(T+75)), y - 250*np.sin(Diameter(T+75)), x - 275*np.cos(Diameter(T+80)), y - 275*np.sin(Diameter(T+80)), fill='red')
        Lpincers_4 = mycanvas.create_polygon(x - 200*np.cos(Diameter(T+70)), y - 200*np.sin(Diameter(T+70)), x - 235*np.cos(Diameter(T+80)), y - 235*np.sin(Diameter(T+80)), x - 275*np.cos(Diameter(T+80)), y - 275*np.sin(Diameter(T+80)), fill='red')
        Rpincers_1 = mycanvas.create_line(x, y, x - 125*np.cos(Diameter(T+110)), y - 125*np.sin(Diameter(T+110)), width=20, fill='red')
        Rpincers_2 = mycanvas.create_line(x - 125*np.cos(Diameter(T+110)), y - 125*np.sin(Diameter(T+110)), x - 200*np.cos(Diameter(T+90)), y - 200*np.sin(Diameter(T+90)), width=20, fill='red')
        Rpincers_3 = mycanvas.create_polygon(x - 200*np.cos(Diameter(T+90)), y - 200*np.sin(Diameter(T+90)), x - 225*np.cos(Diameter(T+85)), y - 225*np.sin(Diameter(T+85)), x - 275*np.cos(Diameter(T+85)), y - 275*np.sin(Diameter(T+85)), fill='red')
        Rpincers_4 = mycanvas.create_polygon(x - 200*np.cos(Diameter(T+90)), y - 200*np.sin(Diameter(T+90)), x - 225*np.cos(Diameter(T+93)), y - 225*np.sin(Diameter(T+93)), x - 275*np.cos(Diameter(T+90)), y - 275*np.sin(Diameter(T+90)), fill='red')
        leg_1 =  mycanvas.create_line(x - 125*np.cos(Diameter(T+5)), y - 125*np.sin(Diameter(T+5)), x + 125*np.cos(Diameter(T+5)), y + 125*np.sin(Diameter(T+5)), width=10, fill='red')
        leg_2 =  mycanvas.create_line(x - 125*np.cos(Diameter(T+35)), y - 125*np.sin(Diameter(T+35)), x + 125*np.cos(Diameter(T+35)), y + 125*np.sin(Diameter(T+35)), width=10, fill='red')
        leg_3 =  mycanvas.create_line(x - 125*np.cos(Diameter(T-25)), y - 125*np.sin(Diameter(T-25)), x + 125*np.cos(Diameter(T-25)), y + 125*np.sin(Diameter(T-25)), width=10, fill='red')
        leg_11 =  mycanvas.create_line(x - 160*np.cos(Diameter(T-10)), y - 160*np.sin(Diameter(T-10)), x - 125*np.cos(Diameter(T+5)), y - 125*np.sin(Diameter(T+5)), width=10,fill='red')
        leg_21 =  mycanvas.create_line(x - 160*np.cos(Diameter(T+20)), y - 160*np.sin(Diameter(T+20)), x - 125*np.cos(Diameter(T+35)), y - 125*np.sin(Diameter(T+35)), width=10, fill='red')
        leg_31 =  mycanvas.create_line(x - 160*np.cos(Diameter(T-40)), y - 160*np.sin(Diameter(T-40)), x - 125*np.cos(Diameter(T-25)), y - 125*np.sin(Diameter(T-25)), width=10, fill='red')
        leg_12 =  mycanvas.create_line(x + 125*np.cos(Diameter(T+5)), y + 125*np.sin(Diameter(T+5)), x + 160*np.cos(Diameter(T+20)), y + 160*np.sin(Diameter(T+20)), width=10, fill='red')
        leg_22 =  mycanvas.create_line(x + 125*np.cos(Diameter(T+35)), y + 125*np.sin(Diameter(T+35)), x + 160*np.cos(Diameter(T+50)), y + 160*np.sin(Diameter(T+50)), width=10, fill='red')
        leg_32 =  mycanvas.create_line(x + 125*np.cos(Diameter(T-25)), y + 125*np.sin(Diameter(T-25)), x + 160*np.cos(Diameter(T-10)), y + 160*np.sin(Diameter(T-10)), width=10, fill='red')
        main_body = mycanvas.create_oval(x-50, y-50, x+50, y+50, fill='red')

    mycanvas.update()
    mycanvas.after(500) #delay 500毫秒