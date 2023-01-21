# Importing modules to get the job done
from tkinter import *
from translate import Translator
import googletrans

# Building a frame for the interface of transaltor
dev=Tk()
dev.title('Translator(Experimental)')
dev.geometry("800x400")

# Extracting languages
language = googletrans.LANGUAGES
lang= list(language.values())

choice1= StringVar(dev)
choice2= StringVar(dev)

def translate():
    
    # Converting languages as per user want
    translator = Translator(from_choiceg = choice1.get(), to_lang = choice2.get())
    trans= translator.translate(var.get())

    var1.set(trans)

choices = {"English","Hindi",'Gujarati','Spanish','German',"Chinese",'Korean','Japanese'}

choice1.set('English')
choice2.set('Hindi')

# Choice menu and text area 
choice1menu = OptionMenu(dev, choice1, *choices)
Label(dev, text="Choose a language ").grid(row=0,column=1)
choice1menu.grid(row=1,column=1)

choice2menu = OptionMenu(dev, choice2, *lang)
Label(dev, text="Converted  ").grid(row=0,column=3)
choice2menu.grid(row=1,column=3)

Label(dev, text="Enter Text = ").grid(row=2,column=0)
var=StringVar()
textbox = Entry(dev,textvariable=var,width=20).grid(row=2,ipadx= 10, ipady=10 , column=1)

Label(dev, text="Translated= ").grid(row=2,column=2)
var1=StringVar()
textbox = Entry(dev,textvariable=var1,width=20,font= 'Helvetica 16 ').grid(row=2, column=3,ipadx= 10, ipady=10)

b=butt= Button(dev, text="Translate",font=("helvetica 12 bold"),relief= RAISED,cursor="hand2",activebackground= "lime green",command=translate,fg="blue").grid(row=3,column=2)


# End of the code 
dev.mainloop()
