def get_inf_stu():
    name = input("Enter name : ")
    age = int(input("Enter age : "))
    grades = list(map(int, input("Enter grades : ").split()))
    return{"name": name , "age" : age , "grades" : grades}

def average_grades(grades):
    return sum(grades) / len(grades)

def save_stu(students):
    with open ("students.txt" , "a") as file:
        file.write(f"{students['name']}, {students['age']} , {",".join(map(str, students['grades']))}\n")
        
def read_stu_file():
    students = []
    try:
        with open("students.txt" , "r") as file:
            for line in file:
                name , age , *grades = line.strip().split(",")
                students.append({"name" : name.strip() , "age" : int(age) , "grades" : list(map(int, grades))})
    except FileNotFoundError:
        print("Data not found. ")    
        return students

def disply_stu(students):
    for student in students:
        avg = average_grades(student["grades"])
        print(f"Name : {student['name']} , Age : {student['age']} , Average grades : {avg: .2f}")   
        
def sorted_by_grades(students):
    return sorted(students, key= lambda x : average_grades(x['grades']) , reverse = True)

def search_student(students, name):
     for student in students:
         if student['name'].lower() == name.lower():
             avg = average_grades(student['grades'])
             print(f"Name : {student['name']} , Age : {student['age']} , Average grades : {avg: .2f}")
             return
         print(f"student {name} not found. ")
         
def main_stu():
    students = read_stu_file()
    
    while True:
        print("Students managment system. ")
        print("1.Add new student.")
        print("2.Display students.")
        print("3.Sort students by average.")
        print("4.Search student by name.")
        print("5.Exite.")
        
        choice = input("Enter your choice : 1/2/3/4/5 ")
        if choice == '1':
            student = get_inf_stu()
            save_stu(student)
            students.append(student)
        elif choice == '2':
            disply_stu(students)
        elif choice == '3':
            sorted_students =  sorted_by_grades(students)
            disply_stu(sorted_students)
        elif choice == '4':
            name = input("Enter the name to search: ")
            search_student(students, name) 
        elif choice == '5':
            print("Exite..")
            break
        else:
            print("Invalid choice.")
            
if __name__ == "__main__":
    main_stu()   