import tkinter
from tkinter import ttk, END

# define window
root = tkinter.Tk()
root.title('Converter')
root.resizable(0,0)
root.geometry('320x145')

# functions
def convert():
    convertvalues = {
        'centimeters': 10**-2,
        'inches': 10**-2*0.9144,
        'meters': 10**0,
        'feet': 10**0*0.3048,
        'kilometers': 10**3,
        'miles': 10**3*1.60934
    }
    right_text_entry.delete(0, END)
    startvalue = float(left_text.get())
    startprefix = input_combobox.get()
    endprefix = output_combobox.get()
    base_value = startvalue*convertvalues[startprefix]
    end_value = base_value/convertvalues[endprefix]
    right_text_entry.insert(0, str("{:.2f}".format(end_value)))

# define fonts and colors
field_font = ('monospace', 8)
bg_color = 'white'
button_color = 'black'
root.config(bg=bg_color)

# frames
frame = tkinter.LabelFrame(root, text="Metric to Imperial Converter", bg=bg_color, width=300, height=120)
frame.pack(padx=10, pady=10)

# inputs n stuff
left_text = tkinter.IntVar()
left_text_entry = tkinter.Entry(frame,textvariable=left_text, width=16)
left_text_entry.grid(row=0, column=0, padx=5, pady=5)
left_text_entry.insert(0, "")
right_text_entry = tkinter.IntVar()
right_text_entry = tkinter.Entry(frame, width=16, bg='white')
right_text_entry.grid(row=0, column=2, padx=5, pady=5)
right_text_entry.insert(0, "")
equal = tkinter.Label(frame, text="=", bg=bg_color)
equal.grid(row=0, column=1, padx=5, pady=5)

# combobox
metricconversion_list = ['centimeters', 'meters', 'kilometers']
imperialconversion_list = ['inches', 'feet', 'miles']
input_combobox = ttk.Combobox(frame, width=14, value=metricconversion_list, justify='center')
output_combobox = ttk.Combobox(frame, width=14, value=imperialconversion_list, justify='center')
to = tkinter.Label(frame, text="to", bg=bg_color)

input_combobox.grid(row=1, column=0, padx=10, pady=10)
output_combobox.grid(row=1, column=2, padx=10, pady=10)
to.grid(row=1, column=1, padx=5, pady=5)

button = tkinter.Button(frame, text='Convert', bg=bg_color, command=convert)
button.grid(row=2, column=0, columnspan=3, padx=5, pady=(0,10))
root.mainloop()
