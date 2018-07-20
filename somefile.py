<<<<<<< HEAD
class Employee:
    def __init__(self,f_name, s_name, pay):
        self.f_name=f_name
        self.s_name=s_name
        self.pay=pay
        self.email=f_name+'.'+s_name+'@company.com'
        self.fullname=f_name+' '+s_name
    def display(self):
        print(self.fullname+'\n'
              +'pay: '+str(self.pay)+'\n'
              +'email: '+self.email+'\n')



emp_1=Employee('Corey','Lane',15000)
emp_2=Employee('John','Lennon',17000)

emp_1.display()
emp_2.display()
=======
class Employee:
    def __init__(self,f_name, s_name, pay):
        self.f_name=f_name
        self.s_name=s_name
        self.pay=pay
        self.email=f_name+'.'+s_name+'@company.com'
        self.fullname=f_name+' '+s_name
    def display(self):
        print(self.fullname+'\n'
              +'pay: '+str(self.pay)+'\n'
              +'email: '+self.email+'\n')



emp_1=Employee('Corey','Lane',15000)
emp_2=Employee('John','Lennon',17000)

emp_1.display()
emp_2.display()
>>>>>>> c3a581a6142b4afe5141cc94fd60406c12aa70fe
