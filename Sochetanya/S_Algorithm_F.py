def S_Alg_F(args_w, N):
    t = 0
    args_c = [len(args_w)]*len(args_w)
    r = N
    args_d = []
    for i in range(1, len(args_w)):
        args_d.append(args_w[i] - args_w[i - 1])
    # print(args_w)
    # print(args_d)
    L2(args_w, args_c, args_d, t, r)
    pass


def L2(args_w, args_c, args_d, t, r):
    L3(args_w, args_c, args_d, t, r)
    pass


def L3(args_w, args_c, args_d, t, r):
    if (args_c[t] > 0 and r >= args_w[0]):
        t += 1
        args_c[t] = 0
        r -= args_w[0]
        L2(args_w, args_c, args_d, t, r)
    else:
        L4(args_w, args_c, args_d, t, r)


def L4(args_w, args_c, args_d, t, r):
    if (t == 0):
        exit()
    else:
        if (args_c[t - 1] > args_c[t] + 1 and r >= args_d[args_c[t] + 1]):
            args_c[t] += 1
            r -= args_d[args_c[t]]
            L2(args_w, args_c, args_d, t, r)
        else:
            L5(args_w, args_c, args_d, t, r)


def L5(args_w, args_c, args_d, t, r):
    r += args_w[args_c[t]]
    t -= 1
    L4(args_w, args_c, args_d, t, r)
