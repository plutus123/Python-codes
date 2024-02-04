import os
def add(n1,n2):
    return n1+n2
def sub(n1,n2):
    return n1-n2
def mul(n1,n2):
    return n1*n2
def div(n1,n2):
    return n1/n2
operations ={
    "+":add,
    "-":sub,
    "*":mul,
    "/":div
}
def fun():
    a=float(input("What's the first number?: "))
    is_true=True
    while is_true:
        for key in operations:
            print(key)
        b=input("Pick an operation: ")
        c=float(input("What's the next number?: "))
        calculation_fun=operations[b]
        answer=calculation_fun(a,c)
        print(f"{a} {b} {c} = {answer}")
        k=input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation ")
        if k=='y':
            a=answer
            os.system('cls')
        elif k=='n':
            is_true=False
            fun()
fun()