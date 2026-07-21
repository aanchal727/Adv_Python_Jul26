class Employee:
    def __init__(self, emp_id, name):
        self.emp_id=emp_id
        self.name=name

    def calculate_salary(self):
        pass

class FullTimeEmployee(Employee):
    def __init__(self, emp_id, name, monthly_salary):
        super().__init__(emp_id, name)

        self.monthly_salary=monthly_salary
    def calculate_salary(self):
        return self.monthly_salary

class PartTimeEmployee(Employee):
    def __init__(self, emp_id, name, hours_worked, hourly_rate):
        super().__init__(emp_id, name)
        self.hours_worked=hours_worked
        self.hourly_rate=hourly_rate

    def calculate_salary(self):
        return self.hours_worked*self.hourly_rate

class ContractEmployee(Employee):
    def __init__(self, emp_id, name, project_amount, bonus):
        super().__init__(emp_id, name)
        self.project_amount=project_amount
        self.bonus=bonus

    def calculate_salary(self):
        return self.project_amount+self.bonus

class Payroll:
    def __init__(self):
        self.emp_list=[]

    def add_employee(self, employee):
        self.emp_list.append(employee)
        
    def generate_payroll(self):
        total_salary=0

        for emp in self.emp_list:
            salary = emp.calculate_salary()
            print("Employee ID :",emp.emp_id)
            print("Name :",emp.name)
            print("Salary :₹" +str(salary))
            print()
            total_salary+=salary
        print("Total Payroll=₹"+str(total_salary))

# Create Employees
emp1=FullTimeEmployee("1","Anand",65000)
emp2=PartTimeEmployee("2","Iksha",120,150)
emp3=ContractEmployee("3","Chinmai",45000,5000)

# Create Payroll
payroll=Payroll()

# Adding the Employees
payroll.add_employee(emp1)
payroll.add_employee(emp2)
payroll.add_employee(emp3)

# Generate Payroll
payroll.generate_payroll()