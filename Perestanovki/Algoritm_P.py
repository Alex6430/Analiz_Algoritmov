def Alg_P(args_a):
    P1(args_a)


def P1(args_a):
    args_c = [0] * len(args_a)
    args_o = [1] * len(args_a)
    P2(args_a, args_c, args_o)


def P2(args_a, args_c, args_o):
    print(args_a, end=", ")
    n = len(args_a)
    j, s = n-1, 0
    P4(args_a, args_c, args_o, j, s)


def P4(args_a, args_c, args_o, j, s):
    q = args_c[j] + args_o[j]
    if (q < 0):
        P7(args_a, args_c, args_o, j, s)
    elif (q == (j+1)):
        P6(args_a, args_c, args_o, j, s)
    else:
        P5(args_a, args_c, args_o, j, s, q)


def P5(args_a, args_c, args_o, j, s, q):
    args_a[j - args_c[j] + s], args_a[j - q + s] = args_a[j - q + s], args_a[j - args_c[j] + s]
    args_c[j] = q
    P2(args_a, args_c, args_o)


def P7(args_a, args_c, args_o, j, s):
    args_o[j] = -args_o[j]
    j -= 1
    print()
    P4(args_a, args_c, args_o, j, s)


def P6(args_a, args_c, args_o, j, s):
    if (j == 1):
        return
        # print()
        #P2(args_a, args_c, args_o)
    else:
        s += 1
    P7(args_a, args_c, args_o, j, s)
