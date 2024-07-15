#Projek to-do-list
import sys

print("Selamat datang di To-Do List")
print("Apakah ada yang ingin anda lakukan hari ini : ")
ulang=input()
simpan=[]

def menu():
    print('\nPilih salah satu dari berikut: ')
    print('1. Input To-Do list')
    print('2. Hapus To-Do list')
    print('3. Lihat To-Do list')
    print('4. Ubah To-Do list')
    print('5. Akhiri program')

   
def Masuk():
    todo=input()
    simpan.append(todo)
    
def hapus():
    for i in enumerate(simpan,start=1):
         print(i)
    
    try:
        hapus=int(input('Pilih no yang ingin di hapus : '))
        index=int(hapus-1)
        if 0 <= index < len(simpan):
            del simpan[index]
        else:
            print('Nomor tidak valid')
    except ValueError:
        print("Masukkan angka yang valid.")
            
def lihat():
    if simpan:
        for i in enumerate(simpan,start=1):
                print(i)
        else:
            print('Tidak ada To-Do list hari ini')

def ubah():
     for i in enumerate(simpan,start=1):
                print(i)
     print('Pilih To-Do yang ingin diubah:')
     ubah=input()
     index = int(ubah)-1
     if index<len(simpan):
            print('Masukan To-Do yang baru: ')
            baru=input('')
            simpan[index]=baru

def akhiri():
    print("Program selesai. Terima kasih!")
    sys.exit()


def main():
    menu()
    pilih=input("Masukkan pilihan:")
    if pilih=='1':
        Masuk()
    elif pilih=='2':
        hapus()
    elif pilih=='3':
        lihat()
    elif pilih=='4':
        ubah()
    elif pilih=='5':
        akhiri()
    else:
        print('Pilih 1 - 5')
  
        
while ulang:
    main()


    

    
    
    
