import tkinter as tk
from tkinter import messagebox

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.todo_list = []

        # Create GUI components
        self.task_entry = tk.Entry(root)
        self.task_entry.pack()

        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.pack()

        self.task_listbox = tk.Listbox(root)
        self.task_listbox.pack()

        self.update_button = tk.Button(root, text="Update Task", command=self.update_task)
        self.update_button.pack()

        self.delete_button = tk.Button(root, text="Delete Task", command=self.delete_task)
        self.delete_button.pack()

    def add_task(self):
        task_name = self.task_entry.get()
        if task_name:
            self.todo_list.append(task_name)
            self.update_task_listbox()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Please enter a task name.")

    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.todo_list:
            self.task_listbox.insert(tk.END, f"■ {task}")

    def update_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            selected_index = int(selected_index[0])
            new_task_name = self.task_entry.get()
            if new_task_name:
                self.todo_list[selected_index] = new_task_name
                self.update_task_listbox()
                self.task_entry.delete(0, tk.END)
            else:
                messagebox.showwarning("Input Error", "Please enter a new task name.")
        else:
            messagebox.showwarning("Selection Error", "Please select a task to update.")
            
    def delete_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            task_index = int(selected_task_index[0])
            self.todo_list.pop(task_index)
            self.update_task_listbox()
        else:
            messagebox.showwarning("No Task Selected", "Please select a task to delete.")       

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("400x400")
    app = ToDoApp(root)
    root.mainloop()
