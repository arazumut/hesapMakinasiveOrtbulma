import math

secim = int(input("\nToplama icin '1'e basiniz\ncıkarma icin '2' ye basiniz\ncarpma için '3'e basiniz\nBolme icin '4'e basiniz\nFaktoriyel hesabi icin '5'e basiniz\nHangi islemi yapmak istediginizi seciniz: "))
#by Kamil Umut Araz  -   instagram : k.umutarazz    --  linkedin: Kamil Umut Araz
if 1 <= secim <= 5:
    sayi1 = int(input("Sayi1: "))
    sayi2 = int(input("Sayi2: "))

    if secim == 1:
        print(f"İslem sonucunuz: {sayi1 + sayi2}")
    elif secim == 2:
        print(f"İslem sonucunuz: {sayi1 - sayi2}")
    elif secim == 3:
        print(f"İslem sonucunuz: {sayi1 * sayi2}")
    elif secim == 4:
        if sayi2 != 0:
            print(f"İslem sonucunuz: {sayi1 / sayi2}")
        else:
            print("Sifira bolunemez!")
    elif secim == 5:
        print(f"Faktoriyel sonucunuz: {math.factorial(sayi1)}")
else:
    print("Seciminiz gerceklestirilemiyor.")

