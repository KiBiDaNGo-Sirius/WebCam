import tkinter as Tk

root = Tk() 
canvas = Canvas(root, width=200, height=200) 
canvas.create_rectangle(10, 10, 60, 60) 
canvas.create_rectangle(70, 70, 120, 120) 
canvas.pack() 
canvas.move(ALL, 50, 50) 
root.mainloop() 