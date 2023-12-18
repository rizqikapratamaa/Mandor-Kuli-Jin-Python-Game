import commands.b01_randomgenerator as b01
import commands.b05_gambar as b05
def kumpul(users, candi, bahan_bangunan, active_user): #Fungsi mengumpulkan bahan bangunan
    
    if active_user[1] == "Pengumpul":
    
        
        pasir = b01.generate_angka_random(0) #mengambil secara random jumlah pasir
        batu = b01.generate_angka_random(0) #mengambil secara random jumlah batu
        air = b01.generate_angka_random(0) #mengambil secara random jumlah air
        bahan_bangunan[1][2] = str(int(bahan_bangunan[1][2]) + pasir) #menambahkan pasir yang diambil ke list bahan bangunan
        bahan_bangunan[2][2] = str(int(bahan_bangunan[2][2]) + batu) #menambahkan batu yang diambil ke list bahan bangunan
        bahan_bangunan[3][2] = str(int(bahan_bangunan[3][2]) + air) #menambahkan air yang diambil ke list bahan bangunan
        b05.gambarbangunan()
        print(f"Jin menemukan {pasir} pasir, {batu} batu, dan {air} air.") #tampilan pada layar jumlah pasir, batu, dan air yang diambil
    
    elif active_user[1] == 0:
        print("Silahkan login dahulu sebelum menggunakan perintah tersebut!")
    
    else:
        print(f"User dengan username {active_user[0]} tidak memiliki akses terhadap perintah kumpul.")
        
    return users, candi, bahan_bangunan


