#syntax for for loop is for var_name in(keyword)
# method-> range(start,end,increment/dece) next line body
#for i in range(0,20,2):
 #   print(i)

# while loop
#i=0
#while i<=20:
 #   print(i)
  #  i+=2
#taking input using while condition
while True:
    username=input("Enter your username: ")
    if username=="Uzair":
        print("Welcome", username)
        break
    else:
        print("Wrong username")

while False:
    print("Hello")