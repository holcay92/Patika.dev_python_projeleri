boslist = []

def flat(l):
    for i in l:
        if type(i)==list:
         flat(i)
        else:
            boslist.append(i)

flat([[1,'a',['cat'],2],[[[3]],'dog'],4,5])
print(boslist)