from multiprocessing import Process
import os
import time


def hesapla_kareler(sayilar):
    for sayi in sayilar:
        time.sleep(0.5)
        print(f"{os.getpid()} PID ile işlem : {sayi} sayının karesi={sayi*sayi}")
    


def hesapla_kupler(sayilar):
    for sayi in sayilar:
        time.sleep(0.5)
        print(f"{os.getpid()} PID ile işlem : {sayi} sayının küpü={sayi**3}")

if __name__== "__main__":

    giris= input("sayıları giriniz:")
    sayilar = [int(sayi)for sayi in giris.split(",")]


    p1= Process(target= hesapla_kareler,args=(sayilar,))
    p2= Process(target=hesapla_kupler,args=(sayilar,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("işlemler tamamlandı:)")
