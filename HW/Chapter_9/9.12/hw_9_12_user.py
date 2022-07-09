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