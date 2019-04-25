input = int(input("Enter your input: "))
mainlist = []
sum = 0
for x in range(1, input):
    k = 11
    for user in range(10, x):
        user = str(user)
# user = input("Enter the number: ")
        y = user
        maincounter = 11
        while len(user)!=0:
            count = 0
            for i in range(2, int(user)):
                if int(user)%i == 0:
                    count+=1
                    if count > 0:
                        break
            else:
                maincounter +=1
            if count>0 or user == "1":
                # print ("not truncatable from left to right")
                break
            if count == 0:
                user = user[1:]

        if len(user) == 0:
            user = y
            while len(user)!=0:
                counter = 0
                for i in range(2, int(user)):
                    if int(user)%i == 0:
                        counter+=1
                        if counter > 0:
                            break
                else:
                    maincounter +=1
                if counter>0 or user == "1":
                    # print ("not truncatable from right to left")
                    break
                if counter == 0:
                    user = user[:-1]
            else:
                # print (y, "is perfect truncatable prime from both ends:)", maincounter)
                if y not in mainlist:
                    mainlist.append(y)
for z in mainlist:
    sum+=int(z)
    print (z)
print ("sum", sum)
