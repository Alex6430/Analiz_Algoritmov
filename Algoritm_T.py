def Alg_T(n):
    N = fact(n)
    d = N // 2
    m = 2
    t = [0 for i in range(fact(n) - 1)]
    t[d - 1] = 1
    T2(n, N, d, m, t)


def T2(n, N, d, m, t):
    if (m == n):
        # print(list(zip(*[iter(t)] * (n-1))))
        print(t)
        exit()
    else:
        m += 1
        d = int(d / m)
        k = 0
    T3(n, N, d, m, t, k)


def T3(n, N, d, m, t, k):
    k += d
    j = m - 1
    while (j > 0):
        t[k - 1] = j
        j -= 1
        k += d
    t[k - 1] += 1
    k += d
    while (j < m - 1):
        j += 1
        t[k - 1] = j
        k += d
    if (k < N):
        T3(n, N, d, m, t, k)
    elif (k >= N):
        T2(n, N, d, m, t)


def fact(n):
    if (n == 0):
        return 1
    elif (n == 1):
        return 1
    else:
        return n * fact(n - 1)
