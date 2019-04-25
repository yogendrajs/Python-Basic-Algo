day = raw_input("Aaj ka din kya hai? (monday/tuesday) > ")
time = raw_input("Kaunse samay ka khana banana hai? (lunch/dinner) > ")
if day == "monday" or time== "lunch":
    print "Daal-Roti banegi aaj"
elif day == "tuesday" or time == "dinner":
    print "Pav-Bhaji banegi aaj toh :)"