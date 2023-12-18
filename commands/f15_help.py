def help(active_user):
    if active_user[1] == 0:
        print('''=========== HELP ===========
    1. login
    Untuk masuk menggunakan akun
    2. load
    Untuk memuat file eksternal ke dalam permainan
    3. exit
    Untuk keluar dari permainan
    4. help
    Untuk menampilkan command yang dapat dipanggil
    ============================''')
    
    elif active_user[1] == "bandung_bondowoso":
        print('''=========== HELP ===========
    1. logout
    Untuk keluar dari akun yang digunakan sekarang
    2. summonjin
    Untuk memanggil jin dari dunia lain
    3. hapusjin
    Untuk menghapus jin yang telah dipanggil
    4. ubahjin
    Untuk mengubah tipe jin yang telah dipanggil
    5. batchkumpul
    Untuk mengerahkan seluruh pasukan jin pengumpul
    6. batchbangun
    Untuk mengerahkan seluruh pasukan jin pengumpul
    7. laporanjin
    Untuk mengambil laporan kinerja jin
    8. laporancandi
    Untuk mengambil laporan progress pembangunan candi
    9. exit
    Untuk keluar dari permainan
    10. help
    Untuk menampilkan command yang dapat dipanggil
    ============================''')

    elif active_user[1] == "roro_jonggrang":
        print('''=========== HELP ===========
    1. logout
    Untuk keluar dari akun yang digunakan sekarang
    2. hancurkancandi
    Untuk menghancurkan candi
    3. ayamberkokok
    Untuk memalsukan ayam berkokok di pagi hari
    4. exit
    Untuk keluar dari permainan
    5. help
    Untuk menampilkan command yang dapat dipanggil
    ============================''')

    elif active_user[1] == "Pengumpul":
        print('''=========== HELP ===========
    1. logout
    Untuk keluar dari akun yang digunakan sekarang
    2. kumpul
    Untuk mengumpulkan bahan-bahan yang diperlukan untuk membangun candi
    3. exit
    Untuk keluar dari permainan
    4. help
    Untuk menampilkan command yang dapat dipanggil
    ============================''')

    else: # role[1] == "Pembangun"
        print('''=========== HELP ===========
    1. logout
    Untuk keluar dari akun yang digunakan sekarang
    2. bangun
    Untuk membangun candi
    3. exit
    Untuk keluar dari permainan
    4. help
    Untuk menampilkan command yang dapat dipanggil
    ============================''')