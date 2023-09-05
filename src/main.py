import fruit_market as fm

#init database
db = [
    ["index","nama","stock", "harga" ],
    [0, "Apel", 20, 10000],
    [1, "Jeruk", 15, 15000],
    [2, "Anggur", 25, 20000],
]

#define prompt display
PROMPT = '''
Selamat datang di pasar buah

List menu:
1. Menampilkan daftar buah
2. Menampilkan buah
3. Menghapus buah
4. Membeli buah
5. Exit
'''
#define main menu
def main():
    """_summary_
    """   
    while True:
        print(PROMPT) 
        menu = int(input('> Silahkan pilih menu: '))

        if menu == 1:
            fm.show(db)
        elif menu == 2:
            fm.add(db)
        elif menu == 3:
            fm.delete(db)
        elif menu == 4:
            fm.buy(db)
        elif menu == 5:
            break
        else:
            print("Menu tidak tersedia")

if __name__ == '__main__':
        main()

# # Hitung harga per buah
# totalPriceApel, nApel = input_fruit ('apel', stockApel, priceApel)
# totalPriceJeruk, nJeruk = input_fruit ('jeruk', stockJeruk, priceJeruk)
# totalPriceAnggur, nAnggur = input_fruit ('anggur', stockAnggur, priceAnggur)

# # Hitung harga total buah
# priceTotal = totalPriceAnggur + totalPriceApel + totalPriceJeruk

# # show
# print (
#     f'''
# Detail Belanja

# Apel : {nApel} x {priceApel} = Rp {totalPriceApel}
# Jeruk : {nJeruk} x {priceJeruk} = Rp {totalPriceJeruk}
# Anggur : {nAnggur} x {priceAnggur} = Rp {totalPriceAnggur}
# Total : Rp {priceTotal}
# '''
# )

# while True:
#     npembayaran = (int(input('Silahkan masukan nominal uang untuk membayar: ')))
#     selisihpembayaran = npembayaran - priceTotal
#     if npembayaran < priceTotal:
#         print (f'Maaf jumlah kekurangan yang anda harus bayar adalah: Rp. {selisihpembayaran}')
#     elif npembayaran > priceTotal:
#         print(f'Terimakasih, berikut jumlah kembaliannya:Rp. {selisihpembayaran}')
#         break
#     else:
#         npembayaran == selisihpembayaran
#         print(f'Terimakasih')
#         break
