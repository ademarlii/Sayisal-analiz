# Sayisal-analiz
sayısal analiz ödevleri
import math


x = math.pi / 5



tekterimsonucu = 1

gercekdeger = math.cos(x)

kesmehatasi = (gercekdeger - tekterimsonucu)

print("Hesaplanan Değer:" ,tekterimsonucu)
print("Gercek Değer:", tekterimsonucu)
print("Kesme Hatası:", kesmehatasi)


print("-"*30)



ikiterimsonucu = 1 + 0   #birinci türevi sinüs fonksiyonu devreye girdiği içiçn sonuç sıfır oluyor.

gercekdeger= math.cos(x)

kesmehatasi = (ikiterimsonucu - gercekdeger)

print("Hesaplanan Değeri:" ,ikiterimsonucu)
print("Gerçek Değeri:",gercekdeger)
print("Kesme Hatası:" ,kesmehatasi)
