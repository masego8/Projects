#To Do List

toDoList = []
completedTasks = []

def choice():

    while True:
        choice = int(input("(1) View To Do list   (2) Add to To Do List    (3) Delete list item   (4)  Mark As Done (5)  Close app \n"))

        if choice == 5: 
            break

        elif choice == 1:
            view()

        elif choice == 2:
            upload()

        elif choice == 3:
            delete()

        elif choice == 4:
            mark()
        
        if choice == 5: 
            break


        elif choice > 5:
            continue

def upload():
    post = input("Enter Task: ")
    toDoList.append(post)

def delete():
   
   for x in range(len(toDoList)):
        print((toDoList[x]))

        pick = int(input("which note would you like to delete? "))
        toDoList.remove(toDoList[pick])

def mark(post):
    while post > 0:
        print(enumerate(toDoList))
        pickD = int(input("which note would you like to mark as done? "))
        completedTasks.append(toDoList[pickD])
        toDoList.remove(toDoList[pickD])

def view():
    print(toDoList)



choice()