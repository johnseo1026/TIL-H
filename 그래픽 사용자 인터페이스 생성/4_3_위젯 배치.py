import tkinter

window = tkinter.Tk()
frame = tkinter.Frame(window)
frame.pack()
label = tkinter.Label(frame, text='Name')
label.pack(side='left')
entry = tkinter.Entry(frame)
entry.pack(side='left')

window.mainloop()


# import tkinter

# window = tkinter.Tk()
# frame = tkinter.Frame(window)
# frame.pack()
# label = tkinter.Label(frame, text='Name:')
# label.grid(row=0, column=0)
# entry = tkinter.Entry(frame)
# entry.grid(row=1, column=1)

# window.mainloop()