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
        if age>=5 and age<130:
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


