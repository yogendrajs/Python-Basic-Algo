user = raw_input("enter an input ")
index = 20
count = user + user
while index > 0:
    print ' ' * index + user
    user = user + count
    index -= 1