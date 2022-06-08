def persistence(n):
    numsep = [int(a) for a in str(n)]
    total = 1
    count = 0
    if len(numsep) == 1:
        return count
    else:
        for i in range(len(numsep)):
            total *= numsep[i]
    count+=1
    numsep2 = [int(a) for a in str(total)]
    if len(numsep2) == 1:
        return count
    else:
        total = 1
        for i in range(len(numsep2)):
            total *= numsep2[i]
    count+=1
    numsep3 = [int(a) for a in str(total)]
    if len(numsep3) == 1:
        return count
    else:
        total = 1
        for i in range(len(numsep3)):
            total *= numsep3[i]
    count+=1
    numsep4 = [int(a) for a in str(total)]
    if len(numsep4) == 1:
        return count
    else:
        total = 1
        for i in range(len(numsep4)):
            total *= numsep4[i]
    count+=1
    numsep5 = [int(a) for a in str(total)]
    if len(numsep5) == 1:
        return count
    else:
        total = 1
        for i in range(len(numsep5)):
            total *= numsep5[i]
    count+=1
    numsep6 = [int(a) for a in str(total)]
    if len(numsep6) == 1:
        return count
    else:
        total = 1
        for i in range(len(numsep6)):
            total *= numsep6[i]
    count+=1
    return count




# import operator
# def persistence(n):
#    i = 0
#    while n>=10:
#        n=reduce(operator.mul,[int(x) for x in str(n)],1)
#        i+=1
#    return i

def persistence(n):
    n = str(n)
    count = 0
    while len(n) > 1:
        p = 1
        for i in n:
            p *= int(i)
        n = str(p)
        count += 1
    return count