from hw_9_12_user import User
from hw_9_12_admin_privileges import Privileges, Admin

admin = Admin('Tor','Odinson',1500,'Asgard')
admin.describe_admin()
admin.greet_admin()
admin.privileges.show_privileges()