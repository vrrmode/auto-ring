from tkinter import *

from tkinter import messagebox

import about

root = Tk()
root.title('AutoRing')
root.minsize(0,10)
root.resizable(width=False, height=False)


# Widgets
button_table = Button(text = 'Составить расписание звонков')
button_callTuning = Button(text = 'Настройка звонка')

onOff = IntVar()
onRbttn1 = Radiobutton(text = 'Ring On', variable = onOff, value = 1)
onRbttn2 = Radiobutton(text = 'Ring Off', variable = onOff, value = 2)

button_extraCall = Button(text = 'Подать экстренный звонок')
button_extraCallTuning = Button(text = 'Настройка экстренного звонка')

button_about = Button(text = 'О программе', command = set)


# Widgets pack
button_table.grid(row = 0, column = 0, padx = 60, pady = 4)
button_callTuning.grid(row = 1, column = 0, padx = 60, pady = 4)

onRbttn1.grid(row = 2, column = 0)
onRbttn2.grid(row = 3, column = 0)

button_extraCall.grid(row = 4, column = 0, padx = 60, pady = 4)
button_extraCallTuning.grid(row = 5, column = 0, padx = 60, pady = 4)

button_about.grid(row = 8, column = 0, padx = 60, pady = 10)


root.mainloop()	