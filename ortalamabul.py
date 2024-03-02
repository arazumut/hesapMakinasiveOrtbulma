def notlari_al():
    while True:
        try:
            notlar_str = input("Notları arasına virgül koyarak girin (örn. 75,80,90): ")
            notlar = [float(not_str) for not_str in notlar_str.split(',')]
            return notlar
        except ValueError:
            print("Hatalı giriş. Lütfen sayıları virgülle ayırarak girin.")

def ortalama_hesapla(notlar):
    toplam_not = sum(notlar)
    not_sayisi = len(notlar)
    ortalama = toplam_not / not_sayisi
    return ortalama
#by Kamil Umut Araz  -   instagram : k.umutarazz    --  linkedin: Kamil Umut Araz

def main():
    notlar = notlari_al()
    
    if not notlar:
        print("Not girilmedi. Program sonlandırılıyor.")
        return
    
    ortalama = ortalama_hesapla(notlar)
    
    print("Girilen Notlar:", notlar)
    print("Notların Ortalaması:", ortalama)

if __name__ == "__main__":
    main()
