#30pts
Testcase = int(input())
for i in range(Testcase):
    List = []
    k = 0
    flag = 0
    N = input()
    List = input().split()
    value = 0
    for item in List:
        value = value + int(item)
    finalAns = (value / len(List))
    #print("Sum:",value)
    #print("Final ans is:" , finalAns)
    for j in range(0,int(N)):
        checksum = 0
        checkmean = 0
        for item in range(0,len(List)):
            if(item == j):
                continue
            checksum = checksum + int(List[item])
        #    print("sum=",j,checksum)
        checkmean =  (checksum / (len(List)-1))
       # print("Mean=",checkmean)
        if(finalAns == checkmean):
            #print(List[j])
            k= j+1
            flag = 1
            break
    if(flag ==1):
        print(k)
    else:
        print("Impossible")
            
       
