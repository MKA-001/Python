#Praoblem no.1
Oppinion = str(input("Enter you Opinion Here:"))
x = "Enjoy"
if x in Oppinion:
    print("You have done great")
else:
    print("You can improve")
#Problem no.2
Marks = float(input("Enter average marks here:"))
x = Marks
if x >= 90:
    print("Your grade is 'A+'")
elif 70<= x <90:
    print("Your grade is 'A-'")
elif  50<= x < 70:
    print("Your grade is 'B'")
else:
    print("Your grade is 'Fail'")
#Problem no.3
num = int(input("Enter the numer:"))
x = num%3
y = num%5
if x==0 and y!=0:
    print("Fizz")
elif x!=0 and y==0:
    print("Buzz")
elif x==0 and y==0:
    print("FizzBuzz")
else:
    print("Not a FizzBuzz")
#Problem no.4
Inp1 = float(input("Enter the 1st number:"))
Inp2 = float(input("Enter the 2nd number:"))
Inp3 = input("Enter the operational Symbol:")
i = Inp1
j = Inp2
k = Inp3
if k == "+":
    sum = i + j 
    print("The result is:", sum)
elif k == "-":
    diff = i - j
    print("The result is:", diff)
elif k == "*":
    product = i*j 
    print("The result is:", product)
elif k == "/" and j !=0:
    division = i/j
    print("The result is:", division)
elif k == "/" and j ==0:
    print("Error: Division by Zero is not Allowed")
else:
    print("start again")
