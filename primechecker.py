n=int(input("Enter the Number: "))
def prime_checker(Number):
    x=0
    for y in range(2,n):
        if n%y==0:
            print("The Number is not prime")
            break
        x=y
    x+=1
    if x==n:
        print("The Number is prime")
prime_checker(Number="n")

def prime_checkers(Number):
    is_true=True
    for i in range(2,n):
        if n%i==0:
            is_true=False
    if is_true:
        print("The number is prime")
    else:
        print("The number is not prime")
prime_checkers(Number="n")