Nama: Raymundo Rafaelito Maryos Von Woloblo
Kelas: PBP B
## Tugas 6
- Synchronous request memblokir dan biasanya menyebabkan reload halaman (sederhana tapi lambat), sedangkan asynchronous request (AJAX/fetch) berjalan di background tanpa reload sehingga UI tetap responsif dan hanya bagian yang perlu saja di-update (lebih cepat tapi butuh logika tambahan seperti manajemen state, error handling, dan history).

- AJAX di Django bekerja seperti ini: JS kirim fetch/XHR ke view Django (sertakan CSRF dan credentials), view memproses (validasi, auth, create/update), lalu JsonResponse dikembalikan; JS membaca JSON dan update UI tanpa reload — untuk login/register server tetap harus verifikasi kredensial dan mengembalikan response yang aman (session cookie atau token) dan client harus menangani cookie/credential dengan benar.

- AJAX memberi UX lebih cepat dan interaktif karena hanya mengupdate bagian halaman yang perlu dan menghemat bandwidth, cocok untuk fitur real-time atau inline edit; tapi menambah kompleksitas (manajemen state, history, fallback/SEO) dibanding render server-side penuh.

- Keamanan AJAX untuk login/register ditangani di server: pakai Django auth (authenticate/login, create_user), jangan @csrf_exempt, gunakan CSRF token pada header, selalu HTTPS, set cookie flags (Secure, HttpOnly, SameSite), batasi rate login (anti-brute force), validasi server-side, minimalkan info error, dan jangan simpan token sensitif di localStorage — client cukup kirim request dengan X-CSRFToken dan credentials:'same-origin'.

- AJAX meningkatkan UX dengan membuat interaksi lebih cepat, mulus, dan responsif (tanpa reload), tapi menambah tanggung jawab developer: harus menangani history, aksesibilitas, SEO, dan memberikan feedback/loading/error yang jelas — kalau diterapkan benar, UX jadi jauh lebih nyaman; kalau asal-asalan, malah membingungkan pengguna.

## Tugas 5
- Prioritas CSS berjalan berdasarkan: pertama deklarasi dengan !important, lalu origin stylesheet (author/user/user-agent), kemudian specificity (inline > ID > class/attribute/pseudo-class > tag/pseudo-element), dan jika specificity sama diputuskan oleh source order (rule yang didefinisikan paling akhir menang). Intinya: jangan pakai !important sembarangan; atur struktur selector dan urutan file supaya predictable.

- Responsive design penting karena pengguna mengakses web dari banyak ukuran layar — tanpa responsif UX buruk, konversi turun, dan SEO bisa terpengaruh; contoh yang sudah responsive misalnya Google Search atau X karena mereka prioritas mobile, sedangkan contoh yang kurang responsive biasanya situs intranet lama atau admin panel enterprise yang dibuat khusus desktop

- Margin adalah ruang di luar elemen untuk memisahkan elemen satu dengan lain, border adalah garis pembatas yang bisa diberi warna/ketebalan, dan padding adalah ruang di dalam border agar konten tidak menempel; implementasinya via margin, border, dan padding di CSS (shorthand tersedia), dan gunakan box-sizing: border-box supaya ukuran elemen termasuk padding & border sehingga layout lebih mudah dikendalikan.

- Flexbox adalah layout satu-dimensi yang bagus untuk menyusun item dalam baris atau kolom (mis. nav, toolbar, row card) dengan properti seperti justify-content, align-items, dan flex; CSS Grid adalah layout dua-dimensi yang lebih kuat untuk tata letak halaman atau area kompleks (baris + kolom) dengan grid-template-*, grid-row/column; praktisnya, gunakan Grid untuk struktur halaman dan Flexbox untuk menyusun komponen di dalam area tersebut.

Langkah-langkah mengimplementasikan cheklist tugas 5:
  - Menambahkan Tailwind, fitur Edit Product, fitur Hapus Product, dan Navigation Bar ke aplikasi Main
  - Konfigurasi file statis pada Main
  - Styling pada Main dengan Tailwind dan External CSS

