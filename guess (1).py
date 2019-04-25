index=0
while index<10:
	user = input("enter input")
	if user == 4:
		print 'you win'
		break
	else:
		if user > 4:
			print 'try once more'
			index+=1
		else:
			print 'try once more'
			index+=1
else:
	print 'you lose'