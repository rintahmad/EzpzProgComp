x,y = map(int,input().split())

numHen = int((((y/2) * 4)-x)/2)
numGoat = int((x - (numHen*2))/4)
print(str(numHen) + " " + str(numGoat))
    
