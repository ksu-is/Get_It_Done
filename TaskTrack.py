tasks = []

import tkinter as tk
from tkinter import messagebox, simpledialog, ttk
import json
import os

def addTask():
    task_text = simpledialog.askstring("Add Task", "Enter the task:")
    if task_text:
        tasks.append({"task": task_text, "completed": False})
        refreshTaskList()
    task_text = simpledialog.askstring("Add Task", "Enter the task:")
    if task_text:
        tasks.append({"task": task_text, "completed": False})
        refreshTaskList()

def markCompleted():
    selected = task_listbox.curselection()
    if selected:
        index = selected[0]
        tasks[index]["completed"] = True
        refreshTaskList()
        showMotivationalPopup()
    selected = task_listbox.curselection()
    if selected:
        index = selected[0]
        tasks[index]["completed"] = True
        refreshTaskList()
    selected = task_listbox.curselection()
    if selected:
        index = selected[0]
        tasks[index]["completed"] = True
        refreshTaskList()

def refreshTaskList():
    task_listbox.delete(0, tk.END)
    for task in tasks:
        status = "✅" if task["completed"] else "❌"
        task_listbox.insert(tk.END, f"{status} {task['task']}")
    updateProgress()

def updateProgress():
    total = len(tasks)
    completed = sum(1 for t in tasks if t["completed"])
    percent = (completed / total) * 100 if total > 0 else 0
    progress_var.set(f"Progress: {completed}/{total} ({percent:.1f}%)")

def setTheme():
    global theme_color
    color = simpledialog.askstring("Set Theme", "Enter color hex (e.g., #1f77b4 for blue):")
    if color:
        theme_color = color
        main_frame.config(bg=theme_color)
        for widget in main_frame.winfo_children():
            widget.config(bg=theme_color)

app = tk.Tk()
app.title("TaskTrack - Get It Done!!")
app.geometry("400x400")

main_frame = tk.Frame(app, bg=theme_color)
main_frame.pack(fill="both", expand=True)

task_listbox = tk.Listbox(main_frame, width=50)
task_listbox.pack(pady=10)

progress_var = tk.StringVar()
progress_label = tk.Label(main_frame, textvariable=progress_var, bg=theme_color, fg="white")
progress_label.pack()

button_frame = tk.Frame(main_frame, bg=theme_color)
button_frame.pack(pady=10)

tk.Button(button_frame, text="Add Task", command=addTask).grid(row=0, column=0, padx=5)
tk.Button(button_frame, text="Mark Completed", command=markCompleted).grid(row=0, column=1, padx=5)
tk.Button(button_frame, text="Save", command=saveTasks).grid(row=1, column=0, padx=5, pady=5)
tk.Button(button_frame, text="Load", command=loadTasks).grid(row=1, column=1, padx=5, pady=5)
tk.Button(button_frame, text="Set Theme", command=setTheme).grid(row=2, column=0, columnspan=2, pady=5)

loadTasks()
app.mainloop()
