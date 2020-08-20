import cv2
import tkinter
from PIL import Image, ImageTk
import threading

# VideoCapture オブジェクトを取得します
capture = cv2.VideoCapture(int(int(input())))
# windowを描画
window = tkinter.Tk()
# windowサイズを変更
window.geometry("800x600")
# windowタイトルを設定
window.title("Welcome to the Tkinter")

def getPicture():
   # while(True):
        ret, frame = capture.read()
        # resize the window1

        windowsize = (800, 600)
        frame = cv2.resize(frame, windowsize)
        cv2.imwrite('test.png',frame)

        # 画像を表示するための準備
        img = Image.open('test.png')
        img = ImageTk.PhotoImage(img)
        # 画像を表示するためのキャンバスの作成（黒で表示）
        canvas = tkinter.Canvas(bg = "black", width=800, height=600)
        canvas.place(x=0, y=0) # 左上の座標を指定
        # キャンバスに画像を表示する。第一引数と第二引数は、x, yの座標
        canvas.create_image(0, 0, image=img, anchor=tkinter.NW)
        
        #if cv2.waitKey(1) & 0xFF == ord('q'):
           # break
getPicture()
window.mainloop()

print("fin")