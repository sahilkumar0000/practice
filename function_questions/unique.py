def unique(list1):
    list_unique=[]
    for x in list1:
        if x not in list_unique:
            list_unique.append(x)
    return list_unique

print(unique((1,2,2,2,3,4,5)))