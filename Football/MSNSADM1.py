# cook your dish here
testcase = int(input())
for item in range(testcase):
    number = int(input())
    score = input().split()
    faul = input().split()
    #print(score)
    for item in range(int(len(score))):
        score[item] = int(score[item]) * 20
        faul[item] = int(faul[item]) * 10
        #print(score)
        #print(faul)
        score[item] = int(score[item]) - int(faul[item])
        if(score[item] <0):
            score[item] = 0
    print(max(score))
