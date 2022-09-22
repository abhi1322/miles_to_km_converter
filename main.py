from tkinter import *

km_value = 0


def get_miles():
    value = int(miles_input.get())
    global km_value
    km_value = round(value * 1.60934, 2)
    output_lable.config(text=f"is equal to {km_value} Km")


window = Tk()
window.minsize(width=200, height=120)
window.title(string="Miles to km converter")

miles_input = Entry(width=10)
miles_input.place(x=50, y=30)

miles_text = Label(text="Miles")
miles_text.place(x=120, y=30)

output_lable = Label(text=f"is equal to {km_value} Km")
output_lable.place(x=45, y=50)

button = Button(text="Convert", command=get_miles)
button.pack(side="bottom", pady=20)


window.mainloop()
