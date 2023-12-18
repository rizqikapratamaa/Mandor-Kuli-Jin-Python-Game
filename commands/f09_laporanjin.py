from functions import *


def laporanjin(users, candi, bahan_bangunan, active_user):    #qika
    if active_user[1] == "bandung_bondowoso":
        nama_pembuat = []
        jumlah_pembuatan = []
        pengumpul = 0
        pembangun = 0
        
        for i in range(arr_len(users)):
            if users[i][2] == "Pengumpul":
                pengumpul += 1
            if users[i][2] == "Pembangun":
                pembangun += 1

        for i in range(1, arr_len(candi)):
            pembuat = candi[i][1]
            found = False
            for j in range(arr_len(nama_pembuat)):
                if nama_pembuat[j] == pembuat:
                    found = True
                    jumlah_pembuatan[j] += 1
                    break
            if not found:
                nama_pembuat = konso(nama_pembuat, pembuat)
                jumlah_pembuatan = konso(jumlah_pembuatan, 1)

        # mencari pembuat dengan pembuatan terbanyak
        pembuat_terbanyak = ''
        jumlah_pembuatan_terbanyak = 0  # inisialisasi dengan nilai nol

        for i in range(arr_len(nama_pembuat)):
            if jumlah_pembuatan[i] > jumlah_pembuatan_terbanyak:
                jumlah_pembuatan_terbanyak = jumlah_pembuatan[i]
                pembuat_terbanyak = nama_pembuat[i]

        # mengecek apakah ada lebih dari satu pembuat dengan pembuatan terbanyak
        jumlah_terbanyak_sama = 0
        for i in range(arr_len(nama_pembuat)):
            if jumlah_pembuatan[i] == jumlah_pembuatan_terbanyak:
                jumlah_terbanyak_sama += 1
                
        if jumlah_terbanyak_sama > 1:
            nama_pembuat_terbanyak = []
            for i in range(len(nama_pembuat)):
                if jumlah_pembuatan[i] == jumlah_pembuatan_terbanyak:
                    nama_pembuat_terbanyak = konso(nama_pembuat_terbanyak, nama_pembuat[i])
            pembuat_terbanyak = sorting_arr_leks(nama_pembuat_terbanyak)[0]

        # mencari pembuat dengan pembuatan terkecil
        pembuat_terkecil = ''
        jumlah_pembuatan_terkecil = arr_len(candi) - 1  # inisialisasi dengan nilai maksimal

        for i in range(arr_len(nama_pembuat)):
            if jumlah_pembuatan[i] < jumlah_pembuatan_terkecil:
                jumlah_pembuatan_terkecil = jumlah_pembuatan[i]
                pembuat_terkecil = nama_pembuat[i]

        # mengecek apakah ada lebih dari satu pembuat dengan pembuatan terkecil
        jumlah_terkecil_sama = 0
        for i in range(arr_len(nama_pembuat)):
            if jumlah_pembuatan[i] == jumlah_pembuatan_terkecil:
                jumlah_terkecil_sama += 1

        if jumlah_terkecil_sama > 1:
            nama_pembuat_terkecil = []
            for i in range(len(nama_pembuat)):
                if jumlah_pembuatan[i] == jumlah_pembuatan_terkecil:
                    nama_pembuat_terkecil = konso(nama_pembuat_terkecil, nama_pembuat[i])
            pembuat_terkecil = sorting_arr_leks(nama_pembuat_terkecil)[arr_len(nama_pembuat)-1]

        if arr_len(nama_pembuat) == 0:
            pembuat_terbanyak = "-"
            pembuat_terkecil = "-"
        # elif pembangun == 1:
        #     pembuat_terbanyak = nama_pembuat[0]
        #     pembuat_terkecil = "-"

            

        print(f"Total Jin: {pengumpul + pembangun}")
        print(f"Total Jin Pengumpul: {pengumpul}")
        print(f"Total Jin Pembangun: {pembangun}")
        print(f"Jin Terajin: {pembuat_terbanyak}")
        print(f"Jin Termalas: {pembuat_terkecil}")
        print(f"Jumlah Pasir: {bahan_bangunan[1][2]} unit")
        print(f"Jumlah Air: {bahan_bangunan[3][2]} unit")
        print(f"Jumlah Batu: {bahan_bangunan[2][2]} unit")

    elif active_user[1] == 0:
        print("Silahkan login dahulu sebelum menggunakan perintah tersebut!")
    
    else:
        print(f"User dengan username {active_user[0]} tidak memiliki akses terhadap perintah laporanjin.")
        
    return users, candi, bahan_bangunan
