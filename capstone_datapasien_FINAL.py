"""
PROGRAM UNTUK CAPSTONE MODUL 1
Study case : Data Pasien Rumah Sakit
Untuk mengetahui data pasien berdasarkan ID dan status rawat pasien
BY ANASTIARA ADINA RESTU - JCDS 1702 002 
CAMPUS BSD
MAY 2022
"""

data_pasien = [{
                'ID':'19A',
                'nama':'Miranti',
                'tanggalLahir':'27 Mei 1998',
                'jenisKelamin':'P',
                'status':'Rawat Jalan'},
                {
                'ID':'19B',
                'nama':'Oppa',
                'tanggalLahir':'20 Oktober 1989',
                'jenisKelamin':'L',
                'status':'Rawat Inap'},
                {
                    'ID':'19C',
                    'nama':'Wilma',
                    'tanggalLahir':'2 Maret 2020',
                    'jenisKelamin':'P',
                    'status':'Rawat Jalan'}]
# data_pasien = []

# ========= Function untuk menu 1 ==============
def display_patient():
# untuk menampilkan Submenu menu Menampilkan data pasien
    print(''' 
    ******Menampilkan Data Pasien******

    1. Menampilkan semua data pasien
    2. Menampilkan data pasien tertentu berdasarkan ID
    3. Menampilkan data pasien tertentu berdasarkan Status Rawat
    4. Kembali ke Menu Utama
    ''')
    submenuChoice=int(input('Masukan pilihan submenu: '))
    if submenuChoice == 1:
        display_patient1()
    elif submenuChoice == 2:
        display_patient2()
    elif submenuChoice == 3:
        display_patient3()
    elif submenuChoice == 4:
        app_dataPasien()
    else:
        display_patient()

def display_patient1():
    if data_pasien != []:
        print('{:<9} | {:<16} | {:<16} | {:<16} | {:<17}'.format('ID','Nama','Tanggal Lahir','Jenis Kelamin','Status'))
        for i in range(len(data_pasien)):
            print('{:<9} | {:<16} | {:<16} | {:<16} | {:<17}'.format(data_pasien[i]['ID'],data_pasien[i]['nama'],data_pasien[i]['tanggalLahir'],data_pasien[i]['jenisKelamin'],data_pasien[i]['status']))
        display_patient()
    elif data_pasien == []:
        print('Tidak ada data')
        display_patient()

def display_patient2():
    if data_pasien == []:
        print('Tidak ada data')
        display_patient()
    elif data_pasien != []: 
        ID_masukan = input('Masukkan ID: ')
        tidak_ada = 0
        for i in range(len(data_pasien)):
            if data_pasien[i]['ID'] == ID_masukan:        
                print('{:<9} | {:<16} | {:<16} | {:<16} | {:<17}'.format('ID','Nama','Tanggal Lahir','Jenis Kelamin','Status'))
                print('{:<9} | {:<16} | {:<16} | {:<16} | {:<17}'.format(data_pasien[i]['ID'],data_pasien[i]['nama'],data_pasien[i]['tanggalLahir'],data_pasien[i]['jenisKelamin'],data_pasien[i]['status']))
                tidak_ada -= tidak_ada
            else:
                tidak_ada += 1
        if tidak_ada  >= len(data_pasien):
            print('Data tidak ditemukan')
        display_patient()

def display_patient3():
    if data_pasien == []:
        print('Tidak ada data')
        display_patient()
    elif data_pasien != []:
        status_masukan = input('Masukkan status yang ingin dicari [rawat inap/rawat jalan] :')
        tidak_ada = 0
        count = 0
        print('{:<9} | {:<16} | {:<16} | {:<16} | {:<17}'.format('ID','Nama','Tanggal Lahir','Jenis Kelamin','Status'))
        while True:
            for i in range(len(data_pasien)):
                if data_pasien[i]['status'] == status_masukan.title():        
                    print('{:<9} | {:<16} | {:<16} | {:<16} | {:<17}'.format(data_pasien[i]['ID'],data_pasien[i]['nama'],data_pasien[i]['tanggalLahir'],data_pasien[i]['jenisKelamin'],data_pasien[i]['status']))
                    tidak_ada -= tidak_ada
                    count += 1
                else:
                    tidak_ada += 1
            if tidak_ada >= len(data_pasien):
                print('Data tidak ditemukan')
            elif tidak_ada < len(data_pasien):
                print(f'\nJumlah pasien dengan status {status_masukan.title()} ada sebanyak {count} orang')
            break  
        display_patient()

