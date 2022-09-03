def even(x):
    e_list=[]
    for i in x:
        if i%2==0:
            e_list.append(i)
    return e_list
print(even([1,2,3,4,5,6,7]))