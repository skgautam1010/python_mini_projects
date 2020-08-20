from getpass import getpass

class Person:
    def __init__(self,f_name,l_name,age,password,m_name):
        self.__f_name=f_name.title()
        self.__l_name=l_name.title()
        self.__age=age
        self.__email=(self.get_first_name()[0]+self.get_last_name()+'@gmail.com').lower()
        self.__password=password
    @staticmethod
    def string_has_number(string):
        return any(char.isdigit() for char in string)
  
    def get_first_name(self):
        return self.__f_name
  
    def get_last_name(self):
        return self.__l_name
  
    def set_first_name(self,f_name):
        if self.string_has_number(f_name):
            print("Your entered First name contains number!!")
        else:
            self.__f_name=f_name.title()
  
    def set_last_name(self,l_name):
        if self.string_has_number(l_name):
            print("Your entered last name contains number!!")
        else:
            self.__l_name=l_name.title()
  
    def get_middile_name(self):
        return self.__m_name
  
    def set_middile_name(self,m_name):
        if self.string_has_number(m_name):
            print("Your entered middile name contains a number!!")
        else:
            self.__m_name=m_name.title()
  
    def get_age(self):
        return self.__age
  
    def set_age(self,age):
        if age>=5 and age<20:
            self.__age=age
        else:
            print("The age enetered is invalid!!")
    
    def get_email(self):
        return self.__email

    def set_email(self,new_email):
        self.__email=new_email

    def get_password(self):
        return self.__password

    def administrator_set_password(self,password):
        if len(password)<6:
            new_password=getpass("password should contain 6 or more characters!!Enter the new password : ")
        self.__password=new_password

    def set_password(self):
        old_password=getpass("please enter your password: ")
        for tries in range(4):
            if old_password!=self.__password:
                old_password=getpass("Wrong password!!Enter the password agin:  ")
            else:
                break
            if tries==3:
                print("\nYou had 5 tries!! Logging Out!!")
                return exit()
        new_password=getpass("Please enter the new password: ")
        while len(password)<6:
            new_password=getpass("password should contain 6 or more characters!!\n  please enter a new password: ")
        self.__password=new_password


class Student(Person):
    number_of_students=0
    def __init__(self, f_name, l_name, age, password,grade,speciality,group_number,m_name=''):
        super().__init__(f_name, l_name, age, password, m_name)
        self.__grade=grade.upper()
        self.__speciality=speciality.upper()
        self.__group_number=group_number
        self.__id='STD'+'_'+self.__grade[0:3]+'_'+self.__speciality[0:3]+'_'+\
                    str(self.__group_number)+'_'+str(self.number_of_students)
        self.__maths=None
        self.__informatics=None
        self.__electronics=None
    
    def get_id(self):
        return self.__id
    
    def set_id(self):
        self.__id='STD'+'_'+self.__grade[0:3]+'_'+self.__speciality[0:3]+'_'+\
            str(self.__group_number)+'_'+str(self.number_of_students)
    
    def get_grade(self):
        return self.__grade
    
    def set_grade(self,grade):
        if grade.upper() not in ('FIRST','SECOND','THIRD','FOURTH','FIFTH'):
            print('Wrong Grade!!')
        else:
            self.__grade=grade.upper()
            self.set_id()
    
    def get_speciality(self):
        return self.__speciality
    
    def set_speciality(self,speciality):
        if speciality.upper() not in ('PYTHON','JAVA','C++'):
            print("Wrong Speciality!!")
        else:
            self.__speciality=speciality.upper()
            self.set_id()
    
    def get_group_number(self):
        return self.__group_number

    def set_group_number(self,group_number):
        if group_number not in range(1,30):
            print("Group Number out of range!!")
        else:
            self.__group_number=group_number
            self.set_id()

    def get_maths(self):
        return self.__maths
    
    def set_maths(self,maths):
        if maths>=0 and maths<=20:
            self.__maths=maths
        else:
            return 'Marks out of range!!'
    
    def get_informatics(self):
        return self.__informatics
    
    def set_informatics(self,informatics):
        if informatics>=0 and informatics<=20:
            self.__informatics=informatics
        else:
            return 'Marks Out of range'

    def get_electronics(self):
        return self.__informatics

    def set_electronics(self,electronics):
        if electronics>=0 and electronics<=20:
            self.__electronics=electronics
        else:
            return 'Marks Out of range!!'

    def get_average(self):
        if self.__maths and self.__informatics and self.__electronics:
            print(self.get_first_name(),self.get_last_name(),end=': ')
            return round((self.__maths+self.__informatics+self.__electronics)/3,2)
        else:
            print('Maths: ',self.get_maths())
            print('Informatics: ',self.get_informatics())
            print('Electronics: ',self.get_electronics())
            return 'Student doesnt have all the marks!!'
    
    def define(self):
        if self.get_middile_name():
            print('Student: ',self.get_first_name(),self.get_middile_name(),self.get_last_name(),'-his Id is: ',self.__id)
        else:
            print('Student',self.get_first_name(),self.get_last_name(),'-his Id is: ',self.__id)
    

class Professor(Person):
    number_of_professors=0
    def __init__(self, f_name, l_name, age, password,grade,speciality,teaching_hours, m_name=''):
        super().__init__(f_name, l_name, age, password, m_name)
        self.__grade=grade
        self.__speciality=speciality.upper()
        self.__teaching_hours=teaching_hours
        self.__id='PRO'+'_' + str(self.__grade) + '_' + self.__speciality \
                    + '_' + str(self.number_of_professors)
    
    def get_id(self):
        return self.__id
    
    def set_id(self):
        self.__id='PRO'+'_' + str(self.__grade) + '_' + self.__speciality \
                    + '_' + str(self.number_of_professors)
    
    def get_grade(self):
        return self.__grade

    def set_grade(self,grade):
        if grade not in range(1,6):
            print("Wrong Grade!!")
        else:
            self.__grade=grade
            self.set_id()
    def get_speciality(self):
        return self.__speciality
    
    def set_speciality(self,speciality):
        if speciality not in ('MATHS','INFORMATICS','ELECTRONICS'):
            print('Wrong Speciality!!')
        else:
            self.__speciality=speciality
            self.set_id()
    
    def get_teaching_hours(self):
        return self.__teaching_hours
    
    def set_teaching_hours(self,teaching_hours):
        if teaching_hours>=5 and teaching_hours<=25:
            self.__teaching_hours=teaching_hours
        else:
            print("Teaching Hours out of range!!")
    
    def get_salary(self):
        basic_salary=2000
        print('The salary of professor ',self.get_first_name(),self.get_last_name(),'is: ',end=' ')
        salary=str(round((basic_salary + (self.get_grade() / 100) * (basic_salary) +
                            self.__teaching_hours * 20), 2)) + '$'
        return salary
    
    def define(self):
        if self.get_middile_name():
            print('Professor',self.get_first_name(),self.get_middile_name(),self.get_last_name(),'-his Id is: ',self.__id)
        else:
            print('Professor',self.get_first_name(),self.get_last_name(),'-his id is: ',self.__id)
    

