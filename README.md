# Square-and-Cube-Calculation-Multi-Processor-Program

---

# Paralel Kare ve Küp Hesaplama Programı

Bu Python programı, verilen sayıların karelerini ve küplerini hesaplamak için çoklu işlemcileri (paralel işlemleri) kullanır.

## Nasıl Kullanılır

1. `kare_ve_kup_hesapla.py` dosyasını çalıştırın.
2. Program çalıştırıldığında, bir sayı listesi girmeniz istenecektir.
3. Sayıları virgülle ayırarak girin ve Enter tuşuna basın.
4. Program, girilen sayıların karelerini ve küplerini hesaplamak için iki ayrı işlem başlatacaktır.
5. Her işlem bitene kadar bekleyin. Ardından program, sonuçları ekrana yazdıracaktır.

## Örnek Kullanım

```
$ python kare_ve_kup_hesapla.py
sayıları giriniz: 1, 2, 3, 4, 5
```

```
2 PID ile işlem : 1 sayının karesi=1
2 PID ile işlem : 2 sayının karesi=4
2 PID ile işlem : 3 sayının karesi=9
2 PID ile işlem : 4 sayının karesi=16
2 PID ile işlem : 5 sayının karesi=25
2 PID ile işlem : 1 sayının küpü=1
2 PID ile işlem : 2 sayının küpü=8
2 PID ile işlem : 3 sayının küpü=27
2 PID ile işlem : 4 sayının küpü=64
2 PID ile işlem : 5 sayının küpü=125
```

## Geliştirme

Bu program, sadece pozitif tam sayıların karelerini ve küplerini hesaplar. Programı geliştirmek için şu adımları düşünebilirsiniz:

- Kullanıcıdan daha geniş bir sayı aralığı alınmasına izin verin.
- Hesaplama süresini optimize etmek için farklı çoklu işlem tekniklerini araştırın.
- Çalışma zamanı hatalarını ele almak için gerekli hata kontrolünü ekleyin.

## Lisans

Bu program MIT Lisansı altında lisanslanmıştır. Daha fazla bilgi için `LICENSE` dosyasını inceleyin.

---
