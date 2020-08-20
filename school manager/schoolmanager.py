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
        if age>=5 and age<30:
            self.__age=age
        else:
            print("The age enetered is invalid!!")
    
    def get_email(self):
        return self.__email

    def set_email(self,new_email):
        self.__email=new_email

    def get_password(self):
        return self.__password

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

    def administrator_set_password(self,password):
        if len(password)<6:
            password=getpass("password should contain 6 or more characters!!Enter the new password : ")
        self.__password=password


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
            print(round((self.__maths+self.__informatics+self.__electronics)/3,2))
        else:
            print('Maths: ',self.get_maths())
            print('Informatics: ',self.get_informatics())
            print('Electronics: ',self.get_electronics())
            print('Student doesnt have all the marks!!')
    
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
    

class Administrator(Person):
    number_of_administrators=0
    def __init__(self, f_name, l_name, age, password,grade,speciality, m_name=''):
        super().__init__(f_name, l_name, age, password, m_name)
        self.__grade=grade
        self.__speciality=speciality.upper()
        self.__id='ADM' + '_' + str(self.__grade) + '_' + self.__speciality[0:3] + '_' + str(
            self.number_of_administrators)
        
    def get_id(self):
        return self.__id
    
    def set_id(self):
        self.__id='ADM' + '_' + str(self.__grade) + '_' + self.__speciality[0:3] + '_' + str(
            self.number_of_administrators)
    
    def get_grade(self):
        return self.__grade
    
    def set_grade(self,grade):
        if grade not in range(1,6):
            print('Wrong Grade')
        else:
            self.__grade=grade
            self.set_id()
    
    def get_speciality(self):
        return self.__speciality
    
    def set_speciality(self,speciality):
        if speciality.upper() not in ('STUDENTS','PROFESSORS','ADMINS'):
            print('Wrong Speciality')
        else:
            self.__speciality=speciality.upper()
            self.set_id()

    def get_salary(self):
        basic_salary=3000
        print('The salary of Administrator ',self.get_first_name(),self.get_last_name(),'is: ',end=' ')
        salary=str(round((basic_salary + (self.get_grade() / 100) *
                            (basic_salary)), 2)) + '$'
        return salary
    
    def define(self):
        if self.get_middle_name():
            print('Administrator',self.get_first_name(),self.get_middle_name(),self.get_last_name(),'-his Id is: ',self.__id)
        else:
            print('Administrator',self.get_first_name(),self.get_last_name(),'-Id is: ',self.__id)
    

def student_menu(logged_member:Student):
    print('\n\t1)Change Your Password\n\t2)Check your Marks\n\t3)Check your Average\n\t4)Back to main menu ')
    operation=int(input('Please choose the operation: '))
    while operation not in range(1,5):
        operation = input('Wrong operation! please choose an operation again: ')
    if operation==1:
        logged_member.set_password()
        print("Your New Password is Set")
    elif operation==2:
        print('Maths mark:', logged_member.get_maths(),
              '\nInformatics mark:', logged_member.get_informatics(),
              '\nElectronics mark:', logged_member.get_electronics())
    elif operation==3:
        logged_member.get_average()
    else:
        return main()
    return student_menu(logged_member)

def get_members_list(member_list):
    i=1
    for member in member_list:
        print('('+str(i)+')',member.get_first_name(),member.get_last_name())
        i +=1

def get_member_number(member_list):
    print('Please enter the number of the %s: ' %
          ('student' if member_list == members[0] else
            'professor' if member_list == members[1]else
            'administrator'), end='')
    member_number = int(input()) - 1
    while member_number not in range(0, len(member_list)):
        member_number = int(input('Number out of range! '
                                  'please enter the number again: ')) - 1
    return member_number

