import tkinter as tkk
from tkinter import Tk
from tkinter.messagebox import showerror

window=Tk()
window.title("Сложение двух чисел") 
window.geometry("700x100") 

def calc(): 

    float1=float(entry.get()) 
    float2=float(entry2.get()) 

    
    sum=float1+float2

    outlabel=tkk.Label(window, text=sum)
    outlabel.grid(column=4, row=0)
    
    
out=tkk.Label(window, text=" + ") 
out.grid(column=1, row=0)

out2=tkk.Label(window, text=" = ")
out2.grid(column=3, row=0)

entry=tkk.Entry(window) 
entry.grid(column=0, row=0)

entry2=tkk.Entry(window)
entry2.grid(column=2, row=0)

butnn=tkk.Button(window, text="Расчитать сумму чисел", command=calc)
butnn.grid(column=1, row=2)

window.mainloop()
