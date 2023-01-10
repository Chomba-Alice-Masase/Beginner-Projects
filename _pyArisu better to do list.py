from tkinter import *
from tkinter.font import Font
# With guidance from Codemy tutorial
#  we're going to make a better to do list application
root = Tk()
root.title("To do list")
root.geometry("300x400")  # .geometry determines window size
# let's add some font style because why not.
root.config(bg="#59788E")
my_Font = Font(
    family="Comic Sans MS",
    size=15,
    weight="bold"
)
The_Frame = Frame(root) # The frame will hold our widgets
The_Frame.pack(pady=15)
The_Frame.config(bg="#59788E")
#  We will create a listbox to display our  list items
my_Listbox = Listbox(The_Frame,  # the listbox is used to display a list in a gui
                     font=my_Font,
                     width=25,
                     height=5,
                     bg="SystemButtonFace",
                     bd=0,
                     fg="#1167b1",
                     highlightthickness=0,
                     selectbackground="#03254c",  # This will chose the color of our highlight
                     activestyle="none"  # removes underline
                     )

my_Listbox.pack(side=LEFT, fill=BOTH)
the_List = ["Water reptiles", "Feed big cats", "Give tour at 12AM"]  # Sample list
# This is how we will add items to our list box
for task in the_List:
    my_Listbox.insert(END, task)

# Creating the scrollbar widget fr when your list gets too long
The_scrollbar = Scrollbar(The_Frame)
The_scrollbar.pack(side=RIGHT, fill=BOTH)
# Adding the scroll bar
my_Listbox.config(yscrollcommand=The_scrollbar.set)
The_scrollbar.config(command=my_Listbox.yview())

# We create an entrybox to receive entries
entries = Entry(root, font=("Comic Sans MS", 20))  #Choosing font that will be in our entry box
entries.pack(pady=5)
# we create a frame to hold the buttons
button_frame = Frame(root)
button_frame.pack(pady=5)


# our functions
def checker():
    my_Listbox.itemconfig(my_Listbox.curselection(),  #The currently selected item will be crossed off
                          fg="#59788E")  # color change when clicked
    #Get rid of selection bar upong clicking
    my_Listbox.selection_clear(0, END)


def unchecker():
        my_Listbox.itemconfig(my_Listbox.curselection(),  # The currently selected item will be crossed off
                              fg="#1167b1")  # color change when clicked
        # Get rid of selection bar upong clicking
        my_Listbox.selection_clear(0, END)
        Checked = False


def remover():
    my_Listbox.delete(ANCHOR)


def add():
    my_Listbox.insert(END, entries.get())
    entries.delete(0, END)


def clear():
    my_Listbox.delete(0, END)


Check = Button(button_frame, width=35, height=1, text="Check", bg="#d0efff", fg="#03254c", command=checker)
Remove = Button(button_frame, width=35, height=1, text="Remove", bg="#d0efff", fg="#03254c", command=remover)
Add = Button(button_frame, width=35, height=1, text="Add", bg="#d0efff", fg="#03254c", command=add)
Clear = Button(button_frame, width=35, height=1, text="Clear", bg="#d0efff", fg="#03254c", command=clear)
Uncheck = Button(button_frame, width=35, height=1, text="Uncheck", bg="#d0efff", fg="#03254c", command=unchecker)

Check.grid(row=0, column=0, )
Remove.grid(row=1, column=0)
Add.grid(row=2, column=0)
Clear.grid(row=3, column=0)
Uncheck.grid(row=4, column=0)
root.mainloop()