def professor_menu(logged_member:Professor):
    print('\n\t1)Change Your Password\n\t2)check students list\n\t3)Set Students marks\n\t4)Get students Marks\n\t5)Back to Main Menu')
    operation=int(input('Please select an operation: '))
    while operation not in range(1,6):
        operation = input('Wrong operation! please select an operation again: ')
    if operation==1:
        logged_member.set_password()
        print("The New Password Is set!!!!")
    elif operation==2:
        get_members_list(members[0])
    elif operation==5:
        main()
    elif operation==3:
        student_number=get_member_number(members[0])
        mark=int(input("Please enter the marks: "))
        while mark not in range(0,21):
            mark=int(input("Marks ranges from (0,20) Out of range!!! Please enter marks again: "))
        {
            'MATHS':members[0][student_number].set_maths,
            'INFORMATICS':members[0][student_number].set_informatics,
            'ELECTRONICS':members[0][student_number].set_electronics
        }[logged_member.get_speciality()](mark)
    else:
        i=1
        if logged_member.get_speciality()=='MATHS':
            for student in members[0]:
                print(str(i) + ')' + student.get_first_name(), student.get_last_name(),
                     '\t\t', student.get_maths())
                i += 1
        elif logged_member.get_speciality() == 'INFORMATICS':
            for student in members[0]:
                print(str(i) + ')' + student.get_first_name(), student.get_last_name(),
                     '\t\t', student.get_informatics())
                i += 1
        elif logged_member.get_speciality()=='ELECTRONICS':
            for student in members[0]:
                print(str(i) + ')' + student.get_first_name(), student.get_last_name(),
                       '\t\t', student.get_electronics())
                i += 1
    return professor_menu(logged_member)

def set_person_data(keyword,person:Person,data):
    if keyword=='first_name':
        person.set_first_name(data)
    elif keyword=='last_name':
        person.set_last_name(data)
    elif keyword=='middle_name':
        person.set_middile_name(data)
    elif keyword=='age':
        person.set_age(int(data))
    elif keyword=='email':
        person.set_email(data)
    elif keyword=='password':
        person.administrator_set_password(data)

def get_members_detail(member_list):
    i=1
    for member in member_list:
        print('('+str(i)+')',end=' ')
        member.define()
        i +=1

def add_members(member_list):
    print('Please enter the data of the %s: ' %
          ('student' if member_list == members[0] else
           'professor' if member_list == members[1] else
           'administrator'))
    if member_list==members[0]:
        member=Student('a','a',7,'a','a','a',11)
        member.set_group_number(int(input("Please enter the group number: ")))
    elif member_list==members[1]:
        member=Professor('a','a',7,'a','a','a',11)
        member.set_teaching_hours(int(input("enter teaching hours: ")))
    else:
        member=Administrator('a','a',7,'a','a','a')
    member.set_first_name(input('First_name: '))
    member.set_last_name(input('Last_name: '))
    member.set_age(int(input('Age: ')))
    member.administrator_set_password(input('Enter password: '))
    member.set_grade(input('Enter grade: ') if member_list == members[0]
                     else int(input('Enter grade: ')))
    member.set_speciality(input('Enter speciality: '))
    member_list.append(member)


