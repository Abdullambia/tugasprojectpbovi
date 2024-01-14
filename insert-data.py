import mysql.connector

def buat_koneksi():
    host = "localhost"
    user = "root"
    password = ""
    database = "5220411421"

    try:
        koneksi = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )

        print("Terhubung ke database.")
        return koneksi

    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

def periksa_koneksi():
    koneksi = buat_koneksi()
    if koneksi:
        koneksi.close()

def tampilkan_data():
    koneksi = buat_koneksi()
    if not koneksi:
        return

    cursor = koneksi.cursor()

    # Menampilkan data dari tabel
    query = "SELECT * FROM tbmahasiswa"
    cursor.execute(query)
    hasil = cursor.fetchall()

    if not hasil:
        print("Tabel kosong.")
    else:
        print("\nData dalam Tabel:")
        for row in hasil:
            print("NPM:", row[0])
            print("Nama Mahasiswa:", row[1])
            print("Alamat:", row[2])
            print("Prodi:", row[3])
            print("Angkatan:", row[4])
            print("-------------------------")
    koneksi.close()
def tambah_data():
    koneksi = buat_koneksi()
    if not koneksi:
        return

    cursor = koneksi.cursor()

    NPM = input("Masukkan NPM: ")
    nama_mahasiswa = input("Masukkan Nama Mahasiswa: ")
    alamat = input("Masukkan Alamat: ")
    prodi = input("Masukkan Program Studi: ")
    angkatan = input("Masukkan Angkatan: ")

    query = "INSERT INTO tbmahasiswa (NPM, nama_mahasiswa, alamat, prodi, angkatan) VALUES (%s, %s, %s, %s, %s)"
    values = (NPM, nama_mahasiswa, alamat, prodi, angkatan)

    cursor.execute(query, values)
    koneksi.commit()

    print("Data berhasil ditambahkan!")

    koneksi.close()

def hapus_data():
    koneksi = buat_koneksi()
    if not koneksi:
        return

    cursor = koneksi.cursor()

    NPM = input("Masukkan NPM data yang akan dihapus: ")

    query = "DELETE FROM tbmahasiswa WHERE NPM = %s"
    values = (NPM,)

    cursor.execute(query, values)
    koneksi.commit()

    print("Data berhasil dihapus!")

    koneksi.close()

def ubah_data():
    koneksi = buat_koneksi()
    if not koneksi:
        return

    cursor = koneksi.cursor()

    npm = input("Masukkan NPM data yang akan diubah: ")
    nama_mahasiswa_baru = input("Masukkan Nama Mahasiswa baru: ")
    alamat_baru = input("Masukkan Alamat baru: ")
    prodi_baru = input("Masukkan Program Studi baru: ")
    angkatan_baru = input("Masukkan Angkatan baru: ")

    query = "UPDATE tbmahasiswa SET nama_mahasiswa=%s, alamat=%s, prodi=%s, angkatan=%s WHERE NPM=%s"
    values = (nama_mahasiswa_baru, alamat_baru, prodi_baru, angkatan_baru, npm)

    cursor.execute(query, values)
    koneksi.commit()

    print("Data berhasil diubah!")

    koneksi.close()
    

def main():
    periksa_koneksi()

    while True:
        print("\nMenu:")
        print("1. Tampilkan Data")
        print("2. Tambah Data")
        print("3. Hapus Data")
        print("4. Ubah Data")
        print("5. Keluar")

        pilihan = input("Pilih menu (1/2/3/4/5): ")

        if pilihan == '1':
            tampilkan_data()
        elif pilihan == '2':
            tambah_data()
        elif pilihan == '3':
            hapus_data()
        elif pilihan == '4':
            ubah_data()
        elif pilihan == '5':
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih menu yang sesuai.")

if __name__ == "__main__":
    main()
