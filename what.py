To_Do_list = []


#show task
def show_task(To_Do_list):
 
 if not To_Do_list:
   print("list is empty")
 for i,  val in enumerate(To_Do_list , start=1):
   
   print (f"{i}. {val}")


#add task
def add_task():
   me =  input("add task:")
   To_Do_list.append(me)


#delete task
def delete_task():
   index = int(input("remove element at index (0-based)"))  
   if 0 <= index <len(To_Do_list):
    removed = To_Do_list.pop(index)
    print(f"removed: {removed}")
   else:
     print("invalid index")
 


#menu list
while True:
    print("\nMenu:")
    print("1. Show Tasks")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        show_task(To_Do_list)
    elif choice == "2":
        add_task()
    elif choice == "3":
        delete_task()
    elif choice == "4":
        print("Exiting...")
        break  
    else:
        print("Invalid choice, try again")