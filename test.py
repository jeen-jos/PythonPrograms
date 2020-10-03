# Follwoing code shows how to print
msg = "Hello world"
print(msg)
print(msg.capitalize())
print(msg.split())

# Taking inputs from user
name = input("enter your name : ")
print("Hello ",name)

# eval() converts entered text into number to evaluate expressions
num= eval(input("Enter the number : "))
print(" The value is ",num*num)

print("the value of 3+4 is ",3+4)
print("5+6 is ",5+6," and 4+7 is ",4+7)

#Optional Arguments of print()
#-------------------------------------
#sep - python insets space between arguments of print()
print("the value of 3+4 is ",3+4,".",sep=' ')

#end - keeps python print() from advancing automatically to next line
print("hello friends",end=' ')
print("Have a great day")
