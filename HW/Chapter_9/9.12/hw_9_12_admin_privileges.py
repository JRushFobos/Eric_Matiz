from hw_9_12_user import User

class Admin(User):
    def __init__(self, fist_name, last_name, age, location):
        super().__init__(fist_name, last_name, age, location)
        self.privileges = Privileges()

    def describe_admin(self):
        print (f'\n{self.fist_name} {self.last_name} {self.age} {self.location}')

    def greet_admin(self):
        print (f'Hello admin {self.fist_name.title()}')

class Privileges():
    def __init__(self):
        self.privileges=['Разрешено добавлять сообщение ', 'Разрешено удалять пользователей','Разрешено банить пользователей', 'Разрешено назначать доступы']
        
    def show_privileges(self):
        print (f'Show admin privileges:')
        for privilege in self.privileges:
            print(privilege)