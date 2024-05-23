import pickle
from datetime import datetime

class Task:
    def __init__(self, description, priority, deadline):
        self.description = description
        self.priority = priority
        self.deadline = deadline
        self.created_at = datetime.now()
    
    def __repr__(self):
        return (f"Task(description={self.description}, priority={self.priority}, "
                f"deadline={self.deadline}, created_at={self.created_at})")
    
    def __str__(self):
        return (f"Description: {self.description}\n"
                f"Priority: {self.priority}\n"
                f"Deadline: {self.deadline.strftime('%Y-%m-%d %H:%M:%S')}\n"
                f"Created At: {self.created_at.strftime('%Y-%m-%d %H:%M:%S')}\n")


class TaskManager:
    def __init__(self, storage_file='tasks.pkl'):
        self.tasks = []
        self.storage_file = storage_file
        self.load_tasks()
    
    def add_task(self, task):
        self.tasks.append(task)
        self.save_tasks()
    
    def remove_task(self, task_description):
        self.tasks = [task for task in self.tasks if task.description != task_description]
        self.save_tasks()
    
    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        for task in self.tasks:
            print(task)
            print("-" * 40)
    
    def save_tasks(self):
        with open(self.storage_file, 'wb') as file:
            pickle.dump(self.tasks, file)
    
    def load_tasks(self):
        try:
            with open(self.storage_file, 'rb') as file:
                self.tasks = pickle.load(file)
        except FileNotFoundError:
            self.tasks = []

def main():
    task_manager = TaskManager()
    
    while True:
        print("Task Manager Menu:")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. View Tasks")
        print("4. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            description = input("Enter task description: ")
            priority = input("Enter task priority (High, Medium, Low): ")
            deadline_str = input("Enter task deadline (YYYY-MM-DD HH:MM): ")
            try:
                deadline = datetime.strptime(deadline_str, '%Y-%m-%d %H:%M')
                task = Task(description, priority, deadline)
                task_manager.add_task(task)
                print("Task added successfully.")
            except ValueError:
                print("Invalid date format. Please use YYYY-MM-DD HH:MM.")
        
        elif choice == '2':
            description = input("Enter the description of the task to remove: ")
            task_manager.remove_task(description)
            print("Task removed successfully.")
        
        elif choice == '3':
            print("Viewing tasks:")
            task_manager.view_tasks()
        
        elif choice == '4':
            print("Exiting Task Manager.")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
