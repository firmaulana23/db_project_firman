from pydantic import BaseModel,Field
from typing import Optional
from datetime import datetime
from werkzeug.security import check_password_hash,generate_password_hash

class User(BaseModel):
    id: Optional[str] = None
    username: str
    password: str

    def set_hash_password(self, password):
        self.password = generate_password_hash(password)

class Karyawan(BaseModel):
    id: int
    nama_lengkap: str
    nomor_induk_karyawan: str
    alamat: str
    cabang: str
    organisasi: str
    jabatan: str
    level_jabatan: str

class Presensi(BaseModel):
    id: int
    tanggal: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    jam_masuk: str
    jam_pulang: str
    id_karyawan: int
    presensi_status: str