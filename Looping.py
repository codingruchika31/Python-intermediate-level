def looping():
    a=0
    b=1
    for i in range(10):
        temp=a
        a=b
        b=temp+b
        print(temp)

looping()