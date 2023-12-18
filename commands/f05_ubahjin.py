from functions import *
def ubahjin(users, candi, bahan_bangunan, active_user) :

    if active_user[1] == "bandung_bondowoso":

        username_jin = input("Masukkan username jin: ")
        found = False
        N = arr_len(users)

        for i in range (N) :
            if username_jin == users[i][0] :
                lokasi = i
                found = True

        if found == False :
            print ("Tidak ada jin dengan username tersebut.")

        else :
            if users[lokasi][2] == "Pengumpul" :
                determine = input("Jin ini bertipe “Pengumpul”. Yakin ingin mengubah ke tipe “Pembangun” (Y/N)? ")
                while True :
                    if determine == "Y" or determine == "y" :
                        users[lokasi][2] = "Pembangun"
                        print("Jin telah berhasil diubah.")
                        break
                    elif determine == "N" or determine == "n" :
                        print("Jin tidak jadi diubah.")
                        break
                    else :
                        print(f"Hanya menerima input Y/N. Silahkan ulangi.")
                        determine = input("Jin ini bertipe “Pengumpul”. Yakin ingin mengubah ke tipe “Pembangun” (Y/N)? ")
            else :
                determine = input("Jin ini bertipe “Pembangun”. Yakin ingin mengubah ke tipe “Pengumpul” (Y/N)? ")
                while True :
                    if determine == "Y" or determine == "y" :
                        users[lokasi][2] = "Pengumpul"
                        print("Jin telah berhasil diubah.")
                        break
                    elif determine == "N" or determine == "n" :
                        print("Jin tidak jadi diubah.")
                        break
                    else :
                        print(f"Hanya menerima input Y/N. Silahkan ulangi.")
                        determine = input("Jin ini bertipe “Pengumpul”. Yakin ingin mengubah ke tipe “Pembangun” (Y/N)? ")
                    

    elif active_user[1] == 0:
        print("Silahkan login dahulu sebelum menggunakan perintah tersebut!")
    
    else:
        print(f"User dengan username {active_user[0]} tidak memiliki akses terhadap perintah ubahjin.")
        
    return users, candi, bahan_bangunan

