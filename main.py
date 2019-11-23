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