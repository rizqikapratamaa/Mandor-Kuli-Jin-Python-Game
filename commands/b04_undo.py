from functions import *

def undo(users, candi, bahan_bangunan, active_user, trash):

    if active_user[1] == "bandung_bondowoso":

        if arr_len(trash[0]) == 0:

            print("Gagal melakukan undo!")

        else:

            print("Undo berhasil!")

            newTrash = [trash[0][i+1] for i in range(arr_len(trash[0])-1)]

            users = trash[0][0][0]
            candi = trash[0][0][1]

            trash[0] = newTrash

    elif active_user[1] == 0:   
        print("Silahkan login dahulu sebelum menggunakan perintah tersebut!")
    
    else:
        print(f"User dengan username {active_user[0]} tidak memiliki akses terhadap perintah ubahjin.")
        
    return users, candi, bahan_bangunan