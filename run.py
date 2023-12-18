from functions import *
import commands.f01_login as f01
import commands.f02_logout as f02
import commands.f03_summonjin as f03
import commands.f04_hapusjin as f04
import commands.f05_ubahjin as f05
import commands.f06_bangun as f06
import commands.f07_kumpul as f07
import commands.f08_batchkumpulbangun as f08
import commands.f09_laporanjin as f09
import commands.f10_laporancandi as f10
import commands.f11_hancurkancandi as f11
import commands.f12_ayamberkokok as f12
import commands.f13_load as f13
import commands.f14_save as f14
import commands.f15_help as f15
import commands.f16_exit as f16
import commands.b04_undo as b04

def run(command, users, candi, bahan_bangunan, active_user, running, trash):
   
   # Menampilkan list user
   if command == "listuser":
      N = arr_len(users)
      for i in range(1,N):
            print(users[i])

   # Menampilkan list bahan
   elif command == "listbahan":
      N = arr_len(bahan_bangunan)
      for i in range(1,N):
            print(bahan_bangunan[i])

   # Menampilkan list candi
   elif command == "listcandi":
      N = arr_len(candi)
      for i in range(1,N):
            print(candi[i])

   # f01 Login
   elif command == "login":
      users, candi, bahan_bangunan = f01.login(users, candi, bahan_bangunan, active_user)
      
   # f02 Logout
   elif command == "logout":
      users, candi, bahan_bangunan = f02.logout(users, candi, bahan_bangunan, active_user)
   
   # f03 Summon Jin   
   elif command == "summonjin":
      users, candi, bahan_bangunan = f03.summonjin(users, candi, bahan_bangunan, active_user)
      
   # f04 Hapus Jin
   elif command == "hapusjin":
      users, candi, bahan_bangunan = f04.hapusjin(users, candi, bahan_bangunan, active_user, trash)

   # f05 Ubah Jin
   elif command == "ubahjin":
      users, candi, bahan_bangunan = f05.ubahjin(users, candi, bahan_bangunan, active_user)

   # f06 Bangun
   elif command == "bangun":
      users, candi, bahan_bangunan = f06.bangun(users, candi, bahan_bangunan, active_user)

   # f07 Kumpul
   elif command == "kumpul":
      users, candi, bahan_bangunan = f07.kumpul(users, candi, bahan_bangunan, active_user)

   # f08 Batch Kumpul
   elif command == "batchkumpul":
      users, candi, bahan_bangunan = f08.batchkumpul(users, candi, bahan_bangunan, active_user)
   
   # f08 Batch Bangun
   elif command == "batchbangun":
      users, candi, bahan_bangunan = f08.batchbangun(users, candi, bahan_bangunan, active_user)
   
   # f09 Laporan Jin
   elif command == "laporanjin":
      users ,candi, bahan_bangunan = f09.laporanjin(users ,candi, bahan_bangunan, active_user)

   # f10 Laporan Candi
   elif command == "laporancandi":
      users, candi, bahan_bangunan = f10.laporancandi(users, candi, bahan_bangunan, active_user)

   # f11 Hancurkan Candi
   elif command == "hancurkancandi":
      users, candi, bahan_bangunan = f11.hancurkan(users, candi, bahan_bangunan, active_user)
      
   # f12 Ayam Berkokok
   elif command == "ayamberkokok":
      users, candi, bahan_bangunan = f12.ayamberkokok(users, candi, bahan_bangunan, active_user, running)

   # f14 Save
   elif command == "save":
      users, candi, bahan_bangunan, trash = f14.save(users, candi, bahan_bangunan, trash)

   # f15 Help
   elif command == "help":
      f15.help(active_user)

   # f16 Exit
   elif command == "exit":
      users, candi, bahan_bangunan, running, trash = f16.exit(users, candi, bahan_bangunan, running, trash)

   elif command == "undo":
      users, candi, bahan_bangunan = b04.undo(users, candi, bahan_bangunan, active_user, trash)

   # Command tidak tersedia
   else:
      print(f"Command \"{command}\" tidak tersedia.")
      print("Masukkan command “help” untuk daftar command yang dapat kamu panggil.")
   
   return users, candi, bahan_bangunan