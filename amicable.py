k = int(input("enter an input: "))
a = 1
total = 0
while a < k:
    sum = 0
    nxtsum = 0
    for i in range(1, a):
        if a%i == 0:
            sum+=i
    # print (sum)
    nxtsum = 0
    for j in range(1, sum):
        if sum%j == 0:
            nxtsum+=j
    # print (nxtsum)
    if a == nxtsum:
        if sum == nxtsum:
            pass
        else:
            print (a)
            total+=a
    a+=1
print (total)
