import tkinter, ast
from tkinter import ttk, END, ANCHOR
import string

def print_todo():
    todolist.insert(END, (' [ ] ' + input_text.get()))
    input_text.delete(0, END)
    #text = tkinter.Label(todolist, text=('[ ] ' + input_text.get()), bg=bg_color, font=field_font)
    #text.pack()

def remove():
    todolist.delete(ANCHOR)

def clear():
    todolist.delete(0, END)

def save():
    save_file = 'checklistsave.txt'
    with open(save_file, "w") as file:
        for i, j in enumerate(todolist.get(0, END)):
            file.write(j+"\n")
    #except FileNotFoundError:
        #todolist.insert(0, "no file found")

def open_list():
    try:
        with open("checklistsave.txt", "r") as f:
            for line in f:
                todolist.insert(END, (" " + line.strip()))
    except:
        return

def mark_as_done():
    if ' [x] ' in todolist.get(ANCHOR):
        todolist.insert(ANCHOR, (' [ ] ' + todolist.get(ANCHOR)[5:]))
        todolist.delete((ANCHOR))
    else:
        todolist.insert(ANCHOR, (' [x] ' + todolist.get(ANCHOR)[5:]))
        todolist.delete(ANCHOR)

# define window
root = tkinter.Tk()
root.title("to-do List")
root.geometry("350x484")
root.resizable(0,0)

# customize stuff
bg_color = 'white'
root.config(bg=bg_color)
field_font = ('monospace', 8)

# top frame, text box and "add" button
input_frame = tkinter.LabelFrame(root, text='input', bg=bg_color, width=350, height=50, font=field_font)
input_frame.pack(padx=10, pady=10)

add_button = tkinter.Button(input_frame, text='add', font=field_font, bg=bg_color, command=print_todo)
add_button.grid(row = 0, column=1, padx=10, pady=10)

input_text = tkinter.StringVar
input_text = tkinter.Entry(input_frame, bg=bg_color, width=41, font=field_font)
input_text.grid(row=0, column=0, padx=(10,0))

# frame where the list is
todo_frame = tkinter.LabelFrame(root, text='to-do list', bg=bg_color, width=350, height=335, font=field_font)
todo_frame.pack(padx=10)
todo_frame.propagate(0)

todolist = tkinter.Listbox(todo_frame, borderwidth=0, height=24, width=54, highlightthickness=0, font=field_font, bg=bg_color)
scrollbar = tkinter.Scrollbar(todolist, orient='vertical')
todolist.config(yscrollcommand=scrollbar.get)

todolist.grid(row=0, column=1)
todolist.propagate(0)
scrollbar.pack(side='right', fill='y', padx=5, pady=(0,5))
scrollbar.config(command=todolist.yview())

# buttons "remove item", "clear list", "save list", and "quit"
button_frame = tkinter.LabelFrame(root, text='cmd', bg=bg_color, width=350, height=50, font=field_font)
button_frame.pack(padx=10, pady=10)

remove_button = tkinter.Button(button_frame, text='remove', font=field_font, bg=bg_color, command=remove)
clear_button = tkinter.Button(button_frame, text='clear', font=field_font, bg=bg_color, command=clear)
save_button = tkinter.Button(button_frame, text='save', font=field_font, bg=bg_color, command=save)
quit_button = tkinter.Button(button_frame, text='quit', font=field_font, bg=bg_color, command=root.destroy)
mark_as_done = tkinter.Button(button_frame, text='done', font=field_font, bg=bg_color, command=mark_as_done)

remove_button.grid(row=0, column=1, padx=5, pady=5)
clear_button.grid(row=0, column=2, pady=5)
save_button.grid(row=0, column=3, padx=5, pady=5)
quit_button.grid(row=0, column=4, padx=(15,5), pady=5)
mark_as_done.grid(row=0, column=0, padx=(5,0), pady=5)

"""with open("checklistsave.txt", "r") as save_content:
    save_list = save_content.readlines()
    for i in save_list:
        todolist.insert(END,i)"""

open_list()


todolist['yscrollcommand'] = scrollbar.set
# run
root.mainloop()
