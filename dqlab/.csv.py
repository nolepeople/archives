#Sekarang kita akan mencoba membaca sebuah file CSV yang telah dihasilkan aplikasi atau program lain. Di Python, hasil pembacaan setiap baris pada file CSV akan dikonversi menjadi list Python.

#Berikut adalah contoh kode untuk membaca file CSV dengan kasus yang sangat sederhana, coba ketik kode di bawah ini pada Code Editor:

import csv

# tentukan lokasi file, nama file, dan inisialisasi csv
f = open('file.csv', 'r')
reader = csv.reader(f)

# membaca baris per baris
for row in reader:
     print (row)

# menutup file csv
f.close()
#Klik Run untuk melihat hasilnya. Bila sudah paham kegunaanya, klik Submit untuk melanjutkan ke course selanjutnya.
