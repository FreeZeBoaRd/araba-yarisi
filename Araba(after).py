import time


class Araba:
    def __init__(self, isim, marka):
        self.benzin = 100
        self.mesafe = 100
        self.isim = isim
        self.marka = marka

    def kontak(self):
        print(f"Wroooom!!! Wroooom!!! {self.isim} ({self.marka}) çalışıyor...")
        print("-" * 30)
        time.sleep(1.5)

    def gaza_bas(self):
        if self.benzin == 0:
            self.oyun_bitir()

        elif self.mesafe <= 25:
            self.mesafe -= 25
            self.benzin -= 5
            time.sleep(0.5)
            self.oyun_bitir()

        else:
            self.mesafe -= 25
            self.benzin -= 5
            time.sleep(1)
            print("25 metre ilerledin.")
            time.sleep(0.5)

    def yakit_doldur(self):
        self.benzin += 20
        time.sleep(1.75)
        print(f"{self.isim} için yakıt eklendi! Mevcut yakıt: {self.benzin}")

    def mevcut_durum(self):
        print("-" * 30)
        print(f"Araba: {self.isim} ({self.marka})")
        print(f"Kalan yakıt: {self.benzin}")
        print(f"Kalan mesafe: {self.mesafe}")
        print("-" * 30)
        time.sleep(2)

    def oyun_bitir(self):
        if self.benzin == 0 and self.mesafe > 0:
            print(f"{self.isim} ({self.marka}): Yakıtın bitti. KAYBETTİN!!!")
            self.ozel_mesaj(kazandi=False)
            quit()

        elif self.mesafe == 0:
            print(f"{self.isim} ({self.marka}): Tebrikler. KAZANDIN!!!")
            self.ozel_mesaj(kazandi=True)
            quit()

    def ozel_mesaj(self, kazandi):
        mesajlar = {
            "Mercedes": {
                "kazandi": "Mercedes, Alman mühendisliğinin zirvesi! Gücü ve konforu bir arada yaşadın. Tebrikler!",
                "kaybetti": "Mercedes'in konforunu yaşamak için biraz daha deneyim gerekiyor. Bir dahaki sefere kazanacağına inanıyorum!"
            },
            "Audi": {
                "kazandi": "Audi'nin Quattro gücüyle zafere ulaştın! Teknoloji ve hız seninleydi!",
                "kaybetti": "Audi'nin keskin hatlarını biraz daha zorlamalısın. Bir dahaki yarışta daha iyi olacaksın!"
            },
            "BMW": {
                "kazandi": "BMW'nin saf sürüş keyfiyle birinciliğe ulaştın! Müthiş bir performanstı!",
                "kaybetti": "BMW'nin performansını biraz daha iyi kullanmalısın. Ama unutma, asla pes etme!"
            }
        }

        print("-" * 50)
        if kazandi:
            print(mesajlar[self.marka]["kazandi"])
        else:
            print(mesajlar[self.marka]["kaybetti"])
        print("-" * 50)


# Kullanıcıya araba seçtirme
Arabalar = {
    "1": "Mercedes",
    "2": "Audi",
    "3": "BMW"
}

while True:
    arabasecim = input(
        "Lütfen istediğiniz arabanın numarasını yazınız!\n1 ---> Mercedes\n2 ---> Audi\n3 ---> BMW\n----------\n")

    if arabasecim in Arabalar:
        secilen_marka = Arabalar[arabasecim]
        print("-" * 30)
        print(f"Tebrikler! Seçtiğiniz araç: {secilen_marka}")
        print("-" * 30)
        time.sleep(1)
        break
    else:
        print("Lütfen geçerli bir seçenek giriniz (1, 2 veya 3).")

# Kullanıcıdan araba ismi al
araba_ismi = input("Lütfen arabanıza bir isim verin: ")
araba1 = Araba(araba_ismi, secilen_marka)

print("Araba yarışına hoş geldin!")
araba1.kontak()

# Oyun Döngüsü
while True:
    print("-" * 30)
    komut = input(
        "Lütfen yapmak istediğiniz eylemi seçiniz:\n1 ---> Gaza Bas\n2 ---> Yakıt Doldur\n3 ---> Mevcut Durum\n------------------------------\n")

    if araba1.benzin == 0:
        araba1.oyun_bitir()
        break

    elif komut == "1":
        araba1.gaza_bas()

    elif komut == "2":
        araba1.yakit_doldur()

    elif komut == "3":
        araba1.mevcut_durum()

    else:
        print("Lütfen sadece {1}, {2} veya {3} seçeneklerinden birini girin.")
        time.sleep(2)
