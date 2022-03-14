import tkinter 

top = tkinter.Tk()
C = tkinter.Canvas(top, height=500, width=500)


C.create_line(250,500, 250,400)
C.create_line(4, 5, 55, 22)


C.pack()
top.mainloop()