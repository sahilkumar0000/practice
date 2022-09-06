def string1(sam_str):
    upper=0
    lower=0
    for i in sam_str:
        if i.isupper():
            upper+=1
        elif i.islower():
            lower+=1
        else:
            pass
    print("No. of Upper case Character:"+str(upper))
    print("No. of Lower case Character:"+str(lower))
    
string1("My Name is Sahil")