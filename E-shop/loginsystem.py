#login system
from getpass import getpass

def print_elements_name(list):
    for dic in list:
        try:
            print("\t"+dic['user_name'])
        except:
            print("\t"+dic['product_name'])
def invalid_name(list,element):
    global name_dic
    for dic in list:
        try:
            if (dic['user_name']==element):
                return True
        except:
            if(dic['product_name']==element):
                name_dic=dic
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
        'user_id':len(users),
        'user_name':user_name,
        'pasword':password,
        'Products':[]
    })
    admin_menu()
def remove_user():
    print("This is User List: ")
    print_elements_name(users)
    user_name=input("Enter the user_name to be removed: (b: return to main menu) : ")
    if(user_name=='b'):
        return admin_menu()
    remove_id=None
    for user in users:
        if user['user_name']==user_name:
            remove_id=user['user_id']
            print(user)
            break
    if remove_id is None:
        print("No such username exist")
    else:
        answer=input("Are u sure u want to delete "+str(user_name)+" (y:Yes|n:No) ").lower()
        if answer =='y':
            del users[remove_id]
    admin_menu()

def add_product():
    product_name=input("Enter the product name: (b: return to main menu) :  ")
    if product_name=='b':
        return admin_menu()
    if invalid_name(products,product_name):
        answer=input("This Product already exist,Enter another product or" 
        "Increment Quantity: (i:increment quantity/c:add another product): ").lower()
        if answer=='c':
            return add_product()
        elif answer=='i':
            new_quantity=int(input("Enter the new quantity: "))
            name_dic['product_quantity'] +=new_quantity
            return admin_menu()
        else:
            print("Wrong Response!")
            return add_product()
    product_price=int(input("Enter the Product Price: "))
    product_quantity=int(input("Enter the product Quantity: "))
    products.append({
        'product_id':len(products),
        'product_name':product_name,
        'product_price':product_price,
        'product_quantity':product_quantity
    })
    admin_menu() 
def remove_product():
    print("This is Product List: ")
    print_elements_name(products)
    product_name=input("Enter the product to be removed: (b:return to main menu ) : ")
    if(product_name=='b'):
        return admin_menu()
    remove_id=None
    for product in products:
        if product['product_name']==product_name:
            remove_id=product['product_id']
            print(product)
            break
    if remove_id is None:
        print("There is no such Product: ")
    else:
        answer=input("Do you Really want to delete this product?: (y:yes/n:no): ").lower()
        if answer=='y':
            del products[remove_id]
    admin_menu()
def check_lists(list):
    i=1
    for dic in list:
        print('('+str(i)+')',dic)
        i +=1
def check_user():
    check_lists(users)
    answer=input("  (b: return to main menu): ")
    if answer=='b':
        return admin_menu()
def check_product():
    check_lists(products)
    answer=input("  (b:return to main menu) : ")
    if answer=='b':
        return admin_menu()

def admin_menu():
    task_number=input('1-->Add a user\n2-->Remove a user\n3-->Add a product\n4-->Remove a product\n5-->check Users\n'
    '6-->Check Products\n7-->Quit\n Please Enter your Response: ')
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
        'product_id':0,
        'product_name':'Addidas shoes',
        'product_price':100,
        'product_quantity':50
    },
    {
        'product_id':1,
        'product_name':'Nike',
        'product_price':200,
        'product_quantity':30
    },
    {
        'product_id':2,
        'product_name':'Jeans',
        'product_price':2000,
        'product_quantity':20
    },
    {
        'product_id':3,
        'product_name':'Kurta',
        'product_price':500,
        'product_quantity':10
    }
]
users=[
    {
        'user_id':0,
        'user_name':'admin',
        'password':'admin1234'
    },
    {
        'user_id':1,
        'user_name':'sonu',
        'password':'sonu1234',
        'Products' :[products[0],products[3]]
    },
    {
        'user_id':2,
        'user_name':'sanu',
        'password':'sanu1234',
        'Products':[products[1],products[2]]
    }
]
name_dic=None
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

    
