from tkinter import *

def convert():
    miles = float(entry.get())
    km = int(miles * 1.609)
    km_result.config(text=km)

window = Tk()
window.title("Mile to KM Converter")
window.config(padx=20, pady=20)

is_equal = Label()
is_equal.config(text="is equal to")
is_equal.grid(row=1, column=0)
is_equal.config(padx=10, pady=5)

miles_input = Label()
miles_input.config(text="Miles")
miles_input.grid(row=0, column=2)
miles_input.config(padx=10, pady=5)

km_result = Label()
km_result.config(text="0")
km_result.grid(row=1, column=1)
km_result.config(padx=10, pady=5)

km_label = Label()
km_label.config(text="Km")
km_label.grid(row=1, column=2)
km_label.config(padx=10, pady=5)

entry = Entry(width=12)
entry.insert(END, string="0")
entry.grid(row=0, column=1)

button = Button(width=10, text="Calculate", command=convert)
button.grid(row=2, column=1)

window.mainloop()