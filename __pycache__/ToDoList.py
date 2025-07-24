TodoList=[]
while True:
    for i in range(0,len(TodoList)):
        print(f"{i+1}. {TodoList[i]}")
            
    x=input("Enter Task for Your ToDo List (or type 'exit' to finish): ")
  
    if x.lower() == 'exit':
        break
    elif x.lower()== 'clear':
        TodoList.clear()
        print("ToDo List cleared.")
    
    else:
        TodoList.append(x)
        print(f"Task '{x}' added to your ToDo List.")
    