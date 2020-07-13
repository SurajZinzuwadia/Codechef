try:
    testcase = int(input())
    while testcase:
        n = int(input())
        array = list(map(int,(input().strip().split())))
        result = int(0)
        for i in range(0,len(array)-1):
            result = result + abs(array[i+1]-array[i])-1
        print(result)
        testcase-=1
except EOFError:
    exit()
