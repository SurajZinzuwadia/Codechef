T=int(input())
for item in range(T):
    n,m=map(int,input().split())
    if(n%2!=0) and (m%2!=0):
        print("NO")
    else:
        print("YES")

