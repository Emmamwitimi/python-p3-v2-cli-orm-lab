from models.department import Department
from models.employee import Employee


def exit_program():
    print("Goodbye!")
    exit()

# We'll implement the department functions in this lesson


def list_departments():
    departments = Department.get_all()
    for department in departments:
        print(department)


def find_department_by_name():
    name = input("Enter the department's name: ")
    department = Department.find_by_name(name)
    print(department) if department else print(
        f'Department {name} not found')


def find_department_by_id():
    # use a trailing underscore not to override the built-in id function
    id_ = input("Enter the department's id: ")
    department = Department.find_by_id(id_)
    print(department) if department else print(f'Department {id_} not found')


def create_department():
    name = input("Enter the department's name: ")
    location = input("Enter the department's location: ")
    try:
        department = Department.create(name, location)
        print(f'Success: {department}')
    except Exception as exc:
        print("Error creating department: ", exc)


def update_department():
    id_ = input("Enter the department's id: ")
    if department := Department.find_by_id(id_):
        try:
            name = input("Enter the department's new name: ")
            department.name = name
            location = input("Enter the department's new location: ")
            department.location = location

            department.update()
            print(f'Success: {department}')
        except Exception as exc:
            print("Error updating department: ", exc)
    else:
        print(f'Department {id_} not found')


def delete_department():
    id_ = input("Enter the department's id: ")
    if department := Department.find_by_id(id_):
        department.delete()
        print(f'Department {id_} deleted')
    else:
        print(f'Department {id_} not found')


# You'll implement the employee functions in the lab

def list_employees():
    employees=Employee.all()
    for employee in employees:
        print(employee)


def find_employee_by_name():
    name = input("enter the employees name: ")
    employee =Employee.find_by_name(name)
    print(employee) if employee else print(f"Employee {name} not found.")    


def find_employee_by_id():
    id = input("Enter employee id: ")
    employee = Employee.find_by_id(id)
    print(employee) if employee else print(f"employee {id} not found.")
    


def create_employee():
    new_employee =input("enter employees name: ")
    job_title =input("enter employees job title")
    department_id =input("enter department id")
    try:
        employee =Employee.create(name,job_title,department_id)
        print(f"{employee} : success")
    except Exception as exc:
        print("error creating employee", exc)


def update_employee():
    id = input("enter employee id")
    if id in Employee.find_by_id(id):
        try:
            name = input("enter new name")
            Employee.name = name

            job_title = input("enter employees job title")
            Employee.job_title = job_title

            department_id = input("enter the department id")
            Employee.department_id = department_id

            Employee.update()
            print(f"success : {id}")

        except Exception as exc:
            print(f"error updating {id}")

    else:
        print(f"{id} not found")



def delete_employee():
    id = input("enter the Employee id")
    if id in Employee.find_by_id(id):
        Employee.delete()
        print(f"success : Employee {id} deleted")
    else:
        print(f"Employee {id} not found")


def list_department_employees():
    id = input("enter  department_id: ")
    dep_id =Department.find_by_id(id)
    if dep_id in dep_id:
        employees = employees()
        for employee in employees:
            print(f"{employee} /n")

    else:
        print("dep id is not found")