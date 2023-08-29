class Employee:
    def __init__(self, emp_id, name, age, salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.salary = salary
    
    def display(self):
        print(f"Employee ID: {self.emp_id}")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Salary: {self.salary}")
        print("=" * 20)

def search_by_age(employees, age_operator, age_value):
    filtered_employees = []
    for emp in employees:
        if age_operator == '<' and emp.age < age_value:
            filtered_employees.append(emp)
        elif age_operator == '>' and emp.age > age_value:
            filtered_employees.append(emp)
        elif age_operator == '<=' and emp.age <= age_value:
            filtered_employees.append(emp)
        elif age_operator == '>=' and emp.age >= age_value:
            filtered_employees.append(emp)
    return filtered_employees

def search_by_name(employees, name):
    return [emp for emp in employees if name.lower() in emp.name.lower()]

def search_by_salary(employees, salary_operator, salary_value):
    filtered_employees = []
    for emp in employees:
        if salary_operator == '<' and emp.salary < salary_value:
            filtered_employees.append(emp)
        elif salary_operator == '>' and emp.salary > salary_value:
            filtered_employees.append(emp)
        elif salary_operator == '<=' and emp.salary <= salary_value:
            filtered_employees.append(emp)
        elif salary_operator == '>=' and emp.salary >= salary_value:
            filtered_employees.append(emp)
    return filtered_employees

# Sample employee data
employee_data = [
    ("161E90", "Raman", 41, 56000),
    ("161F91", "Himadri", 38, 67500),
    ("161F99", "Jaya", 51, 82100),
    ("171E20", "Tejas", 30, 55000),
    ("171G30", "Ajay", 45, 44000),
]

employees = [Employee(emp_id, name, age, salary) for emp_id, name, age, salary in employee_data]

# User interaction
print("Search Options:")
print("1. Age")
print("2. Name")
print("3. Salary")
search_option = int(input("Enter the search option: "))

if search_option == 1:
    age_operator = input("Enter age operator (<, >, <=, >=): ")
    age_value = int(input("Enter age value: "))
    result = search_by_age(employees, age_operator, age_value)
elif search_option == 2:
    name = input("Enter name: ")
    result = search_by_name(employees, name)
elif search_option == 3:
    salary_operator = input("Enter salary operator (<, >, <=, >=): ")
    salary_value = int(input("Enter salary value: "))
    result = search_by_salary(employees, salary_operator, salary_value)
else:
    print("Invalid search option")
    result = []

if result:
    print("Search Results:")
    for emp in result:
        emp.display()
else:
    print("No results found.")