import tkinter as tk
import cv2
from PIL import Image,ImageTk
import numpy as np

#Main window
window=tk.Tk()
window.title("OMCHS") #online meeting chat helping system
window.geometry("800x450") #same as zoom window
window.resizable(width=True, height=True)
#video canvas
Vcanvas=tk.Canvas(window, width=600, height=450, bg="green")
Vcanvas.place(x=0, y=0)
#text canvas
Tcanvas = tk.Canvas(window, width=200, height=450, bg="blue")
Tcanvas.place(x=600, y=0)


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
        '''終了時の処理はここでは省略します。
        c.release()
        cv2.destroyAllWindows()'''

def update():#update
    global img
    ret, frame =Capture.read()
    windowsize = (1200, 900)
    frame = cv2.resize(frame, windowsize)
    if ret:
        img=ImageTk.PhotoImage(Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)))
        Vcanvas.create_image(0,0,image=img)
    else:
        print("u-Fail")
    window.after(1,update)

capStart()
update()
window.mainloop()

#参考にさせていただいたページ　https://shizenkarasuzon.hatenablog.com/entry/2018/12/31/064646　https://teratail.com/questions/187773
#今後、許可をとる予定です