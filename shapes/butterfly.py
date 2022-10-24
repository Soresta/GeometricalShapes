ortauzunlu = int(input("Uzunluğu girin: "))
bosluk = " "
yıldız = "*"
boslukSayısı = ortauzunlu-2
yıldızsayısı = 1

for j in range(0,ortauzunlu-1):
    for i in range(0,yıldızsayısı):
        print(yıldız,end="")
    yıldızsayısı +=1
    for n in range(0,boslukSayısı*2):
        print(bosluk,end="")
    boslukSayısı -=1
    for o in range(0,yıldızsayısı-1):
        print(yıldız,end="")
    print("")

ortauzunlu = ortauzunlu-1
boslukSayısı = 1
yıldızsayısı = ortauzunlu-1
for j in range(0,ortauzunlu):
    for i in range(0,yıldızsayısı):
        print(yıldız,end="")
    yıldızsayısı -=1
    for n in range(0,boslukSayısı*2):
        print(bosluk,end="")
    boslukSayısı +=1
    for o in range(0,yıldızsayısı+1):
        print(yıldız,end="")
    print("")