user = raw_input("enter a input ")
index = 0
count = user
while index <10:
		print ' ' * 10 + count
		count = count + user
		index +=1
else:
	count = user
	while index > 1:
		print ' ' * index + count
		count = count + user
		index -= 1