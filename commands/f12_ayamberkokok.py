from functions import *
import commands.b05_gambar as b05
def ayamberkokok(users, candi, bahan_bangunan, active_user, running):

    # Jika user yang aktif adalah Roro Jonggrang
    if active_user[1] == "roro_jonggrang":
        
        N = arr_len(candi)-1    # Hitung banyak candi
        if N < 100: # Jika candi kurang dari 100, maka Roro Jonggrang menang
            b05.gambarayam()
            print(f"Jumlah candi: {N} \n")
            print("Selamat, Roro Jonggrang memenangkan permainan! \n")
            print("*Bandung Bondowoso angry noise*")
            print("Roro Jonggrang dikutuk menjadi candi.")
        else:   # Jika candi sudah 100, maka Bandung Bondowoso menang
            b05.gambarayam()
            print(f"Jumlah candi: {N} \n")
            print("Yah, Bandung Bondowoso memenangkan permainan!")

        running[0] = 0  # Ubah running ke 0 untuk menghentikan program

    # Jika tidak ada user yang sedang aktif
    elif active_user[0] == 0:
        print("Silahkan login dahulu sebelum menggunakan perintah tersebut!")
    # Jika user yang sedang aktif bukan Roro Jonggrang
    else:
        print(f"User dengan username {active_user[0]} tidak memiliki akses terhadap perintah ayamberkokok.")
    
    return users, candi, bahan_bangunan
