#fonksiyona degerleri göndererek işarte

def f(x):
    return x ** 3 - 2 * x ** 2 - 5


# Başlangıç aralığı
a = 2
b = 4
# İterasyon sayısı
max_iter = 4

# İterasyonlar
for i in range(max_iter):
    x_ort = (a + b) / 2
    f_ort = f(x_ort)


    if f(a) * f_ort < 0:
        b = x_ort
    else:
        a = x_ort

# Bulunan kök
print("Bulunan kök:", x_ort)
