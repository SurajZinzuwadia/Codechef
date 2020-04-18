try:
    T = int(input().strip())
    while T:
        N = input().strip()
        P = list(map(int, input().strip().split()))
        List = []
        count = 6
        i = 0
        length = len(P)
        while length > 0:
            if P[i] != 0:
                List.append(i)
                if(len(List) == 2):
                    Y = List[0]
                    X = List[1]
                    count = X - Y
                    if(count < 6):
                        break
                    List.pop(0)
            i+=1
            length-=1
        if(count >= 6):
            print("YES")
        else:
            print("NO")
        T -= 1
except EOFError:
    exit()