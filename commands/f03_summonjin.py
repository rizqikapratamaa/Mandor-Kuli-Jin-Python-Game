from functions import *
import commands.b05_gambar as b05
def summonjin(users, candi, bahan_bangunan, active_user):

    if active_user[1] == "bandung_bondowoso":
            
        if arr_len(users) > 103:

            print("Jumlah jin sudah mencapai batas maksimal!")

        else:
            # variabel 'users' berisi data:

            # kolom ke-
            # 0 : username | 1 : password | 2 : role
            # baris ke-
            # 0 : judul kolom | 1 : data bondowoso | 2 : data roro | 3 dst : data jin

            N = arr_len(users)

            # membuat array yang berisi nama jin
            # in range(3, N) karena data jin pertama kali ada pada baris ke 3
            nama_jin = [users[i][0] for i in range(3, N)]
            
            jenis_jin = ["Pengumpul", "Pembangun"] # dengan nomor 0, 1
            nomor_jin = ["1", "2"]

            print("Jenis jin yang dapat dipanggil:")
            print("  (1) Pengumpul - Bertugas mengumpulkan bahan bangunan")
            print("  (2) Pembangun - Bertugas membangun candi")


            # INPUT NOMOR JIN (untuk tipe jin/role jin)

            nomor_jin_input = input("\nMasukkan nomor jenis jin yang ingin dipanggil: ") 

            # validasi agar inputan nomor jin sesuai
            while not(isMember(nomor_jin_input, nomor_jin)):
                
                print(f"\nTidak ada jenis jin bernomor \"{nomor_jin_input}\"!")
                nomor_jin_input = input("\nMasukkan nomor jenis jin yang ingin dipanggil: ") 
            
            print(f"\nMemilih jin \"{jenis_jin[int(nomor_jin_input)-1]}\"")


            # INPUT NAMA JIN

            nama_jin_input = input("\nMasukkan username jin: ")
            
            # validasi agar nama jin tidak ada yang sama
            while (isMember(nama_jin_input, nama_jin)):
                
                print(f"Username \"{nama_jin_input}\" sudah diambil!")
                nama_jin_input = input("\nMasukkan username jin: ")


            # INPUT PASSWORD JIN

            password_jin_input = input("Masukkan password jin: ")

            N = str_len(password_jin_input)
            
            # validasi agar password sesuai ketentuan
            while (N < 5 or N > 25):
                
                print("\nPassword panjangnya harus 5-25 karakter!")

                password_jin_input = input("Masukkan password jin: ")

                N = str_len(password_jin_input)
                
            users = konso(users, [nama_jin_input, password_jin_input, jenis_jin[int(nomor_jin_input)-1]])
            b05.gambarjin()
    else:
            print("Kamu tidak memiliki akses untuk command summonjin!")

    return users, candi, bahan_bangunan