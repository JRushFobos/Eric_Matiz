from hw_9_11 import User, Privileges, Admin

admin = Admin('Tor','Odinson',1500,'Asgard')
admin.describe_admin()
admin.greet_admin()
admin.privileges.show_privileges()