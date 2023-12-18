# File: main.py
from run import *
import commands.f13_load as data
import commands.f01_login as login
import argparse
import os
import time
os.system("cls")

trash = [[]]
active_user = [0,0] # Untuk menentukan apakah ada user yang sedang login atau tidak
users = [] # Matriks data user
candi = [] # Matriks data candi
bahan_bangunan = [] # Data bahan bangunan
running = [1] # Untuk menghentikan program

# Gunakan metode argparse untuk melakukan load data 
if __name__ == '__main__':
      # Menerima argumen saat menjalankan file python menggunakan argparse
      parser = argparse.ArgumentParser(description='Load data from external data structure')
      parser.add_argument('folder_name', metavar='folder_name', type=str, nargs='?',
                              help='Nama folder yang berisi file penyimpanan')
      args = parser.parse_args()

      if args.folder_name:    # Jika nama folder ditemukan
            # Mendapatkan path absolut dari folder berdasarkan path relatif terhadap direktori script
            folder_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'savefiles', args.folder_name)
            users, candi, bahan_bangunan, running = data.load_data(folder_path ,args.folder_name, users, candi, bahan_bangunan, running)
            time.sleep(2)
            os.system("cls")
            print("Selamat Datang di Program “Mandor Kuli Jin”")
      else:       # Jika nama folder tidak ditemukan
            print("Tidak ada nama folder yang diberikan!")
            print("Memulai program dengan New Game...")
            # Mengisi users, candi, dan bahan_bangunan menggunakan file
            users = data.load(r"file\user.csv") # Matrix data user
            candi = data.load(r"file\candi.csv") # Matrix data user
            bahan_bangunan = data.load(r"file\bahan_bangunan.csv") # Matrix data user
            time.sleep(2)
            os.system("cls")
            print("Selamat Datang di Program “Mandor Kuli Jin”")

# Menerima masukan
while running[0] != 0:

      command = input(">>> ")

      users,\
      candi,\
      bahan_bagunanrun\
            = run\
                  (command,\
                  users,\
                  candi,\
                  bahan_bangunan,\
                  active_user,\
                  running,\
                  trash)

      print("\n", end="")
