from common.database import db
from werkzeug.security import check_password_hash,generate_password_hash
import uuid

class User(db.Model):
    id = db.Column(db.String(100), primary_key=True,default=str(uuid.uuid4()))
    username = db.Column(db.String(100))
    password = db.Column(db.String(100))

    def set_password(self, password):
        self.password = generate_password_hash(password)

class Karyawan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nama_lengkap = db.Column(db.String(100))
    nomor_induk_karyawan = db.Column(db.String(20), unique=True)
    alamat = db.Column(db.String(200))
    cabang = db.Column(db.String(50))
    organisasi = db.Column(db.String(50))
    jabatan = db.Column(db.String(50))
    level_jabatan = db.Column(db.String(50))

# Model untuk tabel Presensi
class Presensi(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tanggal = db.Column(db.Date)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)
    jam_masuk = db.Column(db.String(10))
    jam_pulang = db.Column(db.String(10))
    id_karyawan = db.Column(db.Integer, db.ForeignKey('karyawan.id'))
    presensi_status = db.Column(db.String(50))