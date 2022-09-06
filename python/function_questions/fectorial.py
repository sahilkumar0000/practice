def fectorial(num):
    multi=1
    if num==0:
        return 1
    else:
        # for i in range(1,num+1):
        #     multi*=i
        # return multi
        return num*fectorial(num-1)     #second method with recursion
print(fectorial(4))



