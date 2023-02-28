# -*- coding: utf-8 -*-
"""03_Fonksiyonlar_Test_Sorular.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1OBQMEzFD3Jf5liCB6PpvRCTRcvBU7T_x

## Fonksiyon Uygulamasi

### Bilgi:
3 üzeri 2 = 9 
Python'da üstel sayilari hesaplamak icin 3**2 seklinde gösterilir.
"""

3**2

"""#### Soru 1: Asagidaki fonskiyonu 2 parametre alacak ve üstel sonucu return edecek bicimde doldurun"""

def ustel_sayi_v1(a,b):
  return a**b

ustel_sayi_v1(3,2)

"""#### Soru 2: Asagidaki fonskiyonu 2 parametre alacak ve üstel sonucu return edecek bicimde  ve  ** yerine for döngüsü ile hesaplayacak bicimde olusturun"""

def ustel_sayi_v2(taban,b):
    sonuc=1
    for us in range(b):
        sonuc = sonuc * taban
    return sonuc

ustel_sayi_v2(3,2)

"""### Bilgi:
.sort() komutu listeyi kücükten büyüge siralar
"""

liste = [1,5,2,3,4]
liste.sort()
liste

"""#### Soru 3: Asagidaki fonskiyonu 1 parametre alacak (sadece sayilardan olusan liste tipinde) ve en büyük iki sayiyi döndürecek bicimde olusturun"""

def listedeki_en_buyuk_iki_sayi(x):
    liste.sort()
    return liste[-1], liste[-2]


liste=[1,5,2,3,4]
listedeki_en_buyuk_iki_sayi(liste)

"""## Map, Filter ve Lambda Uygulamalari

#### Soru 4: Asagidaki fonskiyonu 1 parametre alacak (liste tipinde) ve sadece str tipindeki degerleri filter ve lambda ifadelerini kullanarak filtreleyecek bicimde olusturun
"""

def str_filtrele():
    """
    parametre: rastgele tipte elemanlar iceren
    tip:       liste
    örnek:     [1,2,3,5,'abc','a',True]
    
    r-return:  sadece string tipindeki degerleri iceren
    r-tip:     liste
    r-örnek:   ['abc', 'a']
    """
    
    pass

"""#### Soru 5: Asagidaki fonskiyonu 1 parametre alacak (sadece sayi iceren liste tipinde) ve map ve lambda ifadelerini kullanarak 6 sifir atacak bicimde olusturun"""

def paradan_alti_sifir_at():
    """
    parametre: sayi tipinde elemanlar iceren
    tip:       liste
    örnek:     [1000000, 90000000, 15000000]
    
    r-return:  liste elemanlarinin 6 sifir atilmis halinde
    r-tip:     liste
    r-örnek:   [1, 90, 15]
    """
    
    pass

"""## Kullanici Girdisi Uygulamasi

#### Soru 6: Asagidaki fonskiyonu input komutu ile kullanicidan saat ve dakika alacak bicimde olusuturun.
"""

def zaman_verisi_al():
    """
    parametre: None
    tip:       None
    örnek:     None
    
    r-return:  Saati ekrana döndür
    r-tip:     String
    r-örnek:   saat: 23,       dakika: 59
    """
    
    pass