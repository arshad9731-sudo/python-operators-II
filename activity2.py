# program to check the application of logical not operator

a = 10
b = 12
c = 12
 # not is used to reverse the result of (a==b)
print(not (a == b))

 # not is used to reverse the result of (b==c)
print(not (b == c))

a = "python"
b = "coding"
 
 #not is used here to check if a is not equal to b
if not (a == b):
    print("a, 'and', b, are different") 


a = 4
b = 5
 
    #not is used here to reverse the result of comparing both coditions
if not ((a == 1) == (b == 5)):
    print("hello")

a = int(input("enter a number: "))

# not is used here to check that hte number is not even
if not (a % 2 == 0):
    print("the number is odd")
else:
    print("the number is even")