tahun = int(input('Masukkan tahun : '))

habis_dibagi_400 = tahun % 400 == 0
habis_dibagi_100 = tahun % 100 == 0
habis_dibagi_4 = tahun % 4 == 0

if habis_dibagi_400:
  print(f'Tahun {tahun} merupakan TAHUNN KABISAT')
elif habis_dibagi_4 and not habis_dibagi_100:
  print(f'Tahun {tahun} merupakan TAHUNN KABISAT')
else:
  print(f'Tahun {tahun} bukan merupakan TAHUN KABISAT')