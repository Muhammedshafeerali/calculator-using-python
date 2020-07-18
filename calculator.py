from tkinter import *

labell = ''
def press(num):
    global labell
    labell = labell + str(num)
    equation.set(labell)
    print('haii')

def equal():
    global labell
    newnum=str(eval(labell))
    equation.set(newnum)
    labell =newnum

def clear():
    global  labell
    labell=" "
    equation.set(labell)


if __name__ == '__main__':

    window = Tk()
    window.geometry('330x400')
    window.config(bg='powderblue')
    window.title('calculator')
    equation = StringVar()
    label = Label(window, bg='white', width='50', height='3', textvariable=equation)
    label.grid(row=0, column=0, columnspan=30)

    button7 = Button(window, text='7', width='4', height='2', command=lambda : press(7))
    button7.grid(row=1, column=0, pady=10)
    button8 = Button(window, text='8', width='4', height='2', command=lambda : press(8))
    button8.grid(row=1, column=1)
    button9 = Button(window, text='9', width='4', height='2')
    button9.grid(row=1, column=2)

    button4 = Button(window, text='4', width='4', height='2')
    button4.grid(row=2, column=0, pady=5)
    button5 = Button(window, text='5', width='4', height='2')
    button5.grid(row=2, column=1)
    button6 = Button(window, text='6', width='4', height='2')
    button6.grid(row=2, column=2)

    button1 = Button(window, text='1', width='4', height='2')
    button1.grid(row=3, column=0, pady=5)
    button2 = Button(window, text='2', width='4', height='2')
    button2.grid(row=3, column=1)
    button3 = Button(window, text='3', width='4', height='2')
    button3.grid(row=3, column=2)

    buttonzero = Button(window, text='0', width='4', height='2')
    buttonzero.grid(row=4, column=0, pady=5)
    buttonpoint = Button(window, text='.', width='4', height='2')
    buttonpoint.grid(row=4, column=1)
    buttonplus = Button(window, text='+', width='4', height='2',command=lambda : press('+'))
    buttonplus.grid(row=4, column=2)

    buttonback = Button(window, text='back', width='4', height='2')
    buttonback.grid(row=1, column=3)
    buttondiv = Button(window, text='/', width='4', height='2')
    buttondiv.grid(row=2, column=3)
    buttonmulti = Button(window, text='*', width='4', height='2')
    buttonmulti.grid(row=3, column=3)
    buttonminus = Button(window, text='-', width='4', height='2')
    buttonminus.grid(row=4, column=3)

    buttonequal = Button(window, text='=', width='28', height='2',command=lambda:equal())
    buttonequal.grid(row=5, columnspan=8, sticky=W, pady=5)

    buttonclear=Button(window,text='C', width='4', height='15', command=lambda:clear())
    buttonclear.grid(row=1, column=4, rowspan=8, padx=4)

    window.mainloop()


