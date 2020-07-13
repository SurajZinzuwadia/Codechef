try:
    testcase = int(input())
    while testcase:
        n = int(input())
        cresult = 0
        mresult = 0
        for _ in range(0,n):
            array = list(map(int,input().strip().split()))
            ccount = (0)
            mcount = (0)
            if(len(str(array[0])) >1):
                for i in str(array[0]):
                    ccount +=int(i)
            else:
                ccount = array[0]
            if(len(str(array[1])) >1):
                for i in str(array[1]):
                    mcount+=int(i)
            else:
                mcount= array[1]
            if(ccount > mcount):
                cresult+=1
            elif(ccount < mcount):
                mresult+=1
            else:
                cresult+=1
                mresult+=1
        if(cresult > mresult):
            print(0,cresult)
        elif(mresult > cresult):
            print(1,mresult)
        else:
            print(2,cresult)
        testcase-=1
except EOFError:
    exit()