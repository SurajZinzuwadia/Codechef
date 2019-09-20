#20pts solve
n = int(input())
L = []
sum=0
for i in range(0,n):
    number = int(input())
    for i in range(1,number+1):
        L.append(i)
    if(number ==1):
        x = L.pop()
        print(x)
    else:
        L.sort()
        for i in range(0,number-1):
            x = L.pop()
            y = L.pop()
            sum = x + y + x*y
            L.append(sum) 
        print(sum% 1000000007)
        ex = L.pop()
