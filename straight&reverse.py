a = 1
for i in range(1, 10):
    j = 0
    if i%2==0:
        while j < i:
            print (a, end="")
            a+=1
            j+=1
        print ()
    else:
        sum = " "
        while j < i:
            sum = sum + str(a)
            a+=1
            j+=1
        string_rev = ""
        for i in range(len(sum)-1, -1, -1):
            string_rev = string_rev + sum[i]
        print (string_rev, end="")
        print ()
