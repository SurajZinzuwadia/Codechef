n=int(input())
while n>0:
    quote=list(map(str,input().split()))
    if 'not' in quote:
        print("Real Fancy")
    else:
        print("regularly fancy")
    n-=1
