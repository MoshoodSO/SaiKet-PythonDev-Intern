# Importing libraries
import gradio as gr

# Class for todo list
class ToDoList:
    def __init__(self):
        self.TASK = {
            "Undone": [],
            "Done": []
        }

    def add_task(self, task):
        if not task or not task.strip():
            return "Please enter a task."

        task = task.strip().capitalize()

        if task in self.TASK["Undone"] or task in self.TASK["Done"]:
            return f"'{task}' is already in the list"

        self.TASK["Undone"].append(task)
        return "Successfully added"

    def delete_task(self, task):
        if not task or not task.strip():
            return "Please enter a task."

        task = task.strip().capitalize()

        if task in self.TASK["Undone"]:
            self.TASK["Undone"].remove(task)
            return "Task successfully deleted"

        elif task in self.TASK["Done"]:
            self.TASK["Done"].remove(task)
            return "Task successfully deleted from done list"

        else:
            return "Task not in your todo list"

    def move_done(self, task):
        if not task or not task.strip():
            return "Please enter a task."

        task = task.strip().capitalize()

        if task in self.TASK["Undone"]:
            self.TASK["Undone"].remove(task)
            self.TASK["Done"].append(task)
            return "Task completed"

        else:
            return "Task not in your todo list"


# Initializing the todo list
# Create the todo object
todo = ToDoList()

# Function to display the current tasks
def display_tasks():
    undone = todo.TASK["Undone"]
    done = todo.TASK["Done"]

    undone_text = " - ".join(undone) if undone else "No undone tasks."

    done_text = " - ".join(done) if done else "No completed tasks."
    return f"""
    ## 📝 Undone Tasks: {undone_text}
    ---
    ## ✅ Done Tasks: {done_text}
    """


# Add task and refresh list
def add_and_refresh(task):
    message = todo.add_task(task)
    return message, display_tasks(), ""


# Delete task and refresh list
def delete_and_refresh(task):
    message = todo.delete_task(task)
    return message, display_tasks(), ""


# Complete task and refresh list
def complete_and_refresh(task):
    message = todo.move_done(task)
    return message, display_tasks(), ""


# Gradio interface
with gr.Blocks(title="To-Do List") as app:

    gr.Markdown("# 📝 To-Do List")

    gr.Markdown("Add tasks, delete tasks, or mark tasks as completed.")

    task_input = gr.Textbox(label="Task",placeholder="Enter a task...",)

    with gr.Row():
        add_btn = gr.Button("➕ Add Task", variant="primary")
        complete_btn = gr.Button("✅ Complete Task")
        delete_btn = gr.Button("🗑️ Delete Task")

    message = gr.Textbox(label="Status",interactive=False)

    # Task list is ALWAYS at the bottom
    task_display = gr.Markdown(display_tasks())

    # Every button refreshes the task list
    add_btn.click(fn=add_and_refresh, inputs=task_input, outputs=[message, task_display, task_input])
    complete_btn.click(fn=complete_and_refresh, inputs=task_input, outputs=[message, task_display, task_input])
    delete_btn.click(fn=delete_and_refresh, inputs=task_input, outputs=[message, task_display, task_input])


app.launch()         # To create a public link, set `share=True` in `launch()`.


