from program.domain import entity
from program.adapter.repository import UserRepository,KaryawanRepository, PresensiRepository
from werkzeug.security import check_password_hash

class LoginService:
    def login(user: entity.User) -> str:
        data =  UserRepository.get(username=user.username)

        if not data:
            return {"result": "Wrong Username and Password", "STATUS_CODE": 200} 
        
        if check_password_hash(data.password, user.password):
            return {"result": "Login Successful", "STATUS_CODE": 200} 
        else:
            return {"result": "Incorrect Password", "STATUS_CODE": 200} 
    
    def register(user: entity.User) -> str:
        data = UserRepository.get(username=user.username)

        if data:
            return {"result": "Username already exist", "STATUS_CODE": 200} 

        user.set_hash_password(user.password)
        UserRepository.create(user)

        return {"result":"Register Success", "STATUS_CODE": 201} 
    
class KaryawanService:
    def add_karyawan(karyawan: entity.Karyawan):
                
        if KaryawanRepository.get(karyawan.nomor_induk_karyawan):
            return {"result": "Karyawan Sudah Terdaftar","STATUS_CODE": 200}
        
        KaryawanRepository.create(karyawan)
        return  {"result": "Karyawan Added Successfully","STATUS_CODE": 200}
    
    def get_all_karyawan():
        result = KaryawanRepository.get_all()
        if not result:
            return {"result":"Data is Empty","STATUS_CODE": 404}
        
        return {"result":result,"STATUS_CODE": 200}
        
class PresensiService:
    def add_presensi(karyawan: entity.Presensi):
        PresensiRepository.create(karyawan)
        return {"result":"Presensi Success","STATUS_CODE": 200}

    def get_presensi():
        result = PresensiRepository.get_all()
        if not result:
            return {"result":"Data is Empty","STATUS_CODE": 404}
        
        return {"result":result,"STATUS_CODE": 200}

    def get_karyawan_absen():
        result = PresensiRepository.get_karyawan_absen()

        if not result:
            return {"result":"Karyawan Naik Gaji","STATUS_CODE": 400}
        
        return {"result":result,"STATUS_CODE": 200}
