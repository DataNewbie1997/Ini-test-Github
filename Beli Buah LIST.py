print('Selamat datang di pasar buah')
print('List Menu:','\n',
'1. Menampilkan daftar buah','\n',
'2. Menambah buah','\n',
'3. Menghapus buah','\n',
'4. Membeli buah','\n',
'5. Exit program')
pilihan = int(input('Masukkan angka menu yang ingin dijalankan:'))

stock = [20,15,25]
harga = [10000,15000,20000]
jenis = ['Apel','Jeruk','Anggur']
index = []
for items in range (0,11):
    index.append(items)    
while pilihan <= 5:
    print('Daftar Buah')
    if pilihan == 1:
        print('Index  | Nama   | Stock| Harga')
        print(index[0],'     |' ,jenis[0],'  |',stock[0],'  |',harga[0])
        print(index[1],'     |' ,jenis[1],' |',stock[1],'  |',harga[1])
        print(index[2],'     |' ,jenis[2],'|',stock[2],'  |',harga[2])
        print('Selamat datang di pasar buah')
        print('List Menu:','\n',
        '1. Menampilkan daftar buah','\n',
        '2. Menambah buah','\n',
        '3. Menghapus buah','\n',
        '4. Membeli buah','\n',
        '5. Exit program')
        pilihan = int(input('Masukkan angka menu yang ingin dijalankan:'))
    elif pilihan == 2:
        jenis.append(str(input('Masukkan nama buah:')))
        stock.append(int(input('Masukkan stock buah:')))
        harga.append(int(input('Masukkan harga buah:')))
        print('Index  | Nama   | Stock| Harga')
        print(index[0],'     |' ,jenis[0],'  |',stock[0],'  |',harga[0])
        print(index[1],'     |' ,jenis[1],' |',stock[1],'  |',harga[1])
        print(index[2],'     |' ,jenis[2],'|',stock[2],'  |',harga[2])
        print(index[3],'     |' ,jenis[3],' |',stock[3],'  |',harga[3])
        print('Selamat datang di pasar buah')
        print('List Menu:','\n',
        '1. Menampilkan daftar buah','\n',
        '2. Menambah buah','\n',
        '3. Menghapus buah','\n',
        '4. Membeli buah','\n',
        '5. Exit program')
        pilihan = int(input('Masukkan angka menu yang ingin dijalankan:'))
    elif pilihan == 3:
        print('Index  | Nama   | Stock| Harga')
        print(index[0],'     |' ,jenis[0],'  |',stock[0],'  |',harga[0])
        print(index[1],'     |' ,jenis[1],' |',stock[1],'  |',harga[1])
        print(index[2],'     |' ,jenis[2],'|',stock[2],'  |',harga[2])
        print(index[3],'     |' ,jenis[3],' |',stock[3],'  |',harga[3]) # INI HARUSNYA TERHAPUS NAMUN KARENA UDH DIBERI  DEL INDEX (LINE 55) KEMBALI NGELOOP SEHINGGA HARUS NGEPRINT LINE 53 INI. PADAHAL SUDAH DIBERI LINE 57
        hapus = (int(input('Masukkan index buah yang ingin dihapus:')))
        del index[hapus] ; del jenis[hapus] ; del stock[hapus] ; del harga[hapus]
        if hapus == 0:
            print(index[0],'     |' ,jenis[0],'  |',stock[0],'  |',harga[0])
            print(index[1],'     |' ,jenis[1],' |',stock[1],'  |',harga[1])
            print(index[2],'     |' ,jenis[2],'|',stock[2],'  |',harga[2])
    
    # elif pilihan == 4:
    #     print('Index  | Nama   | Stock| Harga')
    #     print(index[0],'     |' ,jenis[0],'  |',stock[0],'  |',harga[0])
    #     print(index[1],'     |' ,jenis[1],' |',stock[1],'  |',harga[1])
    #     print(index[2],'     |' ,jenis[2],'|',stock[2],'  |',harga[2])
    # beli = int(input('Masukkan index buah yang ingin dibeli:'))
    # jumlah = int(input('Masukkan jumlah yang ingin dibeli'))
    # if jumlah >= stock:
    #     print('stock tidak cukup, stock tersisa')
    # jumlah = int(input('Masukkan jumlah yang ingin dibeli:'))
    # pilihan += 1