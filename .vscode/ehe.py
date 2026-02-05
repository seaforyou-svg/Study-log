import datetime

catatan = []
target_harian_menit = None

def tambah_catatan():
    # Meminta input dari pengguna
    mapel = input("Masukkan nama mata pelajaran: ").strip()
    topik = input("Masukkan topik yang dipelajari: ").strip()

    # Validasi durasi agar berupa bilangan bulat positif (menit)
    while True:
        durasi_input = input("Masukkan durasi belajar (menit): ").strip()
        try:
            durasi = int(durasi_input)
            if durasi <= 0:
                print("Durasi harus lebih dari 0.")
                continue
            break
        except ValueError:
            print("Masukkan angka bulat untuk durasi.")

    # Simpan catatan sebagai dictionary
    entry = {
        "mapel": mapel,
        "topik": topik,
        "durasi_menit": durasi,
        "tanggal": datetime.date.today().isoformat(),
    }
    catatan.append(entry)
    print("Catatan berhasil ditambahkan.")

def lihat_catatan():
    # Tampilkan semua catatan dengan format yang rapi
    if not catatan:
        print("Belum ada catatan belajar. Silakan tambahkan terlebih dahulu.")
        return

    print("\n=== Daftar Catatan Belajar ===")
    for idx, entry in enumerate(catatan, start=1):
        print(f"{idx}. Mata Pelajaran : {entry.get('mapel', '-')}")
        print(f"   Tanggal        : {entry.get('tanggal', '-')}")
        print(f"   Topik          : {entry.get('topik', '-')}")
        print(f"   Durasi (menit) : {entry.get('durasi_menit', '-')}")
        print("-" * 30)

def total_waktu():
    # Hitung total durasi dari semua catatan (dalam menit)
    if not catatan:
        print("Belum ada catatan belajar untuk dihitung.")
        return

    total_menit = sum(entry.get("durasi_menit", 0) for entry in catatan)
    jam = total_menit // 60
    menit = total_menit % 60

    if jam > 0:
        print(f"Total waktu belajar: {total_menit} menit ({jam} jam {menit} menit)")
    else:
        print(f"Total waktu belajar: {total_menit} menit")

def set_target_harian():
    global target_harian_menit
    while True:
        nilai = input("Masukkan target harian (menit), atau kosong untuk batal: ").strip()
        if nilai == "":
            print("Batal mengubah target.")
            return
        try:
            menit = int(nilai)
            if menit <= 0:
                print("Target harus lebih dari 0.")
                continue
            target_harian_menit = menit
            print(f"Target harian diset: {target_harian_menit} menit.")
            return
        except ValueError:
            print("Masukkan angka bulat untuk target.")

def lihat_target_harian():
    if target_harian_menit is None:
        print("Belum ada target harian. Silakan set target terlebih dahulu.")
        return
    hari_ini = datetime.date.today().isoformat()
    total_hari = sum(e.get('durasi_menit', 0) for e in catatan if e.get('tanggal') == hari_ini)
    sisa = max(0, target_harian_menit - total_hari)
    persen = int((total_hari / target_harian_menit) * 100) if target_harian_menit > 0 else 0
    if persen > 100:
        persen = 100
    print(f"Target harian: {target_harian_menit} menit")
    print(f"Total hari ini: {total_hari} menit ({persen}% tercapai)")
    if sisa > 0:
        print(f"Sisa untuk mencapai target: {sisa} menit")
    else:
        print("Selamat! Target harian tercapai.")

def target_menu():
    print("\n=== Menu Target Harian ===")
    print("1. Set/ubah target harian")
    print("2. Lihat status target hari ini")
    print("3. Kembali")
    pilihan = input("Pilih opsi target: ")
    if pilihan == "1":
        set_target_harian()
    elif pilihan == "2":
        lihat_target_harian()
    else:
        return

def menu():
    print("\n=== Study Log App ===")
    print("1. Tambah catatan belajar")
    print("2. Lihat catatan belajar")
    print("3. Total waktu belajar")
    print("4. Keluar")
    print("5. Target harian")

if __name__ == '__main__':
    while True:
        menu()
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            tambah_catatan()
        elif pilihan == "2":
            lihat_catatan()
        elif pilihan == "3":
            total_waktu()
        elif pilihan == "4" :
            print("Terima kasih, terus semangat belajar!")
            break
        elif pilihan == "5":
            target_menu()
        else:
            print("Pilihan tidak valid")
