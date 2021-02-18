# SnakePRG
# DAHA DETAYLI ANLATIM İÇİN eneserolsahin.wixsite.com/snakeprg SİTESİNDEN BİZE ULAŞABİLİRSİNİZ.
# Python Nesne Tabanlı Programlama Örnekleri
import random
import time

class Kumanda():

    # Burada televizyonun durumunu kanal sayısı vs. eklendiği bölüm. (DAHA DETAYLI ANLATIM İÇİN eneserolsahin.wixsite.com/snakeprg SİTESİNDEN BİZE ULAŞABİLİRSİNİZ.)
    def __init__(self,tv_durum = "Kapalı",tv_ses = 0,kanal_listesi = ["Trt"],kanal = "Trt"):

        self.tv_durum = tv_durum

        self.tv_ses = tv_ses

        self.kanal_listesi = kanal_listesi

        self.kanal = kanal
       # Burada televizyonun açılıp kapanması, eğer açıkken açmaya çalışırsak ise "zaten açık" şeklinde yazılar yazdırıyoruz. (DAHA DETAYLI ANLATIM İÇİN eneserolsahin.wixsite.com/snakeprg SİTESİNDEN BİZE ULAŞABİLİRSİNİZ.)
    def tv_ac(self):

        if (self.tv_durum == "Açık"):
            print("Televizyon zaten açık....")
        else:
            print("Televizyon Açılıyor...")
            self.tv_durum  = "Açık"
            

    def tv_kapat(self):

        if (self.tv_durum == "Kapalı"):
            print("Televizyon Zaten Kapalı..")
        else:
            print("Televizyon Kapanıyor....")
            self.tv_durum = "Kapalı"
     # Burada ise sesi açıp kapamayı ne ne kadar açılıp kapanacağını yazıyoruz. (DAHA DETAYLI ANLATIM İÇİN eneserolsahin.wixsite.com/snakeprg SİTESİNDEN BİZE ULAŞABİLİRSİNİZ.)
    def ses_ayarları(self):

        while True:
            cevap =  input("Sesi Azalt: '<'\nSesi Artır: '>'\nÇıkış : çıkış")

            if (cevap == "<"):
                if (self.tv_ses != 0):

                    self.tv_ses -= 1
                    print("Ses:",self.tv_ses)
            elif (cevap == ">"):
                if (self.tv_ses != 31):

                    self.tv_ses += 1

                    print("Ses:",self.tv_ses)
            else:
                print("Ses Güncellendi:",self.tv_ses)
                break
            # Burada ise kanal eklemeyi yazıyoruz. (DAHA DETAYLI ANLATIM İÇİN eneserolsahin.wixsite.com/snakeprg SİTESİNDEN BİZE ULAŞABİLİRSİNİZ.)
    def kanal_ekle(self,kanal_ismi):

        print("Kanal ekleniyor lütfen bekleyin....")
        time.sleep(3)

        self.kanal_listesi.append(kanal_ismi)

        print("Kanal Eklendi.....")
        # Burada rastgele kanal seçme ve kanal durumunu gösteriyoruz.(DAHA DETAYLI ANLATIM İÇİN eneserolsahin.wixsite.com/snakeprg SİTESİNDEN BİZE ULAŞABİLİRSİNİZ.)
    def rastgele_kanal(self):

        rastgele = random.randint(0,len(self.kanal_listesi)-1)


        self.kanal = self.kanal_listesi[rastgele]

        print("Şu anki Kanal:" ,self.kanal)
    def __len__(self):

        return len(self.kanal_listesi)

    def __str__(self):

        return "Tv Durumu: {}\nTv Ses: {}\nKanal Listesi: {}\nŞu anki kanal: {}\n".format(self.tv_durum,self.tv_ses,self.kanal_listesi,self.kanal)


kumanda = Kumanda()

# Burada girişte yazan bilgiler ve hangi bölümü nasıl açacağımızı yazıyor. (DAHA DETAYLI ANLATIM İÇİN eneserolsahin.wixsite.com/snakeprg SİTESİNDEN BİZE ULAŞABİLİRSİNİZ.)
print("""
____              _        ____  ____   ____
/ ___| _ __   __ _| | _____|  _ \|  _ \ / ___|
\___ \| '_ \ / _` | |/ / _ \ |_) | |_) | |  _      ___) | | | | (_| |   <  __/  __/|  _ <| |_| |
|____/|_| |_|\__,_|_|\_\___|_|   |_| \_\\____|
Televizyon Uygulaması
1. Tv Aç
2. Tv Kapat
3. Ses Ayarları
4. Kanal Ekle
5. Kanal Sayısını Öğrenme
6. Rastgele Kanala Geçme
7. Televizyon Bilgileri
Çıkmak için 'q' ya basın.
""")

# Burada ise işlemleri hangi tuşla nasıl yapacağınız yazıyor. (DAHA DETAYLI ANLATIM İÇİN eneserolsahin.wixsite.com/snakeprg SİTESİNDEN BİZE ULAŞABİLİRSİNİZ.)
while True:

    işlem = input("İşlemi Seçiniz:")

    if (işlem == "q"):
        print("Program Sonlandırılıyor...")
        break

    elif (işlem == "1"):
        kumanda.tv_ac()
    elif (işlem == "2"):
        kumanda.tv_kapat()

    elif (işlem == "3"):
        kumanda.ses_ayarları()

    elif (işlem == "4"):
        kanal_isimleri = input("Kanal isimlerini ',' ile ayırarak girin:")

        kanal_listesi = kanal_isimleri.split(",")

        for eklenecekler in kanal_listesi:
            kumanda.kanal_ekle(eklenecekler)
    elif (işlem == "5"):

        print("Kanal Sayısı:",len(kumanda))

    elif (işlem == "6"):
        kumanda.rastgele_kanal()
    elif (işlem == "7"):
        print(kumanda)
     # Burada "else" kodunu kullanarak (else "eğer" demek) eğer atadıklarımızdan başka bir işlem kullanıcı tarafından yazılırsa "Böyle Bir İşlem Bulunmamakta..." yazısını yazdırıyoruz. (DAHA DETAYLI ANLATIM İÇİN eneserolsahin.wixsite.com/snakeprg SİTESİNDEN BİZE ULAŞABİLİRSİNİZ.)
    else:
        print("Böyle Bir İşlem Bulunmamakta...")
