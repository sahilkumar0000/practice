# # Question 1
# num=8
# for x in range(1,11):
#     # x1=num*x
#     # print(str(num) +" X "+str(x) + " = " + str(x1))        1st method
#     print(f"{num} X {x} = {num*x}")                          2nd method

# # Question 2
# l1=["harry","sohan","sachin","rahul"]

# for x in l1:
#     if x.startswith('s'):
#         print(f"Hello Mr.{x}")

# Question 3


# num=8
# x=1
# while x<=10:
#     print(f"{num} X {x} = {num*x}")
#     x+=1

# # Question 4
# num=int(input("Enter the Number: "))
# prime= True

# for x in range(2,num):
#     if num%x==0:
#         prime=False
#         break       
# if prime:
#     print("The number is prime")
# else:
#     print("the number isnt prime")


# # Question 5
# n=int(input("Enter the value of n: "))
# x=1
# sum=0
# while x<=n:
#     sum+=x
#     x+=1
# print(sum)


# Question 6
# n =int(input("Enter the Number: "))
# factorial=1
# for x in range(1,n+1):
#     factorial*=x

# print(factorial)

# Question 8

# for i in range(4):
#     print("*"*(i+1))

# Question 7
# n=3
# for i in range(3):
#     print(" "*(n-i-1),end="")
#     print("*"*(n-i-1),end="")
#     print(" "*(n-i-1),end="")


# Quuestion 9
# rows=3

# for i in range(rows):
#     for j in range(rows):
#         if j==1 and i==1:
#             print(" ",end="")
#         else:
#             print("*",end="")
#     print("")

# Question 10
# n= int(input("Enter the value of: "))
# for i in range(1,11):
#     print(f"{n} X {i} = {n*i}")