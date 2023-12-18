def logout(users, candi, bahan_bangunan, active_user):
    
    if active_user[0] != 0:            # Jika sudah login, maka bisa logout
        print(f"Keluar dari akun dengan username {active_user[0]}")
        active_user[0] = 0
        active_user[1] = 0

    else:       # Jika belum login, maka tidak bisa logout
        print("Logout gagal!")
        print("Anda belum login, silahkan login terlebih dahulu sebelum melakukan logout.")
    
    return users, candi, bahan_bangunan