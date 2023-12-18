import time

# Tentukan nilai awal (seed) dan konstanta LCG
seed = int(time.time())
a = 1103515245
c = 12345
m = 2**31

# Fungsi untuk menghasilkan angka acak antara 0 dan 5
def generate_angka_random(mulai):
    global seed
    seed = (a*seed + c) % m
    if mulai == 0:  # Jika ingin mulai dari 0
        return seed % 6
    else:   # Jika ingin mulai dari 1
        return (seed % 5) + 1