# ======== Function untuk menu 2 =========
def add_patient():
    print('''
    ****** Tambah Data Pasien ******

    1. Tambah Data Pasien
    2. Kembali ke Menu Utama
    '''
    )
    submenuChoice = int(input('Masukkan pilihan submenu: '))

    if submenuChoice == 1:
        add_patient1()
    elif submenuChoice == 2:
        app_dataPasien()
    else:
        add_patient()

def add_patient1():
    tidak_ada = 0
    pasienID_masukan = input('Masukkan ID Pasien: ')
    for i in range(len(data_pasien)):
        if data_pasien[i]['ID'] != pasienID_masukan:
            tidak_ada += 1
        elif data_pasien[i]['ID'] == pasienID_masukan:
            tidak_ada -= tidak_ada
    if tidak_ada < (len(data_pasien)):
        print('Data sudah ada')
        add_patient()
    elif tidak_ada >= (len(data_pasien)):
        # new_ID = pasienID_masukan
        new_nama = input('Masukan nama: ')
        new_TTL = input('Masukkan tanggal lahir (Contoh 19 Oktober 1995): ')
        new_gender = input('Masukkan jenis kelamin [P/L]: ')
        new_status = input('Masukan status [rawat inap/rawat jalan]: ')
        simpan_data = input('Apakah data disimpan? [Ya/Tidak] ')
        if simpan_data == 'Ya':
            print('Data sudah tersimpan')
            data_pasien.append({'ID' :pasienID_masukan,
                            'nama':new_nama,
                            'tanggalLahir':new_TTL,
                            'jenisKelamin':new_gender.capitalize(),
                            'status':new_status.title()})
            add_patient()
        elif simpan_data == 'Tidak':
            add_patient()

# # ============ Function untuk Mengubah Data ================
def change_patient():
    print(''' 
    ******** Ubah Data Pasien *********

    1. Ubah Data
    2. Kembali ke Menu Utama
    ''')
    submenuChoice = int(input('Masukkan pilihan submenu: '))
    if submenuChoice == 1:
        change_patient1()
    elif submenuChoice == 2:
        app_dataPasien()
    else:
        change_patient()

def change_patient1():
    check_ID=input('Masukkan ID yang ingin diubah: ')
    tidak_ada=0
    # print('{:<9} | {:<9} | {:<16} | {:<16} | {:<17}'.format('ID','Nama','Tanggal Lahir','Jenis Kelamin','Status'))
    for i in range(len(data_pasien)):
        if data_pasien[i]['ID'] == check_ID:
            print('{:<9} | {:<16} | {:<16} | {:<16} | {:<17}'.format('ID','Nama','Tanggal Lahir','Jenis Kelamin','Status'))
            print('{:<9} | {:<16} | {:<16} | {:<16} | {:<17}'.format(data_pasien[i]['ID'],data_pasien[i]['nama'],data_pasien[i]['tanggalLahir'],data_pasien[i]['jenisKelamin'],data_pasien[i]['status']))
            pilihan_edit = input('Apakah ingin mengubah data? [Ya/Tidak]')
            if pilihan_edit == 'Ya':
                item_ubah = input('Masukkan kolom yang ingin diubah: ')
                if item_ubah == 'Tanggal Lahir':
                    tanggalLahir_ubah = input('Masukkan tanggal lahir [contoh 19 Oktober 1995] :  ')
                    pilihan_simpan = input('Apakah data akan disimpan? [Ya/Tidak] ')
                    if pilihan_simpan == 'Ya':
                        data_pasien[i]['tanggalLahir'] = tanggalLahir_ubah
                        print('Data telah tersimpan')
                        change_patient()
                    else:
                        change_patient()
                elif item_ubah.title() == 'Nama':
                    nama_ubah = input('Masukkan nama: ')
                    pilihan_simpan = input('Apakah data akan disimpan? [Ya/Tidak] ')
                    if pilihan_simpan == 'Ya':
                        data_pasien[i]['nama'] = nama_ubah
                        print('Data telah tersimpan')
                        change_patient()
                    else:
                        change_patient()
                elif item_ubah == 'Jenis Kelamin':
                    gender_ubah = input('Masukkan jenis kelamin: ')
                    pilihan_simpan = input('Apakah data akan disimpan? [Ya/Tidak] ')
                    if pilihan_simpan == 'Ya':
                        data_pasien[i]['jenisKelamin'] = gender_ubah
                        print('Data telah tersimpan')
                        change_patient()
                    else:
                        change_patient()
                elif item_ubah == 'Status':
                    status_ubah = input('Masukkan status: ')
                    pilihan_simpan = input('Apakah data akan disimpan? [Ya/Tidak]')
                    if pilihan_simpan == 'Ya':
                        data_pasien[i]['status'] = status_ubah
                        print('Data telah tersimpan')
                        change_patient()
                    else:
                        change_patient()
                else:
                    print(f'{item_ubah} tidak tersedia. Silahkan masukkan ID kembali.')
                    change_patient1()
            elif pilihan_edit == 'Tidak':
                change_patient()
        elif data_pasien[i]['ID'] != check_ID:
            tidak_ada += 1
    if tidak_ada >= len(data_pasien):
        print('Data Tidak Tersedia')
        change_patient()

