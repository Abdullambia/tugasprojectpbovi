import mysql.connector

con = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "5220411421"
)    
if con.is_connected():
    print("Koneksi ke server database berhasil")

db = con.cursor()
# db.execute("create table if not exists tbmahasiswa(Nim varcar(10),"
#            "Nama_Mahasiswa varchar(50), Alamat varchar(50), Prodi varchar(50), Angkatan Varchar(250))")  


