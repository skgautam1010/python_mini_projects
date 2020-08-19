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
    global logged_user
    user_name=input("Enter your Username : (b: return to main menu) : ")
    if user_name=='b':
        return admin_menu()
    while invalid_name(users,user_name):
        user_name=input("This User name is Taken , Enter a new User Name: ")
    password=getpass("Enter the password: ")
    logged_user=len(users)
    users.append({
        'user_id':len(users),
        'user_name':user_name,
        'pasword':password,
        'Products':[]
    })
    admin_menu()
def add_customer():
    global logged_user
    name=input("Enter Your Name:   ")
    mobile_no=int(input("Enter your Mobile Number: "))
    user_name=input("Enter the Username:(b:return to main menu) :  ")
    if user_name=='b':
        return user_menu()
    while invalid_name(users,user_name):
        user_name=input("This username is taken, Enter a new User Name: ")
    password=getpass("Enter the password: ")
    logged_user=len(users)
    users.append({
        'user_id':len(users),
        'user_name':user_name,
        'password':password,
        'Products':[]
    })
    print("Registration Successfull!!")
    user_menu()


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
        'product_name':product_name+'                ',
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
    admin_menu()
def check_product():
    check_lists(products)
    admin_menu()
def finish():
    print("Thanks For Choosing Us!!")
    quit
def shopping():
    i=0
    print("Product List")
    for product in products:
        print('('+str(i)+')',product['product_name'],'$'+str(product['product_price']),str(product['product_quantity'])+'u')
        i=i+1
    product_number=int(input("Enter the Product number u want to add to cart (-1:return to main menu) : "))
    if product_number==-1:
        return user_menu()
    if product_number in range(0,len(products)):
        users[logged_user]['Products'].append(products[product_number])
        products[product_number]['product_quantity'] -=1
        print("Product added to the cart!!")
    else:
        print("The number choosed doesn't exist in the products list")
        shopping()
    user_menu()


def check_cart():
    try:
        i=0
        sum=0
        for product in users[logged_user]['Products']:
            print('('+str(i)+')',product['product_name'],'\t','$'+str(product['product_price']))
            sum +=product['product_price']
            i +=1
        print('\n\tThe sum is:', '$'+str(sum), end='\n___________________________________________________________\n')
    except:
        print('Your cart is empty', end='\n___________________________________________________________\n')
    user_menu()

def remove_product_from_cart():
    try:
        i=0
        for product in users[logged_user]['Products']:
            print('('+str(i)+')',product['product_name'],'\t','$'+str(product['product_price']))
            i +=1
    except:
        print('You cart is empty', end='\n___________________________________________________________\n')
        return user_menu()
    product_to_remove=int(input("Please enter the product number that u want to remove: "))
    if product_to_remove in range(0,len(users[logged_user]['Products'])):
        answer=input("Are u sure u want to remove"+users[logged_user]['Products'][product_to_remove]['product_name'].strip()+'(y:yes/n:no) : ' ).lower()
        if answer=='y':
            users[logged_user]['Products'][product_to_remove]['product_quantity'] +=1
            del users[logged_user]['Products'][product_to_remove]
            print("The Product is removed from Cart!!!")
        else:
            return user_menu()
    else:
        print("Please Enter the Correct number!! The choosen Product Doesnt Exist in Your Cart!!")
    user_menu()

def admin_menu():
    task_number=input('--------------------------------\n1-->Add a user\n2-->Remove a user\n3-->Add a product\n4-->Remove a product\n5-->check Users\n'
    '6-->Check Products\n7-->Quit\n Please Enter your Response: ')
    while int(task_number) not in range(1,8):
        task_number=input("Incorrect Response\n Please Enter the correct number: ")
    return{
        '1':add_user,
        '2':remove_user,
        '3':add_product,
        '4':remove_product,
        '5':check_user,
        '6':check_product,
        '7':quit,
    }[task_number]()
def user_menu():
    answer=input('-------------------------------\n1-->Shopping\n2-->Check Your Cart\n3-->Remove a product from the cart\n'
    '4-->Finish\n  Please Enter Your Response: ')
    while int(answer) not in range(1,5):
        answer=input('----------------------------\nIncorrect Response\n-------------------------------\n1-->Shopping\n2-->Check Your Cart\n3-->Remove a '
        'product from the cart\n4-->Finish\n  Please Enter Your Response: ')
    return{
        '1':shopping,
        '2':check_cart,
        '3':remove_product_from_cart,
        '4':finish
    }[answer]()

products=[
    {
        'product_id':0,
        'product_name':'Addidas shoes                    ',
        'product_price':100,
        'product_quantity':50
    },
    {
        'product_id':1,
        'product_name':'Nike                              ',
        'product_price':200,
        'product_quantity':30
    },
    {
        'product_id':2,
        'product_name':'Jeans                              ',
        'product_price':200,
        'product_quantity':20
    },
    {
        'product_id':3,
        'product_name':'Kurta                               ',
        'product_price':50,
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
logged_user=None
tries=5
answer=input("1-->Register\n2-->SignIn\n  Please choose a option: ")
while int(answer) not in range(1,3):
    answer=input("1-->Register\n2-->SignIn\n  Please choose a option: ")
if answer=='1':
    add_customer()
elif answer=='2':
    while tries>0:
        user_name=input("Please Enter your User Name : ")
        password=getpass("please Enter your Password: ")
        for user in users:
            if user_name==user['user_name'] and password==user['password']:
                logged_user=user['user_id']
                tries=-1
                break
        if tries !=-1:
            print("The Information Entered is Incorrect!You Have",tries-1,"tries left!!!")
            tries=tries-1
        if tries==0:
            print("You crossed 5 tries")
            quit()
    if user_name=='admin':
        print("Hello Admin!")
        admin_menu()
    else:
        print("\nHello",user_name.capitalize(),"!")
        user_menu()




    
