class Kalkulator:
    def pertambahan(self,a,b):
        hasil = a+b
        print('>'*5,"Anda memilih operasi penjumlahan",'<'*5)
        print(f"hasil penjumlahan dari {a}{o}{b} adalah {hasil}\n")
    def pengurangan(self,a,b):
        hasil = a-b
        print('>'*5,"Anda memilih operasi pengurangan",'<'*5)
        print(f"hasil pengurangan dari {a}{o}{b} adalah {hasil}\n")
    def perkalian(self,a,b):
        hasil = a*b
        print('>'*5,"Anda memilih operasi perkalian",'<'*5)
        print(f"hasil perkalian dari {a}{o}{b} adalah {hasil}\n")
    def pembagian(self,a,b):
        if b ==0:
            print(">>>Error!! Tidak bisa dibagi dengan 0")
            print("Silahkan Ulangi\n")
        else:
            print('>'*5,"Anda memilih operasi pembagian",'<'*5)
            hasil = a/b
            print(f"hasil pembagian dari {a}{o}{b} adalah {hasil}\n")
            
cal = Kalkulator()
while True:
    print('-'*50)
    print('<>'*5,"Aplikasi Kalkulator Nabiil",'<>'*5)
    print('-'*50)
    print('-'*50)
    print('<>'*2,"Selamat Datang di Aplikasi Kalkulator",'<>'*2)
    print('-'*50)
    try:
        a = int(input("Masukkan angka pertama: "))
        b = int(input("Masukan angka kedua: "))
        print('-'*50)
        print('<>'*7,"Metode Operasi",'<>'*7)
        print('-'*50)
        print("1.Penjumlahan (+)")
        print("2.Pengurangan (-)")
        print("3.Perkalian (*)")
        print("4.Pembagian (/)")
        print("5.Kembali (5)")
        print("0.Keluar (0)")
        o = str(input("Masukkan Operasi dengan simbol (+ - * /): "))
        if o =='+':
            cal.pertambahan(a,b)
        elif o =='-':
            cal.pengurangan(a,b)
        elif o =='*':
            cal.perkalian(a,b)
        elif o =='/':
            cal.pembagian(a,b)
        elif o =='5':
            print("(Anda telah kembali)\n")
        elif o =='0':
            print("Terima kasih anda telah keluar\n")
            break
        else:
            print("Maaf! Input yang anda masukkan salah")
            print("Silahkan Coba Ulangi\n")
    except:
        print("Error! Input yang anda masukkan harus bertipe integer\n")
        continue
    