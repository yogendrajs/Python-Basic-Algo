index=1
user=int(raw_input("guess a number"))
while index<5:
	if user==4:
		print "you guessed it right"
		break
	else:
		elif user<6:
			print "try once more"
		else:
			print "try once more"
else:
	print "you lost"