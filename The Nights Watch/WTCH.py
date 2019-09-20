T = int(input())
for loop in range(T):
    N = int(input())
    tower = []
    ch = input()
    for item in ch:
        tower.append(int(item))
        
    count = 0
    
    for i in tower:
        
        if(i==0):
            flag=0
        else:
            flag=1
            break
            
    if(flag==0):
        
        if N%2==0:
            count=N//2
        else:
            count=(N//2)+1
            
    else:
        for i in range(len(tower)):
            if i==0:
                if tower[i]==0 and tower[i+1]==0 and tower[i]!=1:
                    tower[i]=1
                    count=count+1
            elif i==len(tower)-1:
                if tower[i-2]==1 and tower[i-1]==0 and tower[i]!=1:
                    tower[i]=1
                    count=count+1
            elif tower[i-1]==0 and tower[i+1]==0 and tower[i]!=1:
                tower[i]=1
                count=count+1   
    print(count)
