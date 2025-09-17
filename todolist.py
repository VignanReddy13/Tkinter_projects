from tkinter import *

def add_task():
    task = task_entry.get()
    if task != "":
        task_listbox.insert(END, task)
        task_entry.delete(0, END)

def delete_task():
    selected_task = task_listbox.curselection()
    if selected_task:
        task_listbox.delete(selected_task)

def clear_tasks():
    task_listbox.delete(0, END)

root = Tk()
root.title("To-Do List")

# Entry to type task
task_entry = Entry(root, width=40)
task_entry.pack(pady=10)

# Buttons
Button(root, text="Add Task", bg="skyblue",activebackground="skyblue",command=add_task).pack(pady=5)
Button(root, text="Delete Selected Task",bg="red",activebackground="red" ,command=delete_task).pack(pady=5)
Button(root, text="Clear All Tasks",bg="yellow", activebackground="yellow",command=clear_tasks).pack(pady=5)

# Listbox to display tasks
task_listbox = Listbox(root, width=100, height=10, selectmode=SINGLE,bg="orange")
task_listbox.pack(pady=10)

root.mainloop()