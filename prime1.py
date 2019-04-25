user = int(input("enter an input "))
if user > 1:
	for i in range(2,user):
		if user % 2 == 0:
			print "not prime"
			break
	else:
		print "prime"
