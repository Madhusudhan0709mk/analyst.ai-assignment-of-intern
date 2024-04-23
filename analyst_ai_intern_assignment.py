class todo_tasks:
    tasks = []


    def add(self,task_desc):
        self.tasks.append({"task_desc":task_desc,"completed":False})

    def deleteitem(self,index):
        if index < len(self.tasks):
            del self.tasks[index]
            print("deleted the choosed task")


    def mark_comp(self,index):
        if index <len(self.tasks):
            self.tasks[index]['completed']=True
            print("marked as completed")


    def tasks_view(self):
        for i,task in enumerate(self.tasks):
            print(f'{i-1}. {'[x]' if task['completed'] else '[]'} {task['task_desc']}')
        else:
            print('no tasks yet')

while True:
    print("\n To-Do List Application")
    print("1. Add Task")
    print("2. Delete Task")
    print("3. Mark Task as Completed")
    print("4. View Tasks")
    print("5. Exit")
    choice = int(input("enter the choice as per given number "))
    
    tasks = todo_tasks()
    
    if choice == 1:
            task_description = input("Enter task description: ")
            tasks.add(task_description)
    elif choice == 2:
        index = int(input("Enter index of task to delete: ")) - 1
        tasks.deleteitem(index)
    elif choice == 3:
        index = int(input("Enter index of task to mark as completed: ")) - 1
        tasks.mark_comp(index)
    elif choice == 4:
        tasks.tasks_view()
    elif choice == 5:
        print("Exiting To-Do List Application.")
        break
    else:
        print("Invalid choice. Please try again.")
        


    
    



