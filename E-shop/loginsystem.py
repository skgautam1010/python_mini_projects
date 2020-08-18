#login system
from getpass import getpass
def invalid_name(list,element):
    for dic in list:
        try:
            if (dic['user_name']==element):
                return True
        except:
            if(dic['product_name']==element):
                return True
    return False

def add_user():
    user_name=input("Enter your Username : (b: return to main menu) : ")
    if user_name=='b':
        return admin_menu()
    while invalid_name(users,user_name):
        user_name=input("This User name is Taken , Enter a new User Name: ")
    password=getpass("Enter the password: ")
    users.append({
        'user_name':user_name,
        'pasword':password,
        'Products':[]
    })

def admin_menu():
    task_number=input('1-->Add a user\n2-->Remove a user\n3-->Add a product\n4-->Remove a product\n5-->check Users\n6-->Check Products\n7-->Quit\nPlease Enter your Response:')
    while int(task_number) not in range(1,8):
        task_number=input("Incorrect Number\n Please Enter the correct number: ")
    return{
        '1':add_user,
        '2':remove_user,
        '3':add_product,
        '4':remove_product,
        '5':check_user,
        '6':check_product,
        '7':quit,
    }[task_number]()
products=[
    {
        'products_name':'Addidas shoes',
        'product_price':100,
        'product_quantity':50
    },
    {
        'product_name':'Nike',
        'product_price':200,
        'product_quantity':30
    },
    {
        'product_name':'Jeans',
        'product_price':2000,
        'product_quantity':20
    },
    {
        'product_name':'Kurta',
        'product_price':500,
        'product_quantity':10
    }
]
users=[
    {
        'user_name':'admin',
        'password':'admin1234'
    },
    {
        'user_name':'sonu',
        'password':'sonu1234',
        'Products' :[products[0],products[3]]
    },
    {
        'user_name':'sanu',
        'password':'sanu1234',
        'Products':[products[1],products[2]]
    }
]
tries=5
while tries>0:
    user_name=input("Please Enter your User Name : ")
    password=getpass("please Enter your Password: ")
    for user in users:
        if user_name==user['user_name'] and password==user['password']:
            print("Hello",user_name,"!")
            admin_menu()
            tries=-1
    if tries !=-1:
        print("The Information Entered is Incorrect!You Have",tries-1,"times left...")
        tries=tries-1

    
