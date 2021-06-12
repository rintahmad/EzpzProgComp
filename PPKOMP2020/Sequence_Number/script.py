n = int(input())
output = 1
counter = 0

for i in range(1000000):
    output += i
    counter += 1
    if n == counter:
        break
print(output)
