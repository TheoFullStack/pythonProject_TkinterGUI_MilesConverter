import tkinter
"""def button_clicked():
    my_label.config(text=input.get())"""

window = tkinter.Tk()

window.title("My first GUI program")

window.minsize(width=300,height=100)


"""#label (WHEN YOU ARE USIGN GRID ALWAYS START WITH WAHT YOU WANT ON TOP LEFT)
my_label = tkinter.Label(text="I am a label", font=("Arial",25,"bold"))
my_label.grid(column=0,row=0)
my_label.config(padx=20,pady=20)

#Button
button = tkinter.Button(text="Click me",command=button_clicked)
button.grid(column=1,row=1)

button2 = tkinter.Button(text="New Button")
button2.grid(column=2,row=0)

#Entry
input = tkinter.Entry(width=10)
input.get()
input.grid(column=3,row=2)
"""
def converter():
    miles = int(input.get())
    km = round(miles*1.60934)
    label4.config(text=km)
#label1
label1 = tkinter.Label(text="Miles",font=("Arial",14,"bold"))
label1.grid(column=4,row=0)
label1.config(padx=10)
#label2
label2 =tkinter.Label(text="is equal to",font=("Arial",10))
label2.grid(column=2,row=3)

#label3
label3 = tkinter.Label(text="KM",font=("Arial",14,"bold"))
label3.grid(column=4,row=3)

#label4

label4= tkinter.Label(text=" ",font=("Arial",10))
label4.grid(column=3,row=3)



#Entry

input = tkinter.Entry(width=10)
input.grid(column=3,row=0)

#button

button = tkinter.Button(text="Calculate",command=converter)
button.grid(column=3,row=5)



window.mainloop()