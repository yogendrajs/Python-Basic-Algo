pink = int(input("enter an input "))
index = 2
while index < pink:
    if pink % index == 0:
        print ("not prime")
        break
    else:
        index+=1
else:
    print ("prime")