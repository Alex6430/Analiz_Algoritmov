def M_Alg_PH1(n, m):
    a = [0] * (m+1);
    a[0] = n - m + 1;
    for j in range(1, m):
        a[j] = 1;
    a[m] = -1;
    M_Alg_PH2(a,m);

def M_Alg_PH2(a,m):
    print(a[:m])
    if(a[1]>=a[0]-1):
        M_Alg_PH4(a,m);
    else:
        M_Alg_PH3(a,m);

def M_Alg_PH3(a,m):
    a[0]-=1;
    a[1]+=1;
    M_Alg_PH2(a,m)


def M_Alg_PH4(a,m):
    j=2;
    s=a[0]+a[1]-1;
    while(a[j]>=(a[0]-1)):
        s+=a[j];
        j+=1;
    if(j>=m):
        return
    else:
        x=a[j]+1;
        a[j]=x;
        j-=1;
        while(j>0):
            a[j]=x;
            s=s-x;
            j-=1;
        a[0]=s;
        M_Alg_PH2(a,m);

M_Alg_PH1(11,4);