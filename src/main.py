#init harga
priceApel = 10000
pricejeruk =15000
priceAnggur = 20000
#input jumlah buah
nApel =int(input("input jumlah apel; "))
njeruk =int(input("input jumlah jeruk; "))
nAnggur = int(input("input jumlah anggur; "))

#hitung harga per buah
totalPriceApel = nApel *priceApel
totalPriceJeruk = njeruk *pricejeruk
totalPriceAnggur = nAnggur * priceAnggur

#hitung harga total buah
priceTotal = totalPriceApel + totalPriceJeruk + totalPriceAnggur

#show
print(
    f'''
Detai Belanja

Apel    : {nApel} X {priceApel}
jeruk   : {njeruk} x {pricejeruk}
Anggur  : {nAnggur} x {priceAnggur}
Total   : {priceTotal}
'''
)