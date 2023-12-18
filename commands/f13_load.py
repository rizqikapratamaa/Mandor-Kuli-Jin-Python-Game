from functions import *
import os

def load_data(folder_path, folder_name, users, candi, bahan_bangunan, running):
    # Validasi apakah folder_path ada atau tidak
    if not os.path.exists(folder_path):       # Jika folder tidak ada, langsung hentikan program
        print(f"Folder “{folder_name}” tidak ditemukan.")
        users = [] # Matriks data user
        candi = [] # Matriks data candi
        bahan_bangunan = []
        running[0] = 0
        return users, candi, bahan_bangunan, running
    else:       # Jika folder ada, baca data dari folder tersebut
        # Menjalankan proses load data
        print(f"Data dari folder “{folder_name}” berhasil di-load.")
        print("Loading...")
        # Mengisi users, candi, dan bahan_bangunan menggunakan file
        users = load(os.path.join("savefiles", folder_path, "user.csv")) # Matrix data user
        candi = load(os.path.join("savefiles", folder_path, "candi.csv")) # Matrix data user
        bahan_bangunan = load(os.path.join("savefiles", folder_path, "bahan_bangunan.csv")) # Matrix data user
        running[0] = 1
        return users, candi, bahan_bangunan, running

def load(file_name):
    with open(file_name, 'r') as file:
        return convertToArr(file, ";")