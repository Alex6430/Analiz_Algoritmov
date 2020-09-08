def Alg_L(args):
    print(args,end=", ")
    j = len(args) - 2
    while (args[j] >= args[j + 1]):
        j -= 1
        if (j == 0):
            break
    l = len(args)-1
    while (args[j] >= args[l]):
        l -= 1
        if(l==0):
            return
    args[j], args[l] = args[l], args[j]
    k = j + 1
    l = len(args)-1
    while(k<l):
        args[k], args[l] = args[l], args[k]
        k+=1
        l-=1
    Alg_L(args)
