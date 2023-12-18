import os
from functions import *

def save(users, candi, bahan_bangunan, trash):

    folder = input("Masukkan nama folder: ")
    savefiles_dir = os.path.join(os.path.abspath(os.path.dirname(__file__)), "..", "savefiles")

    def tulisdata(users, candi, bahan_bangunan, new_dir_path):

        with open(fr"{new_dir_path}\user.csv", 'w') as file_users:
            users_str = convertToCSV(users)
            file_users.write(users_str)

        with open(fr"{new_dir_path}\candi.csv", 'w') as file_candi:
            candi_str = convertToCSV(candi)
            file_candi.write(candi_str)

        with open(fr"{new_dir_path}\bahan_bangunan.csv", 'w') as file_bahan_bangunan:
            bahan_bangunan_str = convertToCSV(bahan_bangunan)
            file_bahan_bangunan.write(bahan_bangunan_str)

    if not os.path.exists(savefiles_dir):

        os.makedirs(savefiles_dir)
        new_dir_path = os.path.join(savefiles_dir, folder)

        if not os.path.exists(new_dir_path):
            print(f"Membuat folder save\{folder}...")
            print("Saving...")
            os.makedirs(new_dir_path)
            tulisdata(users, candi, bahan_bangunan, new_dir_path)
            print(f"Berhasil menyimpan data di folder save\{folder}")

        else:
            new_dir_path = os.path.join(savefiles_dir, folder)
            print("Saving...")
            tulisdata(users, candi, bahan_bangunan, new_dir_path)
            print(f"Berhasil menyimpan data di folder save\{folder}")

    else:
        new_dir_path = os.path.join(savefiles_dir, folder)

        if not os.path.exists(new_dir_path):
            os.makedirs(new_dir_path)
            print("Saving...")
            print(f"Membuat folder {folder}")
            tulisdata(users, candi, bahan_bangunan, new_dir_path)
            print(f"Berhasil menyimpan data di folder save\{folder}")

        else:
            new_dir_path = os.path.join(savefiles_dir, folder)
            print("Saving...")
            tulisdata(users, candi, bahan_bangunan, new_dir_path)
            print(f"Berhasil menyimpan data di folder save\{folder}")
            
    trash[0] = []
    return users, candi, bahan_bangunan, trash