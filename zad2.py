class Employee():
    def __init__(self, i_num, fname, lname, work_experience, education_level, salary, age):
        self.i_num = i_num
        self.fname = fname
        self.lname = lname
        self.work_experience = work_experience
        self.education_level = education_level
        self.salary = salary
        self.age = age

    def display_info(self):
        return f"{self.i_num}, {self.fname}, {self.lname}, {self.work_experience}, {self.education_level}, {self.salary}, {self.age}"

    def bonus(self):        
        if work_experience == "high":
            new_salary = self.salary + 0.05*self.salary            
        elif work_experience == "mid":
            new_salary = self.salary + 0.02*self.salary
        else:
            new_salary = self.salary # приравняваме

        for i in range(0, self.work_experience):
            new_salary = new_salary + 0.012*new_salary

        self.salary = new_salary

# край на клас


def sort_employee(employee_list):
    employee_list.sort(key=lambda x: x.age)
    # убеден съм, че анон ламбда на твоя изпит няма да има.
    for employee in employee_list:
        print(employee.display_info())

def search_by_name(employee_list, fname, lname):
    flag = True
    for empl in employee_list:
        if empl.fname == fname and empl.lname == lname:
           print(empl.display_info())
           flag = False
    if flag:
        print("Not found!!!")   

def print_by_educ_exp(employee1, education, experience):
    new_list = []

    for empl in employee_list:
        if empl.education_level == education and empl.work_experience == experience:
            new_list.append(empl)

    for empl in new_list:
        print(empl.display_info())

def remove_employee(employee_list, i_num):
    flag = True
    for i in range(0, len(employee_list), 1):
        if employee_list[i] == i_num:
            employee_list.pop(i)
            print("Information deleted!")
            flag = False
    if flag:
        print("Wrong i_num maina !")        


            




employee_list = []

i_num = int(input())
fname = input()
lname = input()
work_experience = int(input())
education_level = input()
salary = int(input())
age = int(input())

employee1 = Employee(i_num,fname,lname,work_experience,education_level,salary,age)

employee_list.append(employee1)




