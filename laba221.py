import tkinter as tkk
from tkinter import Tk
from tkinter.messagebox import showerror
# Create the window with Tk library
window=Tk()
window.title("Сложение двух чисел") # set window title
window.geometry("700x100") #set size

def calc(): 

    float1=float(entry.get()) #get float value of first number
    float2=float(entry2.get()) #get float value of second number

    #Addition operation
    sum=float1+float2

    outlabel=tkk.Label(window, text=sum)
    outlabel.grid(column=4, row=0)

#Create the "+" Label
out=tkk.Label(window, text=" + ") 
out.grid(column=1, row=0)
#Create the "=" Label
out2=tkk.Label(window, text=" = ")
out2.grid(column=3, row=0)

#Create Entry for first number
entry=tkk.Entry(window) 
entry.grid(column=0, row=0)

#Create Entry for second number
entry2=tkk.Entry(window)
entry2.grid(column=2, row=0)

#Create the Button for calculation
butnn=tkk.Button(window, text="Расчитать сумму чисел", command=calc)
butnn.grid(column=1, row=2)

window.mainloop()
