
x = int(input())

for i in range(x):
    ayat = input()
    print(ayat.lower())
    print(ayat.upper())
    print(ayat[0].upper()+ayat[1:])
    print(ayat.swapcase())
    print(' '.join(ayat[:1].upper() + ayat[1:] for ayat in ayat.split(' ')))
    print("\n")
