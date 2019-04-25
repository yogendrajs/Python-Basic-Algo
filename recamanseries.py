# 0,1,3,6,2,7,1,8,16,7...(recaman series)
# a = 0
# for i in range(1, 15):
#     if a-i > 0:
#         print (a)
#         a = a-i
#     else:
#         print (a)
#         a = a+i
#####################################################33\\
# def phone(num):
#     for i in range(10):
#         if i not in num:
#             print (i)
# phone([9,8,2,1,1,2,1,3,7,7])
########################3#########################3
# 1
# 121
# 12321
# 1234321
# 123454321
# 12345654321

a = 1
k = "1"
b = str(a)
for i in range(1, 7):
    for j in range(i):
        a = a**2
        print (str(a))
        a = int(k+b)
        k += "1"
########################################################33
# a = 1
# i = 1
# while i < 20:
#     a = i**3
#     print (a)
#     i+=1
