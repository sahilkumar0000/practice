# Question 1 

# rows=6
# for i in range(rows):
#     for j in range(0,i):
#         print(i,end="")
#     print(" ")

# Question 1 inverted
# b=0
# rows=6
# for i in range(rows,0,-1):
#     b+=1
#     for j in range(0,i):
#         print(b,end="")
#     print(" ")

# question 1 inverted but number is upside down

# rows=6
# for i in range(rows,0,-1):
#     for j in range(0,i+1):
#         print(i,end="")
#     print(" ")

# Question 2
# rows=6
# for i in range(rows):
#     for j in range(1,i+1):
#         print(j,end="")
#     print(" ")

# Question 3
# i=5
# for j in range(i,0,-1):
#     for k in range(0,j):
#         print(i,end="")
#     print("")

#QUestion 4
# rows =6
# for i in range(rows):
#     for j in range(i,0,-1):
#         print(j,end="")
#     print("")

# question 5 Inverted Half Pyramid Number Pattern
# b=0
# rows = 6
# for i in range(rows,0,-1):
#     for j in range(1,i+2):
#         print(j,end="")
#     print("")

# Question 6 Pyramid of Natural Numbers Less Than 10
# l=1
# stop=2
# rows=3
# for i in range(0,rows):
#     for j in range(1,stop):
#         print(l, end="")
#         l+=1
#     print("")
#     stop+=2

#question 7 Reverse Pattern of Digits from 10 
# start = 1
# stop = 2
# currentNumber = stop
# for row in range(2, 6):
#     for col in range(start, stop):
#         currentNumber -= 1
#         print(currentNumber, end=’ ‘)
#     print("")
#     start = stop
#     stop += row
#     currentNumber = stop

# start =1 
# stop =2
# currentnum=stop
# for i in range(2,6):
#     for j in range(start,stop):
#         currentnum-=1
#         print(currentnum,end="")
#     print("")
#     start=stop
#     stop+=i
#     currentnum=stop

# Question 8 Unique Pyramid Pattern of Digits


# rows=6
# for i in range(1,rows+1):
#     for j in range(1,i-1):
#         print(j, end="") 
#     for j in range(i-1,0,-1):
#         print(j,end="")

#     print("")

# Question 9 Connected Inverted Pyramid Pattern of Numbers

# rows =6
# for i in range(0,rows):
#     for j in range(rows-1,i,-1):
#         print(j,end=" ")
#     for k in range(i+1,rows):
#         print(k,end=" ")
#     print("")

# Question 10 Even Number Pyramid Pattern

# rows=5
# last_even=rows*2
# even_num=last_even
# for i in range(1,rows+1):
#     even_num=last_even                #2
#     for j in range(i):
#         print(even_num,end=" ")
#         even_num-=2
#     print("")

# rows=5
# b=rows*2
# for i in range(rows+1):
#     b=rows*2
#     for j in range(i):               #1
#         print(b,end=" ")
#         b-=2
#     print("")

#Question 11 Pyramid of Horizontal Tables
# rows=6
# x=0
# y=0
# for i in range(rows+1):
#     x=0 
#     for j in range(i+1):
#         print(x*y,end=" ")        #1
#         x=x+1
#     y+=1
#     print("")

# rows=6
# for i in range(0,rows):
#     for j in range(0,i+1    ):    #2
#         print(i*j,end=" ")
#     print("")

# Question 12 Pyramid Pattern of Alternate Numbers
# rows =6
# for i in range(rows):
#     for j in range(0,i+1):                 
#         if j/2!=0:                    #1
#             print(i*2-1,end=" ")
#     print("")

# rows=6
# i=1
# while i<=rows:
#     j=1
#     while j<=i:
#         print(i*2-1,end=" ")          #2
#         j+=1
#     i=i+1
#     print("")

#question 13
# rows=6
# for i in range(1,rows):
#     for j in range(rows,i,-1):
#         print(" ",end="")             #1
#     for j in range(1,i+1):
#         print(j, end="")
#     print(" ")
# rows=6
# for i in range(0,rows):
#     num=1
#     for j in range(rows,0,-1):
#         if j>i:
#             print(" ",end="")
#         else:
#             print(num,end="")
#             num+=1
#     print(" ")

# Question 14 Equilateral Triangle with Stars (Asterisk Symbol)
rows = 7
f=int(rows)
for i in range(rows):

    for j in range(f,0,-1):
        print(" ",end=" ")
    for j in range()
    print("")

#question 15