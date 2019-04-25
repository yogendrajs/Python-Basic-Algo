a = raw_input("enter an input: ")
sum = 0
i = 0
while i < len(a):
    b = a[i]
    sum = 0
    for k in a:
        j = int(k)
        sum = sum+(j**2)
    if sum == 1:
        print("happy")
        break
    else:
        if sum == 4: #this is because, it will definitely loop through to come 42,0,16,20,4... if it is not a happy number, where it will break next
            print "not happy"
            break
        else:
            a = str(sum)
            continue
    i+=1

# user1 = input("enter a name: ")
# user2 = input("enter another name: ")
# if len(user1) == len(user2):
#     a= list(user1)
#     b= list(user2)
#     a.sort()
#     b.sort()
#     for i in range(len(a)):
#         if a[i] != b[i]:
#             print ("not anagram")
#             break
#     else:
#         print ("anagram")
# else:
#     print ("not anagram")
