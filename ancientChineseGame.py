rab = 35
chi = 35
while rab > 0:
    legs = 4*rab+2*chi
    if legs == 92:
        print (rab, chi)
        break
    rab-=1
