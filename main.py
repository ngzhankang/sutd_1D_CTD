# import library
import tkinter as tk
import json, copy

# open info.json file in datafiles folder to read the content as a dictionary
with open('datafiles/info.json', 'r') as file:
    courses = json.load(file)

# open grades.json file in datafiles folder to read the content as a dictionary
with open('datafiles/grades.json', 'r') as file:
    grade_dict = json.load(file)



def first_input_page():
    # Clear all widgets from the window
    for widget in root.winfo_children():
        widget.destroy()
    
    # Recreate the input page
    global name_entry, label_entry
    name_label = tk.Label(root, text="What is your name?", font=("Helvetica", 12))
    name_label.pack(pady=5)
    name_entry = tk.Entry(root)
    name_entry.pack(pady=5)
    
    term_label = tk.Label(root, text="Please enter your current term (1-3):", font=("Helvetica", 12))
    term_label.pack(pady=5)
    term_entry = tk.Entry(root)
    term_entry.pack(pady=5)
    
    submit_button = tk.Button(root, text="Submit", command=select_mod_page)
    submit_button.pack(pady=20)

def select_mod_page():
    # Clear all widgets from the window
    for widget in root.winfo_children():
        widget.destroy()

    CheckVar1 = tk.IntVar()
    CheckVar2 = tk.IntVar()
    C1 = tk.Checkbutton(root, text = "Music", variable = CheckVar1, \
    onvalue = 1, offvalue = 0, height=5, \
    width = 20, )
    C2 = tk.Checkbutton(root, text = "Video", variable = CheckVar2, \
    onvalue = 1, offvalue = 0, height=5, \
    width = 20)
    submit_button = tk.Button(root, text="Submit", command=second_input_page)
    submit_button.pack(pady=20)
    C1.pack()
    C2.pack()
    submit_button.pack()

    root.mainloop()

def second_input_page():
    # Clear all widgets from the window
    for widget in root.winfo_children():
        widget.destroy()
    
    # Recreate the input page
    global mod1_entry, mod2_entry
    mod1_label = tk.Label(root, text="WHATS UR GRADE for mod1:", font=("Helvetica", 12))
    mod1_label.pack(pady=5)
    mod1_entry = tk.Entry(root)
    mod1_entry.pack(pady=5)
    
    mod2_label = tk.Label(root, text="what is ur grade for mod2:", font=("Helvetica", 12))
    mod2_label.pack(pady=5)
    mod2_entry = tk.Entry(root)
    mod2_entry.pack(pady=5)
    
    submit_button = tk.Button(root, text="Submit", command=switch_to_new_page)
    submit_button.pack(pady=20)

def switch_to_new_page():
    # Retrieve the inputs
    input1 = mod1_entry.get()
    input2 = mod2_entry.get()
    
    # Clear all widgets from the window
    for widget in root.winfo_children():
        widget.destroy()
    
    # Display the new page
    label_new = tk.Label(root, text="New Page", font=("Helvetica", 16))
    label_new.pack(pady=20)
    
    result_label = tk.Label(root, text=f"You entered: {input1} and {input2}", font=("Helvetica", 12))
    result_label.pack(pady=10)
    
    back_button = tk.Button(root, text="Go Back", command=first_input_page)
    back_button.pack(pady=10)

# Create the main window
root = tk.Tk()
root.title("Tkinter Input Example")
root.geometry("300x200")

# Initialize the first page
entry1 = None
entry2 = None
first_input_page()

# Start the Tkinter event loop
root.mainloop()
