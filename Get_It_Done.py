
import tkinter as tk
from tkinter import messagebox, simpledialog, ttk
import json
import os

tasks = []
theme_color = "#c38091"  # Default khaki


def showMotivationalPopup():
    import random
    messages = [
        "💪 Keep going, you're doing great!",
        "🚀 Almost there—don’t quit now!",
        "🌟 Progress is progress, no matter how small!",
        "🌈 Take a deep breath—you’ve got this!",
        "🔥 Stay focused! You’re closer than you think."
    ]
    messagebox.showinfo("Motivation", random.choice(messages))

def saveTasks():
    with open("tasks.json", "w") as f:
        json.dump(tasks, f)
    messagebox.showinfo("Save Tasks", "Tasks saved successfully!")

def loadTasks():
    global tasks
    if os.path.exists("tasks.json"):
        with open("tasks.json", "r") as f:
            tasks = json.load(f)
        refreshTaskList()
        if tasks:
            messagebox.showinfo("Load Tasks", "Tasks loaded successfully!")

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

def unloadTask():
    selected = task_listbox.curselection()
    if selected:
        index = selected[0]
        confirm = messagebox.askyesno("Unload Task", f"Are you sure you want to delete: '{tasks[index]['task']}'?")
        if confirm:
            tasks.pop(index)
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
    theme_options = {
        "Default Pink": "#c38091",
        "Sky Blue": "#87ceeb",
        "Mint Green": "#98ff98",
        "Light Gray": "#d3d3d3",
        "Lavender": "#e6e6fa"
    }

    def apply_selected_theme(selection):
        global theme_color
        theme_color = theme_options[selection]
        main_frame.config(bg=theme_color)
        for widget in main_frame.winfo_children():
            widget.config(bg=theme_color)
        for widget in button_frame.winfo_children():
            widget.config(bg=theme_color)

    # Prompt user with a dropdown
    theme_window = tk.Toplevel(app)
    theme_window.title("Choose Theme")
    tk.Label(theme_window, text="Select a Theme:").pack(pady=5)
    selected_theme = tk.StringVar(theme_window)
    selected_theme.set("Default Pink")
    theme_menu = ttk.Combobox(theme_window, textvariable=selected_theme, values=list(theme_options.keys()))
    theme_menu.pack(pady=5)

    def confirm():
        apply_selected_theme(selected_theme.get())
        theme_window.destroy()

    tk.Button(theme_window, text="Apply Theme", command=confirm).pack(pady=10)


app = tk.Tk()
app.title("Get It Done!!")
app.geometry("400x400")

main_frame = tk.Frame(app, bg=theme_color)
main_frame.pack(fill="both", expand=True)

task_listbox = tk.Listbox(main_frame, width=50)
task_listbox.pack(pady=10)

progress_var = tk.StringVar()
progress_label = tk.Label(main_frame, textvariable=progress_var, bg=theme_color, fg="black")
progress_label.pack()

button_frame = tk.Frame(main_frame, bg=theme_color)
button_frame.pack(pady=10)

tk.Button(button_frame, text="Add Task", command=addTask).grid(row=0, column=0, padx=5)
tk.Button(button_frame, text="Mark Completed", command=markCompleted).grid(row=2, column=1, padx=5, pady=5)
tk.Button(button_frame, text="Unload Task", command=unloadTask).grid(row=1, column=2, padx=5)
tk.Button(button_frame, text="Save", command=saveTasks).grid(row=0, column=1, padx=5)
tk.Button(button_frame, text="Load", command=loadTasks).grid(row=1, column=0, padx=5, pady=5)
tk.Button(button_frame, text="Set Theme", command=setTheme).grid(row=0, column=2, columnspan=2, pady=5)

loadTasks()
app.mainloop()
