
def string_reverse(str1):
    n=len(str1)-1
    str2= ''
    for i in range(0,len(str1)):
        str2+= str1[n-i]
    return str2
print(string_reverse("1234abcd"))