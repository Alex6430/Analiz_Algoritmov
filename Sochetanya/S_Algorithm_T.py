def S_Alg_T(t, n):
    if (n > t > 0):
        args_c = [j - 1 for j in range(0, t + 1)]
        args_c.append(n)
        args_c.append(0)
        j = t
        L2(args_c, j, t)
    else:
        print("Введите правильные значения t и n")
        t = int(input("t = "))
        n = int(input("n = "))
        S_Alg_T(t, n)
    pass


def L2(args_c, j, t):
    if (j > 0):
        x = j
        L6(args_c, x, j, t)
    else:
        L3(args_c, j, t)


def L3(args_c, j, t):
    if (args_c[1] + 1 < args_c[2]):
        args_c[1] += 1
        print(args_c[1:t + 1])
        L2(args_c, j, t)
    else:
        j = 2
        L4(args_c, j, t)


def L4(args_c, j, t):
    args_c[j - 1] = j - 2
    x = args_c[j] + 1
    if (x == args_c[j + 1]):
        j += 1
        L4(args_c, j, t)
    L5(args_c, x, j, t)


def L5(args_c, x, j, t):
    if (j > t):
        print(args_c[1:t + 1])
        exit()
    L6(args_c, x, j, t)


def L6(args_c, x, j, t):
    args_c[j] = x
    j -= 1
    print(args_c[1:t + 1])
    L2(args_c, j, t)
