x,y = map(int,input().split())

numChicken = int((((y/2) * 4)-x)/2)
numCow = int((x - (numChicken*2))/4)
print(str(numChicken) + " " + str(numCow))
    
