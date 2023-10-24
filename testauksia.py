import tkinter as tk

def start_timer():
    global remaining_time
    remaining_time = int(entry.get())
    update_timer()

def update_timer():
    global remaining_time  # Declare remaining_time as a global variable
    if remaining_time > 0:
        label.config(text=f"Time left: {remaining_time} seconds")
        remaining_time -= 1
        root.after(1000, update_timer)  # Update every 1000 milliseconds (1 second)
    else:
        label.config(text="Time's up!")

root = tk.Tk()
root.title("Visible Countdown Timer")

label = tk.Label(root, text="Enter the time in seconds:")
label.pack(pady=10)

entry = tk.Entry(root)
entry.pack()

start_button = tk.Button(root, text="Start Timer", command=start_timer)
start_button.pack(pady=10)

root.mainloop()



