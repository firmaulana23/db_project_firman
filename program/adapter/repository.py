from program.domain import models,entity
from common.database import db


class UserRepository:
    def create(user: entity.User):

        model = models.User(id=user.id,username=user.username, password=user.password)
        db.session.add(model)
        db.session.commit()

    def get(username) -> entity.User:
        model = models.User.query.filter_by(username=username).first()
        if model is None:
            return None

        return model
    
class KaryawanRepository:
    def create(karyawan:entity.Karyawan):
        model = models.Karyawan(id=karyawan.id,nama_lengkap=karyawan.nama_lengkap, nomor_induk_karyawan=karyawan.nomor_induk_karyawan,
                                alamat=karyawan.alamat, cabang=karyawan.cabang, organisasi=karyawan.organisasi,
                                jabatan=karyawan.jabatan, level_jabatan=karyawan.level_jabatan)
        db.session.add(model)
        db.session.commit()

    def get(nik):
        model = models.Karyawan.query.filter_by(nomor_induk_karyawan=nik).first()
        if model is None:
            return None
        
        data = model.__dict__
        result = entity.Karyawan(**data)

        return result
    
    def get_all():
        model = models.Karyawan.query.all()
        if model is None:
            return None
        
        data = []
        for karyawan_model in model:
            karyawan_entity = {
                "id":karyawan_model.id,
                "nama_lengkap":karyawan_model.nama_lengkap,
                "nomor_induk_karyawan":karyawan_model.nomor_induk_karyawan,
                "alamat":karyawan_model.alamat,
                "cabang":karyawan_model.cabang,
                "organisasi":karyawan_model.organisasi,
                "jabatan":karyawan_model.jabatan,
                "level_jabatan":karyawan_model.level_jabatan
                # Add other attributes as needed
            }
            data.append(karyawan_entity)

        result = data

        return result

    

class PresensiRepository:
    def create(presensi: entity.Presensi):
        model = models.Presensi(tanggal=presensi.tanggal, created_at=presensi.created_at, updated_at=presensi.updated_at,
                                jam_masuk=presensi.jam_masuk, jam_pulang=presensi.jam_pulang, id_karyawan=presensi.id_karyawan,
                                presensi_status=presensi.presensi_status)
        db.session.add(model)
        db.session.commit()

    def get(id):
        model = models.Presensi.query.filter_by(nomor_induk_karyawan=id).first()
        if model is None:
            return None
        
        data = model.__dict__
        result = entity.Presensi(**data)

        return result

    def get_all():
        model = models.Presensi.query.all()
        if model is None:
            return None
        
        data = []
        for presensi_model in model:
            presensi_entity = {
                'id': presensi_model.id, 'tanggal': presensi_model.tanggal, 'created_at': presensi_model.created_at, 'updated_at': presensi_model.updated_at,
                      'jam_masuk': presensi_model.jam_masuk, 'jam_pulang': presensi_model.jam_pulang, 'id_karyawan': presensi_model.id_karyawan,
                      'presensi_status': presensi_model.presensi_status
                # Add other attributes as needed
            }
            data.append(presensi_entity)

        result = data

        return result

    def get_karyawan_absen():
        model = (db.session.query(models.Karyawan)
            .join(models.Presensi)
            .filter(models.Presensi.presensi_status == "Absen")
            .group_by(models.Karyawan.id)
            .having(db.func.count(models.Presensi.id) > 3)
            .all())
        
        data = []
        for karyawan_model in model:
            karyawan_entity = {
                "id":karyawan_model.id,
                "nama_lengkap":karyawan_model.nama_lengkap,
                "nomor_induk_karyawan":karyawan_model.nomor_induk_karyawan,
                "alamat":karyawan_model.alamat,
                "cabang":karyawan_model.cabang,
                "organisasi":karyawan_model.organisasi,
                "jabatan":karyawan_model.jabatan,
                "level_jabatan":karyawan_model.level_jabatan
                # Add other attributes as needed
            }
            data.append(karyawan_entity)

        result = data
        return result