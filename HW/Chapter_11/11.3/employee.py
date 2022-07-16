class Employee ():
    '''Класс сотрудник! Имя, фамилия текущая ЗП'''
    def __init__(self,first_name,last_name,current_salary):
        self.first_name = first_name
        self.last_name = last_name
        self.current_salary = current_salary

    '''принт фио и зп'''
    def discribe_employee(self):
        print(f'Name {self.first_name}, last name {self.last_name} and current salary {self.current_salary}')

    '''Прибавка к ЗП'''
    def get_raise(self,salary_up=5000):
        self.current_salary += salary_up
        print(self.current_salary)

new_employee = Employee ('John','Fobos',100_000)

new_employee.discribe_employee()

new_employee.get_raise(10_000)
