import tkinter as tk
from tkinter import messagebox
import cv2
from PIL import Image,ImageTk
import numpy as np
import threading

#Main window
window=tk.Tk()
window.title("OMCHS") #online meeting chat helping system
window.geometry("800x450") #same as zoom window
window.resizable(width=True, height=True)
#control window
control = tk.Toplevel()
control.title("control")
control.geometry('400x400')
control.grid()

#Picture setting
maru = Image.open('maru.png')
maru = ImageTk.PhotoImage(maru)
batu = Image.open('batu.png')
batu = ImageTk.PhotoImage(batu)
toumei = Image.open('toumei.png')
toumei = ImageTk.PhotoImage(toumei)

#path setting
path = 'text.txt'

#Main window set up and function --------------------------------------------

#video canvas
Vcanvas=tk.Canvas(window, width=600, height=450, bg="green")
Vcanvas.place(x=0, y=0)


def getAction():
    with open(path) as f:
        s = f.read()
        print(s)
        if s == "toumei":
            Vcanvas.create_image(0, 0, image=toumei, anchor=tk.NW)
        elif s == "maru":
            Vcanvas.create_image(0, 0, image=maru, anchor=tk.NW)
        elif s == "batu":
            Vcanvas.create_image(0, 0, image=batu, anchor=tk.NW)
        else:
            Vcanvas.create_text(100, 100, text=s, font=("Meiryo", 18, "bold"))
        

#get webCam capture
def capStart():
    print('camera-ON')
    try:
        global Capture, w, h
        Capture=cv2.VideoCapture(0)
        w, h= Capture.get(cv2.CAP_PROP_FRAME_WIDTH), Capture.get(cv2.CAP_PROP_FRAME_HEIGHT)
        
    except:
        import sys
        print("error-----")
        print(sys.exec_info()[0])
        print(sys.exec_info()[1])

#updata
def update():
    global img
    ret, frame =Capture.read()
    windowsize = (1200, 900)
    frame = cv2.resize(frame, windowsize)
    if ret:
        img=ImageTk.PhotoImage(Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)))
        Vcanvas.create_image(0,0,image=img)
        getAction()
    else:
        print("u-Fail")
    window.after(1,update)

#control window set up and function--------------------------------------------



def MaruB_click():
    with open(path, mode='w') as f:
        f.write("maru")

def BatuB_click():
    with open(path, mode='w') as f:
        f.write("batu")

def ToumeiB_click():
    with open(path, mode='w') as f:
        f.write("toumei")

def Textfun():
    s = text.get()
    with open(path, mode='w') as f:
        f.write(s)
    

MaruL = tk.Label(text="O")
MaruL.place(x=100, y=50)
MaruB = tk.Button(control, text='O', command = MaruB_click)
MaruB.place(x=130, y=50) #ボタンを配置する位置の設定

BatuL = tk.Label(text="X")
BatuL.place(x=100, y=80)
BatuB = tk.Button(control, text='X', command = BatuB_click)
BatuB.place(x=130, y=80) #ボタンを配置する位置の設定

ToumeiL = tk.Label(text="Clear")
ToumeiL.place(x=100, y=110)
ToumeiB = tk.Button(control, text='clear', command = ToumeiB_click)
ToumeiB.place(x=130, y=110) #ボタンを配置する位置の設定

textL = tk.Label(text="TEXT")
textL.place(x=100, y=140)
textB = tk.Button(control, text='text', command = Textfun)
textB.place(x=130, y=140) #ボタンを配置する位置の設定
text = tk.Entry(width=20)
text.place(x=130, y=170)

capStart()
update()
window.mainloop()

#参考にさせていただいたページ　https://shizenkarasuzon.hatenablog.com/entry/2018/12/31/064646　https://teratail.com/questions/187773
#今後、許可をとる予定ですk