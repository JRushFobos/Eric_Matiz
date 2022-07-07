class User():
    def __init__(self,fist_name,last_name,age,location):
        self.fist_name = fist_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.login_attempts = 0

    def describe_user(self):
        print (self.fist_name, self.last_name,self.age,self.location)

    def greet_user(self):
        print (f'Hello {self.fist_name.title()}')

    '''increment login'''
    def increnent_login_attempts(self):
        self.login_attempts +=1
        print (f'The number of login attempts is: {self.login_attempts}')

    '''reset login'''
    def reset_login_attempts(self):
        self.login_attempts = 0
        print ('Number of login attempts reset')

user = User('John', 'Fobos', 25, 'Russia')
user.describe_user()
user.greet_user()
user.increnent_login_attempts()
user.increnent_login_attempts()
user.reset_login_attempts()
