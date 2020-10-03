# repeats over few lines of code.Be careful with indendations
for i in range(10) :
    print("Hello")


print("A")
print("B")
for i in range(3) :
    print("C")
    print("D")
print("E")

#   range(3), starts with 0 and ends with 2.
for i in range(3):
    print(i)

#    range(1,5) - arguments- starting index, ending index
for i in range(1,5):
    print(i)

#   range(1,10,2)-args- starting index, ending index, incrementer
for i in range(1,10,2):
    print(i)

#   print triangle stars
for i in range(4):
    print('*'*(i+1))
