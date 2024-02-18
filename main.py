

def menu_goster():
    print("\n** MENU **")
    print("1. Kitap Sırası")
    print("2. Kitap Ekleme")
    print("3. Kitap Silme")
    print("4. Çıkış")

def kitap_sirasi_goster():
    try:
        with open("book.txt", "r") as dosya:
            print("\n-- Kitap Sırası --")
            kitaplar = dosya.readlines()
            if not kitaplar:
                print("Henüz bir kitap eklenmemiş.")
            else:
                for kitap in kitaplar:
                    print(kitap.strip())
    except FileNotFoundError:
        print("Dosya bulunamadı! Lütfen bir kitap ekleyin.")

def kitap_ekle():
    kitap_adi = input("Eklemek istediğiniz kitabın adını girin: ")
    yazar_adi = input("Yazarın adını girin: ")
    basim_tarihi = input("Basım tarihini girin: ")
    sayfa_sayisi = input("Kitabın sayfa sayısını girin: ")

    with open("book.txt", "a") as dosya:
        dosya.write(f"Kitap Adı: {kitap_adi}\n")
        dosya.write(f"Yazar Adı: {yazar_adi}\n")
        dosya.write(f"Basım Tarihi: {basim_tarihi}\n")
        dosya.write(f"Sayfa Sayısı: {sayfa_sayisi}\n")
        dosya.write("-" * 20 + "\n")

    print(f"\n{kitap_adi} başarıyla eklendi.")

def kitap_sil():
    silinecek_kitap = input("Silmek istediğiniz kitabın adını girin: ")
    try:
        with open("book.txt", "r") as dosya:
            kitaplar = dosya.readlines()

        with open("book.txt", "w") as dosya:
            silindi_mi = False
            i = 0
            while i < len(kitaplar):
                if kitaplar[i].strip() == f"Kitap Adı: {silinecek_kitap}":
                    print(f"\n{silinecek_kitap} başarıyla silindi.")
                    silindi_mi = True
                    i += 5
                else:
                    for j in range(5):
                        if i + j < len(kitaplar):
                            dosya.write(kitaplar[i + j])
                    i += 5

            if not silindi_mi:
                print(f"\n{silinecek_kitap} adlı kitap bulunamadı.")
    except FileNotFoundError:
        print("Dosya bulunamadı.")

def login():
    max_deneme = 3
    while max_deneme > 0:
        kullanici_adi = input("Kullanıcı Adı: ")
        sifre = input("Şifre: ")

        with open("kullanici.txt", "r") as kullanici_dosya:
            dogru_kullanici = kullanici_dosya.readline().strip()
            dogru_sifre = kullanici_dosya.readline().strip()

        if kullanici_adi == dogru_kullanici and sifre == dogru_sifre:
            print("Giriş başarılı!\n")
            return True
        else:
            max_deneme -= 1
            print(f"Hatalı giriş! Kalan deneme hakkınız: {max_deneme}")

    print("Giriş hakkınız bitti. Program kapatılıyor.")
    return False

def main():
    if not login():
        return

    while True:
        menu_goster()
        secim = input("Numaralandırılmış menülerden istediğiniz menüye gidin (1-4): ")

        if secim == '1':
            kitap_sirasi_goster()
        elif secim == '2':
            kitap_ekle()
        elif secim == '3':
            kitap_sil()
        elif secim == '4':
            print("\nProgram sonlandırılıyor...")
            break
        else:
            print("\nGeçersiz seçenek, lütfen 1-4 arasında bir sayı girin.")

if __name__ == "__main__":
    main()