def student_administrator_menu(logged_member:Administrator):
    print('Please select an operation:'
          '\n\t1)Change your password'
          '\n\t2)Check students list'
          '\n\t3)Set student first name'
          '\n\t4)Set student last name'
          '\n\t5)Set student middle name'
          '\n\t6)Set student age'
          '\n\t7)Set student email'
          '\n\t8)Set student password'
          '\n\t9)Set student grade'
          '\n\t10)Set student speciality'
          '\n\t11)Set student group number'
          '\n\t12)Get students averages'
          '\n\t13)Get students details'
          '\n\t14)Add a new student'
          '\n\t%s' % '15)Back to the admin menu' if logged_member.get_speciality() == 'ADMINS' else '')
    operation=int(input('> '))
    while operation not in range(1,16):
        operation=int(input("Wrong operation!! Please enter the operation again:> "))
    if operation==1:
        logged_member.set_password()
    elif operation==2:
        get_members_list(members[0])
    elif operation in range(3,9):
        student_number=get_member_number(members[0])
        data=input("Enter the data that u want to set: ")
        set_person_data('first_name' if operation==3 else 'last_name' if operation==4
        else 'middle_name' if operation==5 else 'age' if operation==6 else 'email' if operation==7 else 'password' ,members[0][student_number],data)
    elif operation in range(9,12):
        student_number=get_member_number(members[0])
        data=input('Enter the data that u want to set: ')
        {
            '9':members[0][student_number].set_grade,
            '10':members[0][student_number].set_speciality,
            '11':members[0][student_number].set_group_number
        }[operation](int(data) if operation=='11' else data)
    elif operation==12:
        student_number=get_member_number(members[0])
        print(members[0][student_number].get_average())
    elif operation==13:
        get_members_detail(members[0])
    elif operation==14:
        add_members(members[0])
    else:
        if logged_member.get_speciality()=='ADMINS':
            admins_menu(logged_member)
        else:
            print("Wrong operation !! ")
    return student_administrator_menu(logged_member)

def professor_administrator_menu(logged_member:Administrator):
    print('Please select an operation:'
          '\n\t1)Change your password'
          '\n\t2)Check professors list'
          '\n\t3)Change professor first name'
          '\n\t4)Change professor last name'
          '\n\t5)Change professor middle name'
          '\n\t6)Change professor age'
          '\n\t7)Change professor email'
          '\n\t8)Change professor password'
          '\n\t9)Change professor grade'
          '\n\t10)Change professor speciality'
          '\n\t11)Change professor teaching hours'
          '\n\t12)Check professor salary'
          '\n\t13)Check professors details'
          '\n\t14)Add a new professor'
          '\n\t%s' % '15)Back to the admin menu'
          if logged_member.get_speciality() == 'ADMINS' else '')
    operation = int(input('> '))
    while operation not in range(1,16):
        operation=int(input("Incorrect Response!! Please choose a operation again: "))
    if operation==1:
        logged_member.set_password()
    elif operation==2:
        get_members_list(members[1])
    elif operation in range(3,9):
        professor_number=get_member_number(members[1])
        data = input('Please enter the data that you want to set: ')
        set_person_data('first_name' if operation == 3
                        else 'last_name' if operation == 4
                        else 'middle_name' if operation == 5
                        else 'age' if operation == 6
                        else 'email' if operation == 7
                        else 'password', members[1][professor_number],
                        data)
    elif operation in range(9, 12):
        professor_number = get_member_number(members[1])
        data = input('Please enter the data that you want to set: ')
        {
            9: members[1][professor_number].set_grade,
            10: members[1][professor_number].set_speciality,
            11: members[1][professor_number].set_teaching_hours,
        }[operation](data if operation == 10 else int(data))
    elif operation==12:
        professor_number=get_member_number(members[1])
        print(members[1][professor_number].get_salary())
    elif operation==13:
        get_members_detail(members[1])
    elif operation == 14:
        add_member(members[1])
    else:
        if logged_member.get_speciality() == 'ADMINS':
            admins_menu(logged_member)
        else:
            print('Wrong operation! please enter an operation again: ')
    return professor_administrator_menu(logged_member)

