try:
    T = int(input().strip())
    while T:
        N = input().strip()
        P = list(map(int, input().strip().split()))
        P.sort(reverse=True)
        sum = 0
        i = int(0)
        while len(P) > 0:
            X = P.pop(0)
            if X == 0:
                continue
            else:
                sum += (X - ( i if (X-i > 0) else X)) % 1000000007
                i+=1
        print(sum%1000000007)
        T -= 1

except EOFError:
    exit()