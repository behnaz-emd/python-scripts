import os

def add_task(tasks):
    title = input("Enter the title : ")
    discription = input("Enter discription : ")
    year = int(input("Enter the year: "))
    month = int(input("Enter the month: "))
    day = int(input("Enter the day: "))
    date = f"{year}-{month:02d}-{day:02d}"  

    level = input("Enter the level(hight , medium , low )")
    tasks.append({"title" : title , "discription" : discription , "date" : date , "level" : level , "status": "pending"})
    print(f"task , '{title}' added successfully")
    
def display_task(tasks):
    for task in tasks:
        print(f"title : {task['title']},date : {task['date']},discription:{task['discription']},level : {task['level']},status: {task['status' ]}")
    
def delete_task(tasks, title):
    for task in tasks:
       if task["title"].lower() == title.lower():
        tasks.remove(task)
        print(f"Task '{title}' removed successfully.")
        return
    print(f"No task found with title '{title}'.")
    


# def task_done(tasks, title):
#     for task in tasks:
#         if task["title"].lower() == title.lower():
#             task["status"] = "done"
#             print(f"task , {title} marked as done. ")
#             return
#     print(f"task , {title} not found. ")
    
def mark_task_done(tasks, title):
    for task in tasks:
        if task["title"].lower() == title.lower():
            task["status"] = "done"
            print(f"Task '{title}' marked as done.")
            return
    print(f"No task found with title '{title}'.")
    
        
def save_task(tasks, filename = "task.txt"):
    with open(filename , "w") as file:
        for task in tasks:
            file.write(f"{task['title']},{task['discription']},{task['date']},{task['level']},{task['status']}\n")
    print("task saved successfully. ")
    
def load(filename = "task.txt"):
    tasks = []
    if os.path.exists(filename):
        with open(filename, "r") as file:
            for line in file:
                title , discription , date , level = line.strip().split(", ")
                tasks.append({"title" : title , "discription" : discription  ,"date": int(date)  , "level" : level , "status": status })
    return tasks

def search_task(tasks, term):
    found = [task for task in tasks if term.lower() in task["title"].lower() or term.lower() in task["discription"].lower()]
    if found:
       for task in found:
        print(f"title : {task['title']} , discription : {task['discription']} , date : {task['date']} , level : {task['level']}")
    else:
        print("no task found. ")
        
def task_manag():
  task = load()
  
  while True:
      print("\n TO DO LIST.")
      print("1.Add task.")
      print("2.Display tasks.")
      print("3.Delete task.")
      print("4.Mark task as done.")
      print("5.Search task.")
      print("6.Save and Exit.")
      
      choice = int(input("Enter your choice (1/2/3/4/5/6) : ")) 
      if choice == 1:
          add_task(task)   
      elif choice == 2:
          display_task(task)
      elif choice == 3:
          title = input("Enter title : ")  
          delete_task(task, title)
      elif choice == 4:
          title = input("Enter title : ")  
          mark_task_done(task, title)
      elif choice == 5:
          term = input("Enter title :")
          search_task(task, term)
      elif choice == 6:
          save_task(task)
          print("Exit...")
          break
      else:
          print("Invalid choice. ")
          
if __name__ == "__main__":
    task_manag()






