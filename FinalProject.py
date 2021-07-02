#THE PROBLEM: This program helps to keep track of the employees in a specific campany/bank or Any organisation and makes it easy to reach the information of a specific employee. It has 4 options to apply. You can either add a new employee for the new comers to the company, or delete an employee for the ones who left there, or search for a specific worker by his/her ID to check if that person is still working there or list all the employees who are currently working in the company.
#GROUP MEMBERS: Çeşminaz İrem Aksoy, Joseph Fersh Nkurunziza, Çağla Özdemir
def menu():
    print("\n1. Add new employee\n2. Delete an employee account")
    print("3. Search for a specific employee\n4. List all the employees")
    print("5. Exit")

def addAccount():
    name = input("Enter name: ")
    id = int(input("Enter id: "))
    department = input("Enter department name: ")
    salary = int(input("Enter salary: "))
    name_list.append(name)
    id_list.append(id)
    department_list.append(department)
    salary_list.append(salary)

def findLocation(id,id_list):
    location = 0
    for i in range(len(id_list)):
        if(id==id_list[i]):
            location = i
    return location

def deleteAccount(location,id_list,name_list,dep_list,salary_list):
    del id_list[location]
    del name_list[location]
    del dep_list[location]
    del salary_list[location]

def findAccount(id,id_list):
    counter = 0
    position = 0
    for i in range(len(id_list)):
        if(id==id_list[i]):
            counter = 1
            position = i
    if(counter==0):
        print("\nThere is no employee with id: " + str(id) + "!\n")
        position = -1
    return position

def searchedAccount(location,id_list,name_list,dep_list,salary_list):
    print("\nInformations of the searched employee:")
    print("Id: " + str(id_list[location]))
    print("Name: " + name_list[location])
    print("Department: " + dep_list[location])
    print("Salary: " + str(salary_list[location]))


def printAllAccounts(id_list,name_list,dep_list,salary_list):
    print("\nID\tName\tDepartment\tSalary\n--------------------------------------")
    for i in range(len(id_list)):
        print(str(id_list[i]) + "\t" + name_list[i] + "\t  " + dep_list[i] + "\t\t" + str(salary_list[i]))
        

name_list = ["Irem", "Joseph", "Cagla", "Bora"]
id_list = [123, 245, 375, 468]
department_list = ["HR", "IT", "HR", "ACC"]
salary_list = [12000, 15000, 9500, 8000]

menu()
choice = int(input("Enter an operation: "))
while(choice != 5):
    if(choice==1):
        addAccount()
        print("New employee is added successfully!\n")
    elif(choice==2):
        id = int(input("Enter the id of the employee you want to remove: "))
        position = findLocation(id, id_list)
        deleteAccount(position, id_list, name_list, department_list, salary_list)
        print("The employee is deleted successfully!\n")
    elif(choice==3):
       search_id = int(input("Enter the id you want to search for: "))
       pos = findAccount(search_id, id_list)
       if(pos >=0 ):
           searchedAccount(pos, id_list, name_list, department_list, salary_list)
    elif(choice==4):
       printAllAccounts(id_list,name_list,department_list,salary_list)
    else:
        print("Invalid input entered!\nTry again!\n")
        exit(1)
    menu()
    choice = int(input("Enter an operation: "))
        
print("\nBye!\n\n")
      
