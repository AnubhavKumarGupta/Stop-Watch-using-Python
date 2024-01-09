# Importing the required modules
import tkinter as Tkinter
from datetime import datetime

# Initializing global variables
counter = 0
running = False


# Function to update the label with the stopwatch time
def counter_label(label):
    def count():
        # Checking if the stopwatch is running
        if running:
            global counter

            # To manage the initial delay.
            if counter == 0:
                display = "Ready!"
            else:
                # Converting the elapsed time to a formatted string (HH:MM:SS)
                tt = datetime.utcfromtimestamp(counter)
                string = tt.strftime("%H:%M:%S")
                display = string

            # Updating the label with the formatted time
            label["text"] = display

            # Setting a delay of 1000 milliseconds (1 second) and calling count function again
            label.after(1000, count)
            counter += 1

    # Triggering the start of the counter.
    count()


# Function to start the stopwatch
def Start(label):
    global running
    running = True
    counter_label(label)
    start["state"] = "disabled"
    stop["state"] = "normal"
    reset["state"] = "normal"


# Function to stop the stopwatch
def Stop():
    global running
    start["state"] = "normal"
    stop["state"] = "disabled"
    reset["state"] = "normal"
    running = False


# Function to reset the stopwatch
def Reset(label):
    global counter
    counter = 0

    # If reset is pressed after pressing stop.
    if not running:
        reset["state"] = "disabled"
        label["text"] = "00:00:00"
    # If reset is pressed while the stopwatch is running.
    else:
        label["text"] = "00:00:00"


# Creating the main window using Tkinter
root = Tkinter.Tk()
root.title("Stopwatch")

# Fixing the window size.
root.minsize(width=250, height=70)

# Creating a label to display the stopwatch time
label = Tkinter.Label(root, text="Ready!", fg="black", font="Verdana 30 bold")
label.pack()

# Creating a frame to hold the buttons
f = Tkinter.Frame(root)

# Creating Start, Stop, and Reset buttons
start = Tkinter.Button(f, text="Start", width=6, command=lambda: Start(label))
stop = Tkinter.Button(f, text="Stop", width=6, state="disabled", command=Stop)
reset = Tkinter.Button(
    f, text="Reset", width=6, state="disabled", command=lambda: Reset(label)
)

# Packing the buttons into the frame
f.pack(anchor="center", pady=5)
start.pack(side="left")
stop.pack(side="left")
reset.pack(side="left")

# Running the Tkinter main loop
root.mainloop()