## Tugas 4
- Django AuthenticationForm adalah form bawaan Django yang dipakai untuk login user dengan validasi username dan password secara otomatis. Kelebihannya simpel, langsung terintegrasi dengan sistem autentikasi Django, dan hemat waktu. Kekurangannya agak terbatas kalau butuh kustomisasi login lebih kompleks (misalnya tambah field atau logika lain).

- Autentikasi itu proses memverifikasi identitas user (misalnya login dengan username & password), sedangkan otorisasi menentukan hak akses user setelah terverifikasi (misalnya hanya admin bisa tambah produk). Django mengimplementasikan keduanya lewat AuthenticationMiddleware untuk autentikasi dan permissions/decorators untuk otorisasi.

- Session menyimpan data di server (lebih aman, user hanya pegang session ID), sedangkan cookies menyimpan data langsung di browser (lebih ringan, tapi lebih berisiko). Kelebihan session adalah keamanan lebih baik, sementara cookies unggul di performa karena langsung di sisi client. Kekurangannya, session bisa membebani server, cookies bisa disalahgunakan kalau tidak diamankan.

- Cookies tidak otomatis aman secara default, ada risiko seperti pencurian data lewat XSS atau CSRF. Django mengurangi risiko ini dengan fitur keamanan bawaan seperti HttpOnly, Secure, dan CSRF tokens. Jadi aman digunakan asal developer mengaktifkan opsi-opsi keamanan tersebut.

- Langkah-langkah mengimplementasikan cheklist tugas 4:
  - Membuat fungsi register, login. dan logout
  - Membatasi akses halaman main dan product_detail
  - Menampilkan detail informasi pengguna yang sedang logged in, yaitu username
  - Menerapkan cookies seperti last_login pada halaman utama aplikasi
  - Membuat dua akun pengguna dengan masing-masing tiga dummy data menggunakan model yang telah dibuat sebelumnya untuk setiap akun di lokal

## Tugas 3
- Data delivery diperlukan untuk memastikan pertukaran data yang efisien, aman, dan skalabel antar komponen platform, seperti server dan klien atau microservices. Tanpa mekanisme ini, integrasi data menjadi tidak terstruktur, rentan terhadap kesalahan, dan sulit diskalakan, sehingga menghambat performa keseluruhan sistem.

- JSON lebih unggul daripada XML untuk sebagian besar aplikasi web modern karena struktur yang lebih sederhana, ukuran file yang lebih kecil, dan kemudahan parsing di bahasa seperti JavaScript. JSON lebih populer karena mendukung efisiensi bandwidth, fleksibilitas dalam API RESTful, dan adopsi luas di framework kontemporer, sedangkan XML lebih sesuai untuk dokumen kompleks dengan skema ketat.

- Method is_valid() pada form Django berfungsi untuk memvalidasi input pengguna berdasarkan aturan yang didefinisikan, mengembalikan True jika valid beserta data yang telah dibersihkan, atau False dengan daftar kesalahan. Method ini esensial untuk mencegah data tidak valid memasuki database, mengurangi kerentanan keamanan, dan menjaga integritas aplikasi tanpa validasi manual yang rumit.

- CSRF token diperlukan untuk mencegah serangan Cross-Site Request Forgery (CSRF), di mana penyerang memanipulasi sesi pengguna yang terautentikasi melalui form palsu. Tanpa token, Django tidak dapat memverifikasi asal request, berpotensi mengizinkan aksi tidak sah seperti transfer dana ilegal. Penyerang dapat mengeksploitasi ini melalui phishing atau situs berbahaya yang menyamar sebagai form legitimate, memanfaatkan cookie sesi untuk eksekusi aksi berbahaya.

