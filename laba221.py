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
