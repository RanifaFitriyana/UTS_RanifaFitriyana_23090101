jml_barang = int(input("Masukkan jumlah barang : "))
jmlbarang = [1]
for i in range(1, jml_barang + 1):

    barang = float(input("Masukkan Harga Barang Ke-{i} : "))
    jmlbarang.append(barang)

total_brg = sum(jmlbarang)
total_harga = total_brg + jml_barang

print("Total Belanjaan : Rp.",total_harga)
