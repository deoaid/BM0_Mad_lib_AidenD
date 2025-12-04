from tkinter import *
#need to install on all machines
from tkmacosx import Button

# Create the main window
root = Tk()
root.title("Three Buttons")

#Set size of window
root.geometry("600x300")

# Create buttons
red_button = Button(root, text="Red", background='red')
yellow_button = Button(root, text="Yellow", background='yellow')
green_button = Button(root, text="Green", background='green')


#Add a label
label = Label(root, text="This is a stoplight.")
label2 = Label(root, text="Here, I can add a bunch of text into the letterbox!")
set_background_color(0, 0, 255)

# Place widgets in window (with pack function!)
red_button.pack()
yellow_button.pack()
green_button.pack()
label.pack()

label2.pack()


# Start the GUI event loop
root.mainloop()