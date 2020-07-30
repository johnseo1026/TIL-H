import tkinter

window = tkinter.Tk()
frame = tkinter.Frame(window)
frame.pack()
first = tkinter.Label(frame, text='First label')
first.pack()
second = tkinter.Label(frame, text='Second label')
second.pack()
third = tkinter.Label(frame, text='Third label')
third.pack()

window.mainloop()


# import tkinter

# window = tkinter.Tk()
# frame = tkinter.Frame(window)
# frame.pack()
# frame2 = tkinter.Frame(window, borderwidth=4, relief=tkinter.GROOVE)
# frame2.pack()
# first = tkinter.Label(frame, text='First label')
# first.pack()
# second = tkinter.Label(frame, text='Second label')
# second.pack()
# third = tkinter.Label(frame, text='Third label')
# third.pack()

# window.mainloop()
