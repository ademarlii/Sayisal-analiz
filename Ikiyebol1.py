#fonksiyona degerleri göndererek işarte

def f(x):
    return x ** 3 - 2 * x ** 2 - 5


# Başlangıç aralığı
a = 2
b = 4
# İterasyon sayısı
iterasyon = 4

# İterasyonlar
for i in range(iterasyon):
    ort = (a + b) / 2
    f_ort = f(ort)


    if f(a) * f_ort < 0:
        b = ort
    else:
        a = ort

# Bulunan kök
print("Bulunan kök:", x_ort)
