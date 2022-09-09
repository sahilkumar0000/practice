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

start =1 
stop =2
currentnum=stop
for i in range(2,6):
    for j in range(start,stop):
        currentnum-=1
        print(currentnum,end="")
    print("")
    start=stop
    stop+=i
    currentnum=stop
    
