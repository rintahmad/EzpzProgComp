x1,y1 = map(int , input().split()) 
x2,y2 = map(int , input().split()) 

A = (x1+x2)/2
B = (y1+y2)/2

print(str(A).replace(".0","")+ " " + str(B).replace(".0",""))

