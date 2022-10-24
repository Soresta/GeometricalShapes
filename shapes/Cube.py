cubeLength = int(input("Enter: "))
gap = " "
save =cubeLength
gapA = cubeLength-2
gapB = cubeLength-2
gapC = cubeLength-2
gapD = 1
star ="*"

#x ekseni:
for t in  range(gapC+3):
    print(gap,end="")
for w in range(cubeLength):
    print(star,end="")
    print(gap,end="")
print("")

for i in range(int(cubeLength)):
    for m in range(0,gapC+2):
        print(gap,end="")
    gapC-=1
    for j in range(1):
        print(star,end="")

    for u in range(gapB*2+1):
        print(gap,end="")

    for j in range(1):
        print(star,end="")

    for p in range(gapD):
        print(gap,end="")
    gapD+=1
    for v in range(1):
        print(star,end="")

    cubeLength = save
    print("")
sayı = cubeLength

for w in range(cubeLength):
    print(star,end="")
    print(gap,end="")

for e in range(gapD-1):
    print(gap,end="")
print(star)

for m in range(cubeLength+1):
    sonuc = gap * sayı
    print(star,end="")
    for l in range(gapA*2+1):
        print(gap,end="")
    print(star,end="")

    print(sonuc,end="")
    print(star)
    sayı-=1

for i in range(cubeLength):
    print(star,end="")
    print(gap, end="")
