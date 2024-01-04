# import tkinter
#
#
# def button_clicked():
#     my_label.config(text=f"{input.get()}")
#
#
# # Window
# window = tkinter.Tk()
# window.title("My First GUI Program")
# window.minsize(width=500, height=300)
# window.config(padx=100, pady=200)
#
# # Label
# my_label = tkinter.Label(text="I Am a Label", font=("Arial", 24, "bold"))
# my_label.grid(column=0, row=0)
# my_label["text"] = "New Text"
# my_label.config(text="New Text")
# my_label.config(padx=20, pady=50)
#
# # Button
# button = tkinter.Button(text="Click", command=button_clicked)
# button.grid(column=1, row=1)
#
# # Entry
# input = tkinter.Entry(width=10)
# input.grid(column=3, row=3)
#
# # Button2
# button2 = tkinter.Button(text="new button", command=button_clicked)
# button2.grid(column=2, row=0)
#
# window.mainloop()

from tkinter import *


def calculate():
    miles = int(miles_to_convert.get())
    kilometer = round(miles * 1.609344, 2)
    converted_kilometer.config(text=kilometer)


# Create Window
window = Tk()
window.title("Miles to KM Converter")
window.minsize(width=200, height=100)
window.config(padx=20, pady=20)

# Create Miles to convert
miles_to_convert = Entry(width=10)
miles_to_convert.grid(column=1, row=0)

# Create Miles text
miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

# Create Equal to text
equal_label = Label(text="is equal to")
equal_label.grid(column=0, row=1)

# Create Kilometer text
converted_kilometer = Label(text=0)
converted_kilometer.grid(column=1, row=1)

# Create KM text
km_label = Label(text="KM")
km_label.grid(column=2, row=1)

# Create Button
button = Button(text="Calculate", command=calculate)
button.grid(column=1, row=2)


window.mainloop()
