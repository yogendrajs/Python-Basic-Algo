list = [10,11,2,3,4,5]
i=0
num = list[0]
while i<len(list):
    if list[i] < num:
        num = list[i]
    else:
    	i=i+1
else:    	
	print num
