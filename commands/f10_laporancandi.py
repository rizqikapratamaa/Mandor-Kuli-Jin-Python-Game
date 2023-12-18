from functions import *


def laporancandi(users, candi, bahan_bangunan, active_user):
    if active_user[1] == "bandung_bondowoso":
        total_candi = 0
        total_pasir = 0
        total_batu = 0
        total_air = 0
        list_candi = []
        list_harga = []
        for i in range(1, arr_len(candi)):
            total_candi += 1
            
        for i in range(1,arr_len(candi)):
            total_pasir += int(candi[i][2])
            total_batu += int(candi[i][3])
            total_air += int(candi[i][4])
        
        def hitungharga(pasir, batu, air):
            return pasir*10000 + batu*15000 + air*7500
        
        for i in range(1, arr_len(candi)):
            list_candi = konso(list_candi, candi[i][0])
            list_harga = konso(list_harga, hitungharga(int(candi[i][2]), int(candi[i][3]), int(candi[i][4])))
            
        id_termahal = 0
        id_temurah = 0
        harga_termahal = 0
        harga_termurah = 9999999
        for i in range(arr_len(list_candi)):
            if harga_termahal < list_harga[i]:
                harga_termahal = list_harga[i]
                id_termahal = list_candi[i]
            if harga_termurah > list_harga[i]:
                harga_termurah = list_harga[i]
                id_temurah = list_candi[i]
            
        if total_candi == 0:
            print(f"Total Candi: {total_candi}")
            print(f"Total Pasir yang digunakan: {total_pasir}")
            print(f"Total Batu yang digunakan: {total_batu}")
            print(f"Total Air yang digunakan: {total_air}")
            print(f"ID Candi Termahal: -")
            print(f"ID Candi Termurah: -")
        else:
            print(f"Total Candi: {total_candi}")
            print(f"Total Pasir yang digunakan: {total_pasir}")
            print(f"Total Batu yang digunakan: {total_batu}")
            print(f"Total Air yang digunakan: {total_air}")
            print(f"ID Candi Termahal: {id_termahal} (Rp. {harga_termahal})")
            print(f"ID Candi Termurah: {id_temurah} (Rp. {harga_termurah})")
    
    elif active_user[1] == 0:
        print("Silahkan login dahulu sebelum menggunakan perintah tersebut!")
    
    else:
        print(f"User dengan username {active_user[0]} tidak memiliki akses terhadap perintah laporancandi.")
    
    return users, candi, bahan_bangunan