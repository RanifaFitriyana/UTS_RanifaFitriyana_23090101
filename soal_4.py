berat_badan = int(input("Masukkan Berat Badan (Kg) : "))
tinggi_badan = int(input("Masukkan Tinggi Badan (M)) : "))

print(f'Berat Badan : {berat_badan}')
print(f'Tinggi Badan : {tinggi_badan}')

nilai_bmi = berat_badan / (tinggi_badan ** 2)

if nilai_bmi < 18.5:
    print(f'Berat Badan Kurang')
elif 18.5 <= nilai_bmi < 24.9:
    print(f'Berat Badan Normal')
elif 25 <= nilai_bmi < 29.9:
    print(f'Kelebihan Berat Badan')
else:
    print(f'Obesitas')

print(f'Nilai BMI Anda : {nilai_bmi}')



