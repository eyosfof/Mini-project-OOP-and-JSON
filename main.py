
import json
import os

class Task:
    def __init__(self, task_id, title, completed=False):
        self.id = task_id
        self.title = title
        self.completed = completed

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "completed": self.completed
        }

    @staticmethod
    def from_dict(data):
        return Task(data["id"], data["title"], data["completed"])


class TodoApp:
    def __init__(self, filename="todos.json"):
        self.filename = filename
        self.tasks = []
        self.load_tasks()

    def load_tasks(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as file:
                data = json.load(file)
                self.tasks = [Task.from_dict(task) for task in data]

    def save_tasks(self):
        with open(self.filename, "w") as file:
            json.dump([task.to_dict() for task in self.tasks], file, indent=4)

    def add_task(self, title):
        task_id = 1 if not self.tasks else self.tasks[-1].id + 1
        new_task = Task(task_id, title)
        self.tasks.append(new_task)
        self.save_tasks()
        print("Task added successfully.")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.")
            return
        for task in self.tasks:
            status = "Completed" if task.completed else "Not Completed"
            print(f"ID: {task.id} | Title: {task.title} | Status: {status}")

    def update_task(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                new_title = input("Enter new title (leave blank to keep current): ")
                if new_title:
                    task.title = new_title
                status_input = input("Mark as completed? (yes/no): ").lower()
                task.completed = True if status_input == "yes" else False
                self.save_tasks()
                print("Task updated successfully.")
                return
        print("Task not found.")

    def delete_task(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                self.tasks.remove(task)
                self.save_tasks()
                print("Task deleted successfully.")
                return
        print("Task not found.")


def main():
    app = TodoApp()

    while True:
        print("\n==== Todo App Menu ====")
        print("1. Add Todo")
        print("2. View Todos")
        print("3. Update Todo")
        print("4. Delete Todo")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            title = input("Enter task title: ")
            app.add_task(title)
        elif choice == "2":
            app.view_tasks()
        elif choice == "3":
            task_id = int(input("Enter task ID to update: "))
            app.update_task(task_id)
        elif choice == "4":
            task_id = int(input("Enter task ID to delete: "))
            app.delete_task(task_id)
        elif choice == "5":
            print("Exiting application.")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
