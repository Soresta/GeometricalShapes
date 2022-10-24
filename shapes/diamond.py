bosluk = " "
satırsayısı = int(input("Şeklin kaç satır olmasını istersiniz: "))
bosluksatırı = satırsayısı
bosluksatırı = int(bosluksatırı)
yıldız = "*"
ortabosluk = 0
for i in range(0,satırsayısı):
    for i in range(0,bosluksatırı):
        print(bosluk, end="")
    print(yıldız,end="")
    bosluksatırı -= 1
    for i in range(0,ortabosluk):
        print(bosluk,end="")
    ortabosluk += 2
    print(yıldız)
for i in range(0,satırsayısı+1):
    for i in range(0,bosluksatırı):
        print(bosluk, end="")
    print(yıldız,end="")
    bosluksatırı += 1
    for i in range(0,ortabosluk):
        print(bosluk,end="")
    ortabosluk -= 2
    print(yıldız)

