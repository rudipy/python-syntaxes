from geometry.segitiga import hitung_luas_segitiga
from geometry.persegi_panjang import hitung_luas_persegipanjang
from geometry_class.segitiga import Segitiga

print('Hello World')

#Menghitung Luas Segitiga
alas = 10
tinggi = 3
luas_segitiga = alas * tinggi
print(luas_segitiga)

#Menggunakan Logika percabangan
if luas_segitiga < 30:
    print('Kecil!')
elif luas_segitiga == 30:
    print('Cukupan')
else:
    print('Besar Banget!')

#Perulangan mengatasi kode seperti ini...
print('1', luas_segitiga)
print('2', luas_segitiga)
print('3', luas_segitiga)
print('4', luas_segitiga)
print('5', luas_segitiga)

#cara singkat
print('dengan for')
for i in range(0, 10):
    print(i+1, luas_segitiga)

#module tahab 1 pembuatan fungsi
print('segitiga1')
alas = 5
tinggi = 15
luas_segitiga = alas * tinggi / 2
print(luas_segitiga)

print('segitiga2')
alas = 3
tinggi = 6
luas_segitiga = alas * tinggi / 2
print(luas_segitiga)

print(hitung_luas_segitiga('Segitiga3', 5, 15))
print(hitung_luas_segitiga('segitiga4', 3, 6))
print(hitung_luas_segitiga('segitiga5', 5, 10))

#module tahap 2 : pembuatan package
print(hitung_luas_persegipanjang('Persegi 1', 10, 5))
print(hitung_luas_persegipanjang('Persegi 2', 10, 10))

#module tahap 3 : pembuatan class
segitiga1 = Segitiga('segitiga 1 adalah class', 50, 3)
print(segitiga1.title)
print(segitiga1.hitung_luas())
segitiga2 = Segitiga('segitiga 2 adalah class', 150, 13)
print(segitiga2.title)
print(segitiga2.hitung_luas())