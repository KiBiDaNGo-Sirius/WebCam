import tkinter as tk

frame1 = tk.Tk()
frame1.title("1")
frame1.geometry('300x400')
frame1.grid()

frame2 = tk.Toplevel()
frame2.title("2")
frame2.geometry('500x800')
frame2.grid()

frame1.mainloop()

#https://teratail.com/questions/181202