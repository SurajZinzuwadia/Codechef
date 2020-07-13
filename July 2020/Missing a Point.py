try:
    testcase = int(input())
    while testcase:
        n = int(input())
        points = []
        for i in range(4*n-1):
            points.append(list(map(int,input().strip().split())))
        xValue = {}
        yValue = {}
        for i , j in points:
            if i not in xValue:
                xValue[i] = 1
            else:
                xValue[i]+=1
        for k,v in xValue.items():
            if v%2 != 0:
                print(k, end=" ")
        for i,j in points:
            if j not in yValue:
                yValue[j] = 1
            else:
                yValue[j] += 1
        for k,v in yValue.items():
            if v%2 != 0:
                print(k)
        testcase-=1
except EOFError:
    exit()