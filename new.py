user = int(raw_input("enter a number "))
index = 0
num = 0
sum = 1
gum = 0
while index < user:
	if index <= 1:
		gum = index
	else:
		gum = num + sum
		num,sum = sum,gum
	print gum
	index+=1