def addition(a,b):
    c=a+b
    return c
def substraction(a,b):
    d=a-b
    return d
def multiply(a,b):
    e=a*b
    return e
def divisible(a,b):
    f=a/b
    return f
def main():
    if symbol == "+":
        print(addition(a,b))
    elif symbol == "-":
        print(substraction(a,b))
    elif symbol == "*":
        print(multiply(a,b))
    elif symbol == "/":
        print(divisible(a,b))
a=int(input("enter the number:"))
b=int(input("enter the number:"))
symbol=input("enter the symbol:")
main()
    