numbers=[56,87,6,17,45,21]
i=0
var=0
while i<len(numbers):
    num=numbers[i]
    if num>20 and num<60:
        var=var+1
        i+=1
    else:
        i+=1
else:
    print var