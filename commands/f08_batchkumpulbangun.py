from commands.f06_bangun import *
import commands.b01_randomgenerator as b01
from functions import *
import commands.b05_gambar as b05
# Fungsi batchkumpul
def batchkumpul(users,candi, bahan_bangunan, active_user):

    # Jika user yang sedang aktif adalah Bandung Bondowoso
    if active_user[1] == "bandung_bondowoso":
    
        pengumpul = 0   # Untuk menghitung jumlah jin pengumpul
        for i in range (arr_len(users)):    # Hitung jumlah jin pengumpul
            if users[i][2] == "Pengumpul":
                pengumpul += 1
        
        # Untuk menghitung bahan
        pasir_total = 0
        batu_total = 0
        air_total = 0

        if pengumpul == 0:  # Jika tidak ada jin pengumpul, maka pengumpulan gagal
            print("Kumpul gagal. Anda tidak punya jin pengumpul. Silahkan summon terlebih dahulu.")
        else: # Jika ada jin pengumpul
            # Lakukan pengulangan pengumpulan sebanyak jumlah jin, dan setiap pengumpulan deberi nilai random
            for i in range (pengumpul):
                pasir = b01.generate_angka_random(0)
                bahan_bangunan[1][2] = str(int(bahan_bangunan[1][2]) + pasir)
                pasir_total += pasir
                
                batu = b01.generate_angka_random(0)
                bahan_bangunan[2][2] = str(int(bahan_bangunan[2][2]) + batu)
                batu_total += batu
                
                air = b01.generate_angka_random(0)
                bahan_bangunan[3][2] = str(int(bahan_bangunan[3][2]) + air)
                air_total += air
                
            print(f"Mengerahkan {pengumpul} jin untuk mengumpulkan bahan.")
            print(f"Jin menemukan total {pasir_total} pasir, {batu_total} batu, dan {air_total} air.")
    
    # Jika tidak ada user yang sedang aktif
    elif active_user[1] == 0:
        print("Silahkan login dahulu sebelum menggunakan perintah tersebut!")
    
    # Jika user yang aktif bukan Bandung Bondowoso
    else:
        print(f"User dengan username {active_user[0]} tidak memiliki akses terhadap perintah batchbangun.")
        
    return users, candi, bahan_bangunan

# Fungsi batchbangun
def batchbangun(users, candi, bahan, active_user):
    if active_user[1] == "bandung_bondowoso":
        
        NPembangun = 0
        ListPembangun = []

        for i in range(3, arr_len(users)):
            if users[i][2] == "Pembangun":

                NPembangun += 1
                ListPembangun = konso(ListPembangun, users[i][0])
            

        if ListPembangun == []:

            print("Bangun gagal. Anda tidak punya jin pembangun. Silahkan summon terlebih dahulu.")
            return users, candi, bahan


        ListBahan = []

        sumPasir = 0
        sumBatu = 0
        sumAir = 0
        
        for i in range(NPembangun):

            pasir = b01.generate_angka_random(1)
            batu = b01.generate_angka_random(1)
            air = b01.generate_angka_random(1)

            sumPasir += pasir
            sumBatu += batu
            sumAir += air

            ListBahan = konso(ListBahan, [pasir, batu, air])
        
        print(f"Mengerahkan {NPembangun} jin untuk membangun candi dengan total bahan {sumPasir} pasir, {sumBatu} batu, dan {sumAir} air.")
        

        if not(isCukup(sumPasir, sumBatu, sumAir, bahan)):

            pasirKurang = sumPasir - int(bahan[1][2])
            if pasirKurang < 0:
                pasirKurang = 0

            batuKurang = sumBatu - int(bahan[2][2])
            if batuKurang < 0:
                batuKurang = 0

            airKurang = sumAir - int(bahan[3][2])
            if airKurang < 0:
                airKurang = 0

            print(f"Bangun gagal. Kurang {pasirKurang} pasir, {batuKurang} batu, dan {airKurang} air.")

            return users, candi, bahan

        
        for i in range(NPembangun):

            id = 0 

            for j in range(1,arr_len(candi)):
                if id + 1 == int(candi[j][0]):
                    id +=1
                else:
                    break
            id += 1

            if arr_len(candi) < 101:
                candi = konso(candi, [str(id), ListPembangun[i], str(ListBahan[i][0]), str(ListBahan[i][1]), str(ListBahan[i][2])])
                candi = sortCandi(candi)
            
        bahan[1][2] = int(bahan[1][2]) - sumPasir
        bahan[2][2] = int(bahan[2][2]) - sumBatu
        bahan[3][2] = int(bahan[3][2]) - sumAir
        b05.gambarcandi()
        print(f"Jin berhasil membangun total {NPembangun} candi.")
        print(f"Sisa candi yang perlu di bangun: {100-(arr_len(candi)-1)}")
    elif active_user[1] == 0:
        print("Silahkan login dahulu sebelum menggunakan perintah tersebut!")
    
    else:
        print(f"User dengan username {active_user[0]} tidak memiliki akses terhadap perintah batchbangun.")
        
    return users, candi, bahan