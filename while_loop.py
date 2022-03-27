def whilee ():
    y=[]
    while 1:
        s=int(input("enter the number: "))
        y.append(s)
        if s==0:
            break
    return y    
print(whilee())
