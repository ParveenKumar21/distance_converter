from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
# window.minsize(width=350,height=200)
window.config(padx=40,pady=30, bg="#d7f9f8")

def converter():
    num = input.get()
    kms = float(num) * 1.609
    result.config(text=round(kms,2))

heading = Label(text="Convert", font=("Arial",25,"normal"), bg="#d7f9f8")
heading.grid(column=0, row=0, columnspan=3)

is_equal_to = Label(text="is equal to -",font=("Arial",13,"normal"), bg="#d7f9f8")
is_equal_to.grid(column=0,row=2)
# is_equal_to.config(padx=10,pady=10)

miles = Label(text="Miles -",font=("Arial",13,"normal"), bg="#d7f9f8")
miles.grid(column=0,row=1)
# miles.config(padx=10,pady=10)

km = Label(text="Km",font=("Arial",10,"normal"), bg="#d7f9f8")
km.grid(column=2,row=2)

result =Label(text=0, bg="#d7f9f8")
result.grid(column=1,row=2)

input = Entry(text=0, width=10)
input.grid(column=1,row=1)


calculate = Button(text="Calculate",command=converter)
calculate.grid(column=1,row=3)








window.mainloop()