from tkinter import *


class MenuDemo:
    def __init__(self):
        window = Tk()
        window.title("Menu Demo")

        # Create a menu bar
        menubar = Menu(window)
        # create a pulldown menu, and add it to the menu bar
        operationMenu = Menu(menubar, tearoff=0)
        exitmenu = Menu(menubar, tearoff=0)

        menubar.add_cascade(label="Operation", menu=operationMenu)
        menubar.add_cascade(label="Exit", menu=exitmenu)
        window.config(menu=menubar)  # Display the menu bar

        operationMenu.add_command(label="Add",command=self.add)
        operationMenu.add_command(label="Subtract",command=self.subtract)
        operationMenu.add_separator()
        operationMenu.add_command(label="Multiply",command=self.multiply)
        operationMenu.add_command(label="Divide",command=self.divide)
        # create more pulldown menus
        exitmenu.add_command(label="Quit", command=window.quit)

        # Add a tool bar frame 
        frame0 = Frame(window)  # Create and add a frame to window
        frame0.grid(row=1, column=1, sticky=W)

        # Create images
        plusImage = PhotoImage(file="../img/plus.gif")
        minusImage = PhotoImage(file="../img/minus.gif")
        timesImage = PhotoImage(file="../img/times.gif")
        divideImage = PhotoImage(file="../img/divide.gif")

        Button(frame0, image=plusImage, command=self.add).grid(row=1, column=1, sticky=W)
        Button(frame0, image=minusImage,command=self.subtract).grid(row=1, column=2)
        Button(frame0, image=timesImage,command=self.multiply).grid(row=1, column=3)
        Button(frame0, image=divideImage,command=self.divide).grid(row=1, column=4)

        # Add labels and entries to frame1
        frame1 = Frame(window)
        frame1.grid(row=2, column=1, pady=10)

        Label(frame1, text="Number 1:").pack(side=LEFT)

        self.v1 = StringVar()
        self.v2 = StringVar()
        self.v3 = StringVar()

        Entry(frame1, width=5, textvariable=self.v1,justify=RIGHT).pack(side=LEFT)
        Label(frame1, text="Number 2:").pack(side=LEFT)
        Entry(frame1, width=5, textvariable=self.v2,justify=RIGHT).pack(side=LEFT)
        Label(frame1, text="Result:").pack(side=LEFT)
        Entry(frame1, width=5, textvariable=self.v3,justify=RIGHT).pack(side=LEFT)

        # Add buttons to frame2
        frame2 = Frame(window)  # Create and add a frame to window
        frame2.grid(row=3, column=1, pady=10, sticky=E)

        Button(frame2, text="Add", command=self.add).pack(side=LEFT)
        Button(frame2, text="Subtract",command=self.subtract).pack(side=LEFT)
        Button(frame2, text="Multiply",command=self.multiply).pack(side=LEFT)
        Button(frame2, text="Divide",command=self.divide).pack(side=LEFT)

        mainloop()

    def add(self):
        self.v3.set(eval(self.v1.get()) + eval(self.v2.get()))

    def subtract(self):
        self.v3.set(eval(self.v1.get()) - eval(self.v2.get()))

    def multiply(self):
        self.v3.set(eval(self.v1.get()) * eval(self.v2.get()))

    def divide(self):
        self.v3.set(eval(self.v1.get()) / eval(self.v2.get()))


MenuDemo()  # Create GUI
