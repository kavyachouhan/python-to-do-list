class Task:
    def __init__(self, title):
        self.title = title
        self.completed = False

    def mark_completed(self):
        self.completed = True

class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, title):
        self.tasks.append(Task(title))

    def delete_task(self, index):
        del self.tasks[index]

    def complete_task(self, index):
        self.tasks[index].mark_completed()

    def display_tasks(self):
        for i, task in enumerate(self.tasks):
            status = "Done" if task.completed else "Not Done"
            print(f"{i+1}. {task.title} - {status}")

def main():
    todo_list = TodoList()
    while True:
        print("\n1. Add Task\n2. Delete Task\n3. Complete Task\n4. Display Tasks\n5. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            task = input("Enter task name: ")
            todo_list.add_task(task)
        elif choice == 2:
            index = int(input("Enter task number to delete: "))
            todo_list.delete_task(index - 1)
        elif choice == 3:
            index = int(input("Enter task number to mark as completed: "))
            todo_list.complete_task(index - 1)
        elif choice == 4:
            todo_list.display_tasks()
        elif choice == 5:
            break

if __name__ == "__main__":
    main()
