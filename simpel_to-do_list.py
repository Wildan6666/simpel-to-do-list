#Projek to-do-list
print("Selamat datang di To-Do List")
print("Apakah ada yang ingin anda lakukan hari ini : Y")
ulang=input()
simpan=[]
while ulang=='Y':
    print('\nPilih salah satu dari berikut: ')
    print('1. Input To-Do list')
    print('2. Hapus To-Do list')
    print('3. Lihat To-Do list')
    print('4. Ubah To-Do list')
    print('5. Akhiri program')

    pilih=input("Masukkan pilihan:")

    if pilih=='1':
        print('\nMasukkan To-Do list: ')
        todo=input()
        simpan.append(todo)
        
    elif pilih=='2':
        print('Yang ingin anda hapus:\n1.Hapus awal \n2.Hapus akhir \n3.Hapus semuanya ')
        hapus=input()
        if hapus=='1':
            del simpan[0]
        elif hapus=='2':
            del simpan[-1]
        elif hapus=='3':
            simpan.clear()
        else:
            print('PILIH 1 - 3')
    
    elif pilih=='3':
        if simpan:
            for i in enumerate(simpan,start=1):
                print(i)
        else:
            print('Tidak ada To-Do list hari ini')
            
    elif pilih=='4':
        for i in enumerate(simpan,start=1):
                print(i)
        print('Pilih To-Do yang ingin diubah:')
        ubah=input()
        index = int(ubah)-1
        if index<len(simpan):
            print('Masukan To-Do yang baru: ')
            baru=input('')
            simpan[index]=baru
            
    elif pilih=='5':
        break
    else:
        print('PILIH 1 - 5')


        
            
    
    
    
    