# ============ Function untuk Menghapus Data ===============
def hapus_patient():
    print('''
     ******** Hapus Data Pasien *********

    1. Hapus Data
    2. Kembali ke Menu Utama
    ''')
    submenuChoice=int(input('Masukkan pilihan submenu: '))
    if submenuChoice == 1:
        hapus_patient1()
    elif submenuChoice == 2:
        app_dataPasien()
    else:
        hapus_patient()
        
def hapus_patient1():
    print('{:<9} | {:<16} | {:<16} | {:<16} | {:<17}'.format('ID','Nama','Tanggal Lahir','Jenis Kelamin','Status'))
    for i in range(len(data_pasien)):
        print('{:<9} | {:<16} | {:<16} | {:<16} | {:<17}'.format(data_pasien[i]['ID'],data_pasien[i]['nama'],data_pasien[i]['tanggalLahir'],data_pasien[i]['jenisKelamin'],data_pasien[i]['status']))
    delete_ID=input('Masukkan ID yang ingin dihapus: ')
    tidak_ada = 0
    for i in range(len(data_pasien)):
        if data_pasien[i]['ID'] == delete_ID:
            pilihan_submenu = input('Apakah yakin ingin menghapus? [Ya/Tidak] ')
            if pilihan_submenu == 'Ya':    
                data_pasien.pop(i)
                tidak_ada -= tidak_ada
            elif pilihan_submenu == 'Tidak':
                hapus_patient()
            break
        else:
            tidak_ada += 1
    if tidak_ada >= len(data_pasien):
        print('Data yang anda cari tidak tersedia')
        hapus_patient()
    elif tidak_ada < len(data_pasien):
        print('Data telah terhapus')
        hapus_patient()

# ================== Function untuk Menu Utama ==========================
def app_dataPasien():
    while True:
        print('''
        Selamat datang di Aplikasi PasienKu RS Selamat Sentosa!

        Menu Pilihan:
        1. Menampilkan Data Pasien
        2. Menambahkan Data Pasien
        3. Mengubah Data Pasien
        4. Menghapus Data Pasien
        5. Keluar Program
        ''')
        choiceMenu=int(input('Masukkan menu pilihan: '))
        if choiceMenu == 1:
            display_patient()
        elif choiceMenu == 2:
            add_patient()
        elif choiceMenu == 3:
            change_patient()    
        elif choiceMenu == 4:
            hapus_patient()
        elif choiceMenu == 5:
            print('Terima kasih telah menggunakan Aplikasi PasienKu!')
            quit()
        else:
            print('Pilihan yang anda masukkan salah')
app_dataPasien()