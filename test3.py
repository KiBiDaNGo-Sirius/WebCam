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
        if s == "toumei":
            Vcanvas.create_image(0, 0, image=toumei, anchor=tk.NW)
        elif s == "maru":
            Vcanvas.create_image(0, 0, image=maru, anchor=tk.NW)
        elif s == "batu":
            Vcanvas.create_image(0, 0, image=batu, anchor=tk.NW)

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
    messagebox.showinfo("メッセージ", "ボタンがクリックされました")

MaruB = tk.Button(control, text='O', command = MaruB_click)

btn.place(x=130, y=80) #ボタンを配置する位置の設定


capStart()
update()

# 画像を表示するためのキャンバスの作成（黒で表示）
# キャンバスに画像を表示する。第一引数と第二引数は、x, yの座標
#Vcanvas.create_image(0, 0, image=actionImg, anchor=tk.NW)
window.mainloop()

#参考にさせていただいたページ　https://shizenkarasuzon.hatenablog.com/entry/2018/12/31/064646　https://teratail.com/questions/187773
#今後、許可をとる予定ですk