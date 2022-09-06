
# Question 1
# a=int(input("Enter The First Number: "))
# b=int(input("Enter The Second Number: "))
# c=int(input("Enter The Third Number: "))
# d=int(input("Enter The Fourth Number: "))

# if a>b and a>c and a>d:
#     print("A is the Greatest Number")
# elif b>c and b>d:
#     print("B is the Greatest Number")      first algo
# elif c>d:
#     print("C is the Greatest Number")
# else:
#     print("D is the Greatest Number")

# if a>b:
#     f1=a
# else:
#     f1=b
# if c>d:
#     f2=c
# else:                                       second
#     f2=d
# if f1>f2:
#     print(str(f1) + " is Greatest")
# else:
#     print(str(f2) + " is Greatest")

#Question 2    

# a=int(input("Marks in Maths: "))
# b=int(input("Marks in Hindi: "))
# c=int(input("Marks in Science: "))
# percent=(a+b+c)/3

# if percent<40:
#     print("you are Fail")
# elif a<33 or b<33 or c<33:
#     print("you are Fail")
# else:
#     print("you are pass")

# Question 3

# comment=input("Enter your Comment: ")
# if "make a lot of money" in comment:
#     spam=True
# elif "buy now"in comment:
#     spam= True
# elif "subscribe this" in comment:
#     spam =True
# elif "click this" in comment:
#     spam=True                                    1st method
# else:
#     spam=False

# if spam:
#     print("Your text is Spam")
# else:
#     print("Thanks For Your Valuable Comment")


# spam=["click this","subscribe this","buy now","make a lot of money"]
# comment=input("Enter your comment: ")
# if comment in spam:
#     print("Your Comment is Spam")
# else:
#     print("Thanks for your comment")

# Question 4
# a=input("Enter your Name: ")
# if len(a)>10:
#     print("Your Name contains more then 10 Characters")
# else:
#     print("Great Name sir!!")

# Question 5
# a=["sahil", "shubham","sheetal","sumit","mohit"]
# name=input("Enter your Name:")
# if name in a:
#     print("Your Name is already in the List")
# else:
#     print("Your Name is not present in the List")

# Question 6
# marks=int(input("Enter your Marks: "))
# if marks>100 or marks<0:
#     print("Invalid Number")
# elif marks<100 and marks>=90:
#     print("Ex")
# elif marks<90 and marks>=80:
#     print("A")
# elif marks<80 and marks>=70:
#     print("B")
# elif marks<70 and marks>=60:
#     print("C")
# elif marks<60 and marks>=50:
#     print("D")
# else:
#     print("F")


# Question 7
post=input("Enter your post: ")
a="harry"
if a in post:
    print("Post is talking about harry")
else:
    print("post is not talking about harry")
