print("Welcome to the tip calculator")
a=input("What was the total bill? $")
b=input("What percentage tip would you like to give? 10,12 or 15? ")
c=input("How many people are splitting the bill? ")
d=(float(a)*float(b))/100
f=(float(a)+float(d))/int(c)
splitting=f"Each person to pay: ${round(f,2)}"
print(splitting)
