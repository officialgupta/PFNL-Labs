def checkPrefix(list1, prefix):
    for a in list1:
        if(a[:2] == prefix):
            print("*" + " " + a[:2] + " " + a)
        else:
            print(a[:2] + " " + a)