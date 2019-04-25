s1=input("Enter first string:")
s2=input("Enter second string:")
a=set(s1) & set(s2)
print("The common letters are:")
for i in a:
    print(i)