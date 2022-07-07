class User():
    def __init__(self,fist_name,last_name,age,location):
        self.fist_name = fist_name
        self.last_name = last_name
        self.age = age
        self.location = location

    def describe_user(self):
        print (self.fist_name, self.last_name,self.age,self.location)

    def greet_user(self):
        print (f'Hello  {self.fist_name.title()}')

class Admin(User):
    def __init__(self, fist_name, last_name, age, location):
        super().__init__(fist_name, last_name, age, location)
        self.privileges = []

    def show_privileges(self,*privileges):
        print (f'Show admin privileges:')
        for privilege in privileges:
            print(privilege)

user = User('John', 'Fobos', 25, 'Russia')
user.describe_user()
user.greet_user()
admin = Admin('Luna', 'Kai', 40, 'Russia')
admin.show_privileges('Разрешено добавлять сообщение ', 'Разрешено удалять пользователей','Разрешено банить пользователей', 'Разрешено назначать доступы')