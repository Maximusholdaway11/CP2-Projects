#Max Holdaway, Advanced Functions Notes

#Helper Function below
def check_input_alpha(user_txt):
    try:
        user_txt.isnumeric() == True
    except:
        return True
    else:
        return False

def check_input_integer(user_txt):
    try:
        user_txt.isnumeric() == False
    except:
        return False
    else:
        return True

def hello(name):
    if not check_input_alpha(name):
        print(f"Hello {name}!")
    else:
        print("Please only write letters.")

user_input = input("Please write your name: ")

hello(user_input)
#Inner Function below
def fun1():
    msg = "This is outer function."

    def fun2():
        print(msg)
    fun2()

fun1()
#Closure Function below
def fun(a):
    #Outer function remembers the value of a

    def adder(b):
        return a+b
    return adder #return the closure

val = fun(10) #Call outer function

print(val(5)) #Call inner function
#Closure second example

def end(income):

    def calc(cost, type):
        percent = cost/income * 100
        print(f"Your {type} is ${cost:.2f} and that is {percent:.0f}")
    return calc

def user_input(type):
    return input(f"What is your monthly {type}: \n$")

income = user_input("Income")
rent = user_input("Rent")
utilities = user_input("Utitlites")
transportation = user_input("Transportation")

ready = end(income)

ready = end(rent, "Rent")
ready = end(utilities, "Utilities")
ready = end(transportation, "Transportation")