try:
    testcase = int(input())
    while(testcase):
        n = int(input())
        array = []
        for i in range(8):
            array.append(['X','X','X','X','X','X','X','X'])
        
        count = 0
        for i in range(8):
            for j in range(8):          
                array[i][j] = '.'
                count += 1
                if count == n:
                    break
                
            if count == n:
                break
        array[0][0] = 'O'

        for i in range(8):
            for j in range(8):
                print(array[i][j],end='')
            print()
    testcase-=1
except EOFError:
    exit()