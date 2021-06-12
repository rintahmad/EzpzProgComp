t_shirts = int(input())
membership = input()
total = 0

if t_shirts < 20:
    if membership == "ahli":
        total = 16 * t_shirts
    else:
        total = 18 * t_shirts
elif t_shirts < 50:
    if membership == "ahli":
        total = 13 * t_shirts
    else:
        total = 15 * t_shirts
elif t_shirts < 200:
    if membership == "ahli":
        total = 10 * t_shirts
    else:
        total = 12 * t_shirts
else:
    if membership == "ahli":
        total = 8 * t_shirts
    else:
        total = 9 * t_shirts

print(str(total)+".00")
