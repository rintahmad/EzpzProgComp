n =int(input())
M = list(map(int,input().split()))

print(sum(sorted(M)[-5:]))
