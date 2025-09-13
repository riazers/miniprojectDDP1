
#   Mini Project Playlist Lagu
#   Nama Riaz Ramadhan Al Fattah
#   NIM 2509116106
#   Kelas C 
print("=== Playlist Lagu Riaz ===")

print("1. Pop")
print("2. Indie")
print("3. RnB")

# Daftar lagu dalam setiap genre (List)
Pop = ["As It Was - Harry Styles", 
    "About Damn Time - Lizzo", 
    "Bad Habit - Steve Lacy"]
Indie = ["Anti-Hero - Taylor Swift", 
    "Fallen Star - The Neighbourhood", 
    "Made You Look - Meghan Trainor"]
RnB = ["Blinding Lights - The Weeknd", 
    "Twenties - GIVEON", 
    "Peaches - Justin Bieber"]

# Daftar Lagu dalam setiap genre (Tuple) (tidak bisa diubah)
Pop_Bawaan = ("As It Was - Harry Styles", 
    "About Damn Time - Lizzo", 
    "Bad Habit - Steve Lacy")
Indie_Bawaan = ("Anti-Hero - Taylor Swift", 
    "Fallen Star - The Neighbourhood", 
    "Made You Look - Meghan Trainor")
RnB_Bawaan = ("Blinding Lights - The Weeknd", 
    "Twenties - GIVEON", 
    "Peaches - Justin Bieber")

putar = (input(f"Masukkan Genre Playlist Lagu yang Ingin Diputar: "))

while putar != "Pop" and putar != "1" and putar != "Indie" and putar != "2" and putar != "RnB" and putar != "3":
    print("Genre Playlist tidak tersedia, silakan pilih dengan benar.")
    putar = (input(f"Masukkan Genre Playlist Lagu yang Ingin Diputar: "))   
if putar == "Pop" or putar == "1":
    print("Memutar lagu Pop: ", Pop_Bawaan)
    tambah_pop = str(input("Ingin menambah lagu Pop? (Ya/Tidak): "))
    if tambah_pop == "Ya":
        lagu_baru = str(input("Masukkan judul lagu baru: "))
        Pop.append(lagu_baru)
        print("Playlist Pop terbaru: ", Pop)
    hapus_pop = str(input("Ingin menghapus lagu Pop? (Ya/Tidak): "))
    if hapus_pop == "Ya":
        lagu_hapus = str(input("Masukkan judul lagu yang ingin dihapus: "))
        if lagu_hapus in Pop:
            Pop.remove(lagu_hapus)
            print("Playlist Pop terbaru: ", Pop)
        else:
            print("Lagu tidak ditemukan dalam playlist.")
    elif tambah_pop == "Tidak":
        print("Terima kasih. Selamat mendengarkan lagu Pop!")


elif putar == "Indie" or putar == "2":
    print("Memutar lagu Indie: ", Indie_Bawaan)
    tambah_indie = str(input("Ingin menambah lagu Indie? (Ya/Tidak): "))
    if tambah_indie == "Ya":
        lagu_baru = str(input("Masukkan judul lagu baru: "))
        Indie.append(lagu_baru)
        print("Playlist Indie terbaru: ", Indie)
    hapus_indie = str(input("Ingin menghapus lagu Indie? (Ya/Tidak): "))
    if hapus_indie == "Ya":
        lagu_hapus = str(input("Masukkan judul lagu yang ingin dihapus: "))
        if lagu_hapus in Indie:
            Indie.remove(lagu_hapus)
            print("Playlist Indie terbaru: ", Indie)
        else:
            print("Lagu tidak ditemukan dalam playlist.")
    elif tambah_indie == "Tidak":
        print("Terima kasih. Selamat mendengarkan lagu Indie!")


elif putar == "RnB" or putar == "3":
    print("Memutar lagu R&B: ", RnB_Bawaan)
    tambah_RnB = str(input("Ingin menambah lagu R&B? (Ya/Tidak): "))
    if tambah_RnB == "Ya":
        lagu_baru = str(input("Masukkan judul lagu baru: "))
        RnB.append(lagu_baru)
        print("Playlist R&B terbaru: ", RnB)
    hapus_RnB = str(input("Ingin menghapus lagu R&B? (Ya/Tidak): "))
    if hapus_RnB == "Ya":
        lagu_hapus = str(input("Masukkan judul lagu yang ingin dihapus: "))
        if lagu_hapus in RnB:
            RnB.remove(lagu_hapus)
            print("Playlist R&B terbaru: ", RnB)
        else:
            print("Lagu tidak ditemukan dalam playlist.")
    elif tambah_RnB == "Tidak":
        print("Terima kasih. Selamat mendengarkan lagu R&B!")

else:
    print("Genre Playlist tidak tersedia, silakan pilih dengan benar.")