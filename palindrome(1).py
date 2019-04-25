user=raw_input("enter your name ")
index=0
while index<len(user):
	if user[0]==user[-1] and user[1]==user[-2]:
		print "palindrome hai"
		break
	else:
		print "palindrome nahi hai"
		break