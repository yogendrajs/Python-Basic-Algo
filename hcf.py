print ("This is the program to print the HCF of three numbers")
a = int(input("enter an input: "))
b = int(input("enter another input: "))
c = int(input("enter a third input: "))
pro = a*b*c
# 1,2,3,6
i = 1
while i < pro:
    if a%i == 0 and b%i == 0 and c%i == 0:
        hcf = i
    i+=1
print (hcf)
