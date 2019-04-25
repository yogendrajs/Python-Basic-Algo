water=int(raw_input("paani ka level bharo"))
if water<1:
	print "aur pani bharna hai"
elif water>1 and water<10:
	print "aur nahi bharna hai"
elif water>10:
	print "paani overflow"