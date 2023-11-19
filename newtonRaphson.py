# Başlangıç değeri
xo = 2

# İterasyonlar
for i in range(4):
    fx = 4 * pow(2.71828, -0.5 * xo) - xo
    fturevx = -2 * pow(2.71828, -0.5 * xo) - 1

    xo = xo - (fx / fturevx)

# Bulunan kök
print("Bulunan kök:", xo)