def admins_menu(logged_member:Administrator):
    print('Please select what you want to manage:'
          '\n\t1)Manage Administrators'
          '\n\t2)Manage Professors'
          '\n\t3)Manage Students\n\t4)Back to Main menu')
    manage=int(input('> '))
    while manage not in range(1,5):
        manage=int(input("Incorrect Input!! Please select what u want to manage again: "))
    def administrator_administrator_menu(logged_member: Administrator):
        print('Please select an operation:'
              '\n\t1)Change your password'
              '\n\t2)Check administrators list'
              '\n\t3)Change administrator first name'
              '\n\t4)Change administrator last name'
              '\n\t5)Change administrator middle name'
              '\n\t6)Change administrator age'
              '\n\t7)Change administrator email'
              '\n\t8)Change administrator password'
              '\n\t9)Change administrator grade'
              '\n\t10)Change administrator speciality'
              '\n\t11)Check administrator salary'
              '\n\t12)Check administrators details'
              '\n\t13)Add a new administrator'
              '\n\t%s' % '14)Back to the admin menu' if logged_member.get_speciality() == 'ADMINS'
              else '')
        operation = int(input('> '))
        while operation not in range(1, 15):
            operation = int(input('Wrong operation! please enter an operation again: '))
        if operation == 1:
            logged_member.set_password()
        elif operation == 2:
            get_members_list(members[2])
        elif operation in range(3, 9):
            administrator_number = get_member_number(members[2])
            data = input('Please enter the data that you want to set: ')
            set_person_data('first_name' if operation == 3
                            else 'last_name' if operation == 4
                            else 'middle_name' if operation == 5
                            else 'age' if operation == 6
                            else 'email' if operation == 7
                            else 'password', members[2][administrator_number],
                                            data)
        elif operation in range(9, 11):
            administrator_number = get_member_number(members[2])
            data = input('Please enter the data that you want to set: ')
            {
                9: members[2][administrator_number].set_grade,
                10: members[2][administrator_number].set_speciality,
            }[operation](data if operation == 10 else int(data))
        elif operation == 11:
            administrator_number = get_member_number(members[2])
            print(members[2][administrator_number].get_salary())
        elif operation == 12:
            get_members_details(members[2])
        elif operation == 13:
            add_member(members[2])
        else:
            if logged_member.get_speciality() == 'ADMINS':
                admins_menu(logged_member)
            else:
                print('Wrong operation! please enter an operation again: ')
        return administrator_administrator_menu(logged_member)
    '''{
        1:administrator_administrator_menu,
        2:professor_administrator_menu,
        3:student_administrator_menu,
    }[manage](logged_member)'''
    if manage==1:
        administrator_administrator_menu(logged_member)
    elif manage==2:
        professor_administrator_menu(logged_member)
    elif manage==3:
        student_administrator_menu(logged_member)
    else:
        main()
    


members=[[Student('sonu','gautam',24,'sonu1234','FIRST','PYTHON',15,'Kumar')] ,
            [Professor('Abc','xyz',44,'abc1234','4','MATHS',18)],
            [Administrator('sk','gautam',23,'admin1234','5','admins')]]

def main():
    print("\t\t***********WELCOME TO OUR SCHOOL MANAGEMENT SYSTEM************\n\n1)Student\n2)Professor\n3)Administrator\n4)Exit ")
    profession=int(input("\tPlease Choose Your Profession: "))-1
    while profession+1 not in range(1,5):
        profession=int(input("Wrong choice!! Please choose your profession again:  "))
    if profession==3:
        exit()
    logged_member=None
    while not logged_member:
        email=input("please enter your email address: ")
        for member in members[profession]:
            if member.get_email()==email:
                password=getpass('please enter your password: ')
                for i in range(4):
                    if password==member.get_password():
                        print("Hello ",member.get_first_name(),member.get_last_name())
                        logged_member=member
                        break
                    else:
                        password=getpass("password incorrect!!!Please enter a valid password:  ")
                break
        if not logged_member:
            print("Incorrect Information!!!")
    if profession==0:
        student_menu(logged_member)
    elif profession==1:
        professor_menu(logged_member)
    else:
        if logged_member.get_speciality()=='STUDENTS':
            student_administrator_menu(logged_member)
        elif logged_member.get_speciality()=='PROFESSORS':
            professor_administrator_menu(logged_member)
        elif logged_member.get_speciality()=='ADMINS':
            admins_menu(logged_member)
        else:
            print("Administrator With A Wrong speciality!!!")
            

if __name__=='__main__':
    main()
