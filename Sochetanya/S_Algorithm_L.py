def S_Alg_L(t, n):
    if (n >= t >= 0):
        args_c = [j-1 for j in range(0, t+1)]
        args_c.append(n)
        args_c.append(0)
        # print(args_c)
        L2(args_c,t)
    else:
        print("Введите правильные значения t и n")
        t = int(input("t = "))
        n = int(input("n = "))
        S_Alg_L(t, n)

def L2(args_c,t):
    j = 1
    while (args_c[j] + 1 == args_c[j + 1]):
        args_c[j] = j - 1
        j += 1
    if (j > t):
        # print(args_c)
        print(args_c[1:t + 1])
        return
    args_c[j] = args_c[j] + 1
    print(args_c[1:t+1])
    L2(args_c,t)



