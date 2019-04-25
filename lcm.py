print ("The program is to print the LCM of three numbers")
a = int(input("enter an input: "))
b = int(input("enter another input: "))
c = int(input("enter your third input: "))
i = a*b*c
lcm = 1
while i>1:
    if i%a == 0 and i%b == 0 and i%c == 0:
        lcm = i
    i-=1
print ("your lcm is",lcm)
