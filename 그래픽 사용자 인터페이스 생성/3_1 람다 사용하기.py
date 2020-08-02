# import tkinter

# window = tkinter.Tk()

# # 모델
# counter = tkinter.IntVar()
# counter.set(0)

# # 컨트롤러 두개
# def click_up():
#     counter.set(counter.get() + 1)

# def click_down():
#     counter.set(counter.get() - 1)

# # 뷰
# frame = tkinter.Frame(window)
# frame.pack()
# button = tkinter.Button(frame, text='Up', command=click_up)
# button.pack()
# button = tkinter.Button(frame, text='Down', command=click_down)
# button.pack()
# label = tkinter.Label(frame, textvariable=counter)
# label.pack()

# # 기계를 시작시킨다!
# window.mainloop()



import tkinter

window = tkinter.Tk()

# 모델
counter = tkinter.IntVar()
counter.set(0)

# 보편적인 컨트롤러
def click(var, value):
    var.set(var.get() + value)

# 뷰
frame = tkinter.Frame(window)
frame.pack()
button = tkinter.Button(frame, text='Up', command=lambda: click(counter, 1))
button.pack()

button = tkinter.Button(frame, text='Down', command=lambda: click(counter, -1))
button.pack()

label = tkinter.Label(frame, textvariable=counter)
label.pack()

# 기계를 시작시킨다!
window.mainloop()
