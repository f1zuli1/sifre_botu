import random
print("Meraba")
print("Guclu sifre olusturarak hesabinizi koruya bilirsiniz")
print("")
print("")
print("Hesabimi neden mi korumaliyim?")
print("Diger insanlar sizin hesablarinizi calarak sizin paralarinizi ele gecire bilirler")


karakterler = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
uzunluk= int(input("Lutfen sifrenizin uzunluğunu giriniz!"))
sifre = ""


for i in range(uzunluk):
    sifre += random.choice(karakterler)


print("Sifreniz:",sifre)
