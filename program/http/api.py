from flask import Blueprint, request, jsonify
from program.domain import entity
from program.service.api import LoginService,KaryawanService,PresensiService

api_bp = Blueprint('api', __name__)


@api_bp.route('/dashboard/login', methods=['POST'])
def login():
    data = request.json
    username = data['username']
    password = data['password']

    user = entity.User(
        username=username,
        password=password
    )
    # Panggil service untuk melakukan login

    result = LoginService.login(user)
    return jsonify({'message': result['result']}), result['STATUS_CODE']

@api_bp.route('/dashboard/register', methods=['POST'])
def register():
    data = request.json
    id=data['id']
    username = data['username']
    password = data['password']
    
    user = entity.User(
        id=id,
        username=username,
        password=password
    )
    # Panggil service untuk melakukan login

    result = LoginService.register(user)
    return jsonify({'message': result['result']}), result['STATUS_CODE']

@api_bp.route('/karyawan', methods=['GET', 'POST'])
def karyawan():
    if request.method == 'GET':
        result = KaryawanService.get_all_karyawan()
        
        return jsonify({'message': result['result']}), result['STATUS_CODE']
    
    elif request.method == 'POST':
        # Menambahkan karyawan baru
        data = request.json

        new_karyawan = entity.Karyawan(id=data['id'],nama_lengkap=data['nama_lengkap'], nomor_induk_karyawan=data['nomor_induk_karyawan'],
                                alamat=data['alamat'], cabang=data['cabang'], organisasi=data['organisasi'],
                                jabatan=data['jabatan'], level_jabatan=data['level_jabatan'])
        
        result = KaryawanService.add_karyawan(new_karyawan)
        return jsonify({'message': result['result']}),result['STATUS_CODE']
    
@api_bp.route('/presensi', methods=['GET', 'POST'])
def presensi():
    if request.method == 'GET':
        # Mendapatkan semua data presensi
        result = PresensiService.get_presensi()
        return jsonify({'message': result['result']}),result['STATUS_CODE']

    elif request.method == 'POST':
        # Menambahkan data presensi baru
        data = request.json
        new_presensi = entity.Presensi(id=1,tanggal=data['tanggal'], created_at=data['created_at'], updated_at=data['updated_at'],
                                jam_masuk=data['jam_masuk'], jam_pulang=data['jam_pulang'], id_karyawan=data['id_karyawan'],
                                presensi_status=data['presensi_status'])
        result = PresensiService.add_presensi(new_presensi)
        return jsonify({'message': 'Presensi added successfully'}), 201
    

@api_bp.route('/presensi/absen', methods=['GET'])
def presensi_absen():
    result = PresensiService.get_karyawan_absen()
    return jsonify({'message': result['result']}),result['STATUS_CODE']