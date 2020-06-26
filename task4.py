from colorama import init
from colorama import Fore, Back, Style
init()

print(Back.GREEN)
print(Fore.BLACK)


def add(x,y):
    return x + y

def subtract(x,y):
    return x - y

def multiply(x,y):
    return x * y

def division(x,y):
    if y ==0:
        return "На ноль делить нельзя!"
    else:
        return x / y 

# x = int(input("Введите 1-число: "))

# operation = input("Введите оператор: ")
# operation = operation.strip()

# y = int(input("Введите 2-число: "))

active = True 
while active:
    oper = input("\nВведите выражение через пробелы: ")

    if oper == "quit":
        break
    
    oper = oper.split()
    
    x = int(oper[0])
    y = int(oper[-1])

    operation = oper[1].strip()


    if operation =="+":
        print(add(x,y))

    elif operation=="-":
        print(subtract(x,y))

    elif operation=="*":
        print(multiply(x,y))

    elif operation=="/":
        print(division(x,y))

    else: 
        print("Ввыражение не правильно!")