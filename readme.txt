How to use project

1. Import sql_data.sql pada sql server yang digunakan.
2. Pada file main.py:7 , sesuaikan username dan password sql server.
3. jalankan main.py, maka table pada database akan terbuat secara otomatis.



How to test

- Disini saya menggunakan curl untuk pengetesan API.
- pastikan program sudah running
- pastikan curl sudah terinstall.
- ubah payload sesuai yang diinginkan, pastikan tipe data sesuai
- jalankan pada terminal

1. register endpoint ('/dashboard/register')

    curl --location --request POST 'http://localhost:5000/dashboard/register' \
    --header 'Content-Type: application/json' \
    --data-raw '{
        "id": <str>,
        "username":<str>,
        "password":<str>
    }'

2. login endpoint ('/dashboard/login')

    curl --location --request POST 'http://localhost:5000/dashboard/login' \
    --header 'Content-Type: application/json' \
    --data-raw '{
        "username":<str>,
        "password":<str>
    }'

3. tambah karyawan baru endpoint ('/karyawan')

    curl --location --request POST 'http://localhost:5000/karyawan' \
    --header 'Content-Type: application/json' \
    --data-raw '{
        "id": <int>,
        "nama_lengkap": <str>,
        "nomor_induk_karyawan": <str>,
        "alamat": <str>,
        "cabang": <str>,
        "organisasi": <str>,
        "jabatan": <str>,
        "level_jabatan": <str>
    }'

4. Get All karyawan endpoint('/karyawan')

    curl --location --request GET 'http://localhost:5000/karyawan'

5. create presensi endpoint ('/presensi') 
    - Pastikan karyawan dengan id yang dimasukan sudah exist.

    curl --location --request POST 'http://localhost:5000/presensi' \
    --header 'Content-Type: application/json' \
    --data-raw '{
        "tanggal": <str>,
        "created_at": <datetime>,
        "updated_at": <datetime>,
        "jam_masuk": <str>,
        "jam_pulang": <str>,
        "id_karyawan": <int>,
        "presensi_status": <str>
    }'

6. get presensi endpoint ('/presensi')
    curl --location --request GET 'http://localhost:5000/presensi'

7. karyawan absen >3 ('/presensi/absen')
    curl --location --request GET 'http://localhost:5000/presensi/absen'


Disini program masih dapat banyak dikembangkan seperti migrate db, penambahan schema request dan response, dll.