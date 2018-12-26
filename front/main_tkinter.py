"""Tkinter GUI."""

import tkinter as tk
from tkinter import messagebox

def view_command():
    list1.delete(0, tk.END)
    list1.insert(tk.END, "Hello")


def search_command():
    list1.delete(0, END)
    for row in backend.search(song_text.get(), artist_text.get(), album_text.get(), year_text.get()):
        list1.insert(END, row)


def add_command():
    backend.insert(song_text.get(), artist_text.get(), album_text.get(), year_text.get())
    view_command()


def delete_command():
    index = list1.curselection()[0]
    selected_tuple = list1.get(index)
    backend.delete(selected_tuple[0])
    list1.delete(index)


def update_command():
    backend.update(id=selected_id, song=e1.get(), artist=e2.get(), album=e3.get(), year=e4.get())
    view_command()


def user_set():
    """Sets user."""
    global user_name
    global user_color
    user_name = name_input.get()
    user_color = color_input.get()
    window.destroy()


def get_selected_row(event):
    index = list1.curselection()[0]
    selected_tuple = list1.get(index)

    global selected_id
# update command will need this, so we must make it global
    selected_id = selected_tuple[0]
    list1.insert(tk.END, "Bye")


def exit():
    """Print me."""
    if messagebox.askokcancel("Quit", "Do you really wish to quit?"):
        window.destroy()


# First popup used to set up the user
window = tk.Tk()
window.wm_title("User Setup")

l1 = tk.Label(window, text="Please enter your name and color.")
l1.grid(row=0, columnspan=2)
l2 = tk.Label(window, text="Name")
l2.grid(row=1, column=0)
l3 = tk.Label(window, text="")
l3.grid(row=2, column=0)

name_input = tk.StringVar()
e1 = tk.Entry(window, textvariable=name_input, width=25)
e1.grid(row=1, column=1)

color_input = tk.StringVar(window)
color_input.set("Red")
color_option = tk.OptionMenu(
    window, color_input, "Red", "Blue", "Orange", "White")
color_option.grid(row=3, columnspan=2)

b1 = tk.Button(window, text="Contiune", width=25, command=user_set)
b1.grid(row=4, columnspan=2)

window.mainloop()

# second popup used to set up initial board
window = tk.Tk()
window.wm_title("User Setup")

l1 = tk.Label(window, text="Please enter your name and color.")
l1.grid(row=0, columnspan=2)
l2 = tk.Label(window, text="Name")
l2.grid(row=1, column=0)
l3 = tk.Label(window, text="")
l3.grid(row=2, column=0)

name_input = tk.StringVar()
e1 = tk.Entry(window, textvariable=name_input, width=25)
e1.grid(row=1, column=1)

color_input = tk.StringVar(window)
color_input.set("Red")
color_option = tk.OptionMenu(
    window, color_input, "Red", "Blue", "Orange", "White")
color_option.grid(row=3, columnspan=2)

b1 = tk.Button(window, text="Contiune", width=25, command=user_set)
b1.grid(row=4, columnspan=2)

window.mainloop()

# Main UI
window = tk.Tk()
window.wm_title("Settlers! " + user_name + " " + str(user_color))

l1 = tk.Label(window, text="Song")
l1.grid(row=0, column=0)

l2 = tk.Label(window, text="Arist")
l2.grid(row=0, column=2)

l3 = tk.Label(window, text="Album")
l3.grid(row=1, column=0)

l3 = tk.Label(window, text="Year")
l3.grid(row=1, column=2)

#########
# Display Titles# Display text entry fields
song_text = tk.StringVar()
e1 = tk.Entry(window, textvariable=song_text, width=35)
e1.grid(row=0, column=1)

artist_text = tk.StringVar()
e2 = tk.Entry(window, textvariable=artist_text, width=25)
e2.grid(row=0, column=3)

album_text = tk.StringVar()
e3 = tk.Entry(window, textvariable=album_text, width=35)
e3.grid(row=1, column=1)

year_text = tk.StringVar()
e4 = tk.Entry(window, textvariable=year_text, width=25)
e4.grid(row=1, column=3)

############################
# display listbox and attached a Scrollbar
list1 = tk.Listbox(window, height=9, width=60)
list1.grid(row=2, column=0, rowspan=6, columnspan=2)
# we want to span across multiple rows and columns

list1.bind("<<ListboxSelect>>", get_selected_row)

sb1 = tk.Scrollbar(window)
sb1.grid(row=2, column=2, rowspan=6, sticky=tk.N+tk.S+tk.W)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

# Display Buttons
b1 = tk.Button(window, text="View All songs", width=25, command=view_command)
b1.grid(row=2, column=3)
b2 = tk.Button(window, text="Search ", width=25, command=search_command)
b2.grid(row=3, column=3)
b3 = tk.Button(window, text="Add Song", width=25, command=add_command)
b3.grid(row=4, column=3)
b4 = tk.Button(window, text="Update Song", width=25, command=update_command)
b4.grid(row=5, column=3)
b5 = tk.Button(window, text="Delete Song", width=25, command=delete_command)
b5.grid(row=6, column=3)
b6 = tk.Button(window, text="Exit", width=25, command=exit)
b6.grid(row=7, column=3)

window.mainloop()
