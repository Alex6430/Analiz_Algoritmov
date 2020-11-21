

def M_Alg_H1(n):
    a = [0]*n;
    b = [1]*(n-1);
    m=1;
    M_Alg_H2(a,b,m,n);

def M_Alg_H2(a,b,m,n):
    print(a)
    if(a[n-1]==m):
        m+=a[n-1];
        M_Alg_H4(a,b,m,n)
    else:
        M_Alg_H3(a,b,m,n)

def M_Alg_H3(a,b,m,n):
    a[n-1]+=1;
    M_Alg_H2(a,b,m,n);

def M_Alg_H4(a,b,m,n):
    j=n-2;
    while (a[j]==b[j]):
        j-=1;
    if(j==0):
        return
    else:
        a[j]+=1;
        if (a[j]==b[j]):
            m=b[j]+a[j];
        else:
            m=b[j];
        j+=1;
        while(j<n-1):
            a[j]=0;
            b[j]=m;
            j+=1;
        a[n-1]=0;
        M_Alg_H2(a,b,m,n)

print(M_Alg_H1(4))