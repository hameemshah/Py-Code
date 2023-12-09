import tkinter

def button_clicked():
    value = float(input.get()) * 1.6
    output['text'] = str(value) + " Kilometers."


window = tkinter.Tk()
window.title("My GUI Programme")
window.minsize(width=300, height=150)

# Input
input = tkinter.Entry(width=10)
input.grid(column=3, row=0)

# Label
my_label = tkinter.Label(text=" miles are ", font=("Arial", 12, "italic"))
my_label.grid(column=4, row=0)

# Label for output
output = tkinter.Label(text=" ")
output.grid(column=2, row=1)

# Button
button = tkinter.Button(text="Calculate", command=button_clicked)
button.grid(column=2, row=2)

window.mainloop()
