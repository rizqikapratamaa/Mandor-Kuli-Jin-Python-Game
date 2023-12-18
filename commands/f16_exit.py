import commands.f14_save as f14
def exit(users, candi, bahan_bangunan, running, trash):
    
    # Terima input dari user dalam bentuk variabel "choice"
    choice = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n)\n")
    while True:
        if choice == "y" or choice == "Y":  # Jika input dari user adalah "Y" atau "y"
            f14.save(users, candi, bahan_bangunan, trash)  # Lakukan save
            running[0] = 0  # Ubah running ke 0 untuk menghentikan program
            break
        elif choice == "n" or choice == "N":    # Jika input dari user adalah "Y" atau "y"
            print("Keluar dari game tanpa melakukan save.")
            running[0] = 0  # Ubah running ke 0 untuk menghentikan program
            break
        else:   # Jika input selain di atas, ulangi sampai user memasukkan input yang sesuai
            print("Input (y/n) untuk melakukan save atau tidak.")
            choice = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n)\n")
    return users, candi, bahan_bangunan, running, trash