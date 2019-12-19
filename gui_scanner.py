import tkinter as tk
from time import strftime
import portscanner
window = tk.Tk() # you may also see it named as "root" in other sources

window.title("FAST PORT SCANNER") # self explanatory!
window.geometry("300x300") # size of the window when it opens
window.minsize(width=300, height=300) # you can define the minimum size of the window like this
window.resizable(width="false", height="false") # change to false if you want to prevent resizing

# WIDGETS
# three frames on top of each other
frame_header = tk.Frame(window, borderwidth=2, pady=2)
center_frame = tk.Frame(window, borderwidth=2, pady=5)
bottom_frame = tk.Frame(window, borderwidth=2, pady=5)
log_frame = tk.Frame(window, borderwidth=2, pady=5)

frame_header.grid(row=0, column=0)
center_frame.grid(row=1, column=0)
bottom_frame.grid(row=2, column=0)
log_frame.grid(row=3, column=0)


def check_target(event):
    """Forces the input TO to be lower case"""
    target_text.set(target_text.get().lower())   
    

def close_app():
    window.destroy()


def run_app():
    print('run')
    portscanner.open_ports = []
    log_text.config(state=tk.NORMAL)
    scan_target = target_text.get()
    ports = portscanner.read_ports_from_file()
    results = portscanner.scan(ports, scan_target)
    
    log_text.insert(tk.END, 'Target: {}\n'.format(scan_target))
    for port in results:
        log_text.insert(tk.END, 'Open port found: {}{}'.format(str(port), '\n'))
    


def save_result():
    log_text.delete(1.0, tk.END)


# label header to be placed in the frame_header
header = tk.Label(frame_header, text = "PORT SCANER", bg='grey', fg='black', height='1', width='29', font=("Helvetica 12 bold"))
# inside the grid of frame_header, place it in the position 0,0
header.grid(row=0, column=0)


# two additional frames go inside the center_frame
frame_main_1 = tk.Frame(center_frame, borderwidth=2, relief='sunken')

# Put it simply: StringVar() allows you to easily track tkinter variables and see if they were read, changed, etc
# check resources here for more details: http://effbot.org/tkinterbook/variable.htm

target_text = tk.StringVar(window, value='google.com')

# and populate them with the labels referring to the inputs we want from the user
target_label = tk.Label(frame_main_1, text = "TARGET: ")
target = tk.Entry(master=frame_main_1, textvariable=target_text)

target.bind("<KeyRelease>", check_target)
# this part is just to display the labels inside the center frame
# the order which we pack the items is important
frame_main_1.pack(fill='x', pady=2)
target_label.pack(side='left')
target.pack(side='left', padx=5)

# Button
button_run = tk.Button(bottom_frame, text="Scan", command=run_app, bg='dark green', fg='white', relief='raised', width=10, font=('Helvetica 9 bold'))
button_run.grid(column=0, row=0, sticky='w', padx=2, pady=2)

button_save = tk.Button(bottom_frame, text="Clear", command=save_result, bg='red', fg='white', relief='raised', width=10, font=('Helvetica 9 bold'))
button_save.grid(column=1, row=0, sticky='w', padx=2, pady=2)

log_label = tk.Label(log_frame, text = "Logging:", bg='white', fg='black', height='1', width='29', font=("Helvetica 10"))
log_text = tk.Text(log_frame, width=29, height=8)

log_label.grid(row=0, column=0)
log_text.grid(row=1, column=0)

window.mainloop()