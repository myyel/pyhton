i=0
liste=[*range(1,11)]
while i<11:
    for a in liste:
        s=i*a
        print("{0} x {1} = {2}".format(i,a,s))
        if a==10:
            print("----------\n")
            
    i+=1