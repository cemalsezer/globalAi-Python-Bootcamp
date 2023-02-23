""" 
Kullanıcıdan 1 ile 10 sayısı arasında tahmin girmesini istiyoruz.
Girilen tahminlere göre puanlama ve hak hesaplaması yaparak kullanıcıya sonuçlarını gösteriyoruz.

- Rastgele sayı oluşturmak için random metodunu dahil ettim.
"""

import random

rndNumber = random.randrange(1,10)
hak=5
puan=100
sayac=0


while hak > 0:
    ansNumber = int(input("Tahmininizi giriniz(1-10): "))
    hak-=1
    sayac+=1
    #puan-=20
    if ansNumber > rndNumber:
        print("Aşağı")
    elif ansNumber < rndNumber:
        print("Yukarı")
    else:
        #puan+=20
        print(f"Doğru bildiniz cevap: {rndNumber}, Kalan Hakkınız: {hak}, Puanınız: {puan-20*(sayac-1)}")
        break
    if hak <= 0:
        print(f"Hakkınızı bitirdiniz, Doğru cevap: {rndNumber} olacaktı, Puanınız: {puan}")
        
            