- Langkah-langkah mengimplementasikan cheklist tugas 3:
  - Menmbahkan 4 fungsi views baru untuk melihat objek yang sudah ditambahkan dalam format XML, JSON, XML by ID, dan JSON by ID serta membuat routing URL untuk masing-masing fungsi views tadi
  - Mengimplementasikan skeleton sebagai kerangka views
  - Membuat halaman yang menampilkan data objek model yang memiliki tombol "Add" yang akan redirect ke halaman form, serta tombol "Detail" pada setiap data objek model yang akan menampilkan halaman detail objek
  - Membuat halaman form untuk menambahkan objek model pada app sebelumnya
  - Membuat halaman yang menampilkan detail dari setiap data objek model

- Tangkapan layar Postman:
  - ![alt text](xml.png)
  - ![alt text](json.png)
  - ![alt text](xml_by_id.png)
  - ![alt text](json_by_id.png)

## Tugas 2
- Tautan menuju aplikasi PWS yang sudah di-deploy: https://raymundo-rafaelito-footballshop.pbp.cs.ui.ac.id/

- Langkah-langkah mengimplementasikan cheklist tugas 2:
    - Membuat direktori lokal football-shop 
    - Menyiapkan dependencies dan membuat proyek Django, yaitu football_shop
    - Konfigurasi environment variables dan proyek
    - Unggah proyek ke repositori GitHub
    - Deployment melalui PWS
    - Membuat aplikasi main dalam proyek football-news
    - Membuat dan mengisi berkas main.html
    - Mengubah berkas models.py dalam aplikasi main: Menambahkan Class Product dengan atribut name, price, description, thumbnail, category, is_featured, dan product_views
    - Membuat dan mengaplikasikan migrasi Model
    - Modifikasi template
    - Mengonfigurasi routing URLrAplikasi main
    - Mengonfigurasi routing URL Proyek
    - Membuat Unit Test dan Menjalankan Test

- https://miro.medium.com/v2/resize:fit:1400/1*m2_0pEyl1cfnfWYgCSlAZA.png
  Kaitan antara urls.py, views.py, models.py, dan berkas html pada bagan:
  - HTTP Request: Permintaan HTTP dikirim oleh klien (misalnya browser) ke server.
  - URLs (urls.py): Permintaan diterima oleh modul urls.py yang bertugas untuk memetakan URL ke fungsi atau view yang sesuai, lalu meneruskan permintaan ke view yang tepat.
  - View (views.py): Modul views.py memproses permintaan tersebut. View dapat membaca atau menulis data ke model jika diperlukan.
  - Model (models.py): Model menyediakan data yang dibutuhkan oleh view melalui operasi read/write data.
  - Template (<namafile>.html): View menggunakan template (berupa file HTML) untuk merender data menjadi respons yang dapat ditampilkan.
  - HTTP Response (HTML): Akhirnya, respons dalam bentuk HTML dikirim kembali ke klien sebagai hasil dari permintaan HTTP.

- Berkas settings.py di Django adalah file yang berfungsi sebagai pusat kontrol utama untuk mendefinisikan dan mengonfigurasi berbagai aspek proyek web, mulai dari pengaturan keamanan, seperti kunci rahasia, daftar host yang mempunyai akses, dan penentuan Debug atau tidak; pengaturan koneksi basis data; daftar aplikasi yang terinstal; pengaturan zona waktu dan bahasa; hingga konfigurasi penanganan file statis dan media. File ini bertindak sebagai "cetak biru" yang mengontrol bagaimana aplikasi berfungsi dan memungkinkan penyesuaian berbagai aspek aplikasi sesuai kebutuhan.

- Pertama-tama, dibuat migrasi model yang dijalankan dengan perintah berikut: python manage.py makemigrations

  makemigrations menciptakan berkas migrasi yang berisi perubahan model yang belum diaplikasikan ke dalam basis data. Lalu, diterapkan migrasi ke dalam basis data lokal yang dijalankan perintah berikut: python manage.py migrate

  migrate mengaplikasikan perubahan model yang tercantum dalam berkas migrasi ke basis data dengan menjalankan perintah sebelumnya.

- Jujur, berdasarkan pengetahuan saya sekarang, saya tidak tahu pasti jawabannya, tetapi saya punya hipotesis bahwa jawabannya adalah karena Framework Django merupakan Framework yang paling beginner-friendly

- Belum ada