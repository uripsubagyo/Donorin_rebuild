
# A04 - Donorin

Anda dapat mengakses situs web Kelompok A04 di [link berikut.](https://a04-donorin.herokuapp.com/)

## Anggota kelompok
* Davina Fardya Zulfa Izzati
* Faris Bayhaqi
* Hanin Atina Rahmania
* I Made Urip Subagyo
* Salma Hanifah Hidayanti

## Cerita aplikasi dan manfaat Donorin
Ancaman kesehatan global merupakan isu yang tengah dibahas dalam G20. Setelah pandemi COVID-19 yang memengaruhi kesehatan banyak individu, penurunan kemampuan masyarakat untuk membantu dalam bidang kesehatan mulai terlihat. Data kantong darah yang diberikan oleh Provinsi Jawa Tengah mengalami kekurangan hingga 60 persen.

Kebutuhan darah pasca COVID-19 mulai membaik, tetapi masih perlu diwaspadai. Data yang dikutip dari theconvercation.com pada tanggal 19 September 2022 mengungkapkan bahwa Indonesia masih mempunyai 20 persen kebutuhan kantong darah. Namun, pemerataan ketersediaan darah belum terwujud dengan baik. Terdapat daerah yang masih kekurangan kantong darah dan yang kelebihan kantong darah. Dengan begitu kesulitan dalam mencari data ketersediaan kantong darah masih sangat sulit untuk diperoleh.

Masyarakat mengalami kesulitan, khususnya dalam pendonoran darah, karena memerlukan pencarian relawan, proses screening, dan mengharuskan pendonornya sehat, padahal kesehatan mereka terdampak pandemi. Di sisi lain, banyak orang mengalami kendala untuk mendapat informasi terkait ketersediaan stok darah karena berita pasca pandemi masih menjadi perhatian tertinggi di bidang kesehatan. Selain itu, pembatasan kunjungan ke rumah sakit atau pusat kesehatan lainnya ikut memengaruhi informasi yang diterima masyarakat.

Oleh karena itu, Donorin hadir sebagai solusi isu kesehatan global dengan cara memfasilitasi masyarakat dalam melakukan donor darah. Donorin menyediakan informasi lokasi donor darah, penjadwalan donor darah, berita terkini yang relevan dengan donor darah dan kesehatan global, serta ketersediaan stok darah di lokasi tertentu. Melalui aplikasi ini, kami berharap masyarakat semakin menyadari manfaat donor danar, baik untuk kesehatan individu maupun kesehatan masyarakat, juga merasakan kemudahan dalam menemukan darah dan melakukannya.

Referensi data:
* https://dataindonesia.id/Ragam/detail/stok-darah-indonesia-sebesar-87238-kantong-per-14-juni-2022
* https://theconversation.com/data-bicara-donasi-darah-di-indonesia-naik-dalam-10-tahun-tapi-masih-kurang-20-188850

## Daftar modul
### Login, Logout, Registration
Alur registration akun:

Registration (email & password) → ketika login direct ke pengisian data diri, jika belum mengisi, pengguna tidak dapat mengakses fitur apa pun.

Setelah log in, akan terdapat form pengisian data diri pengguna dengan rincian sebagai berikut:

* Nama Lengkap Pengguna
* Nomor Telepon
* Golongan Darah
* Jenis Kelamin
* Tanggal Lahir

### Landing Page
Berisi informasi atau berita seputar donor darah.

Terdapat berbagai informasi mengenai donor darah, seperti pengertian, manfaat, persiapan yang diperlukan sebelum mendonor darah, dan lainnya.

### Admin Dashboard
Terdapat fitur memasukkan hasil screening kesehatan.

Terdapat fitur untuk menerima atau menolak penjadwalan donor darah pengguna.

### User Dashboard
Pada bagian user dashboard akan berisikan fitur booking mengarah pada penjadwalan donor darah.

Jumlah history sudah berapa kali donor atau menerima darah.

Melihat data hasil dari screening kesehatan.

### Penjadwalan Donor Darah
Dengan fitur ini, pengguna bisa menjadwalkan kedatangan mereka ke tempat donor darah. Ketika pengguna sudah mengisi data, data tersebut akan masuk ke dashboard admin untuk dikonfirmasi apakah pengguna dapat datang saat jadwal tersebut.

## Peran pengguna
### Admin
Admin dapat melihat data diri pengguna, memasukkan hasil screening kesehatan pengguna, menerima atau menolak penjadwalan donor darah, dan memasukkan informasi mengenai lokasi donor darah.

### Pengguna biasa
Pengguna dapat melihat data diri, menjadwalkan donor darah, melihat berita pada landing page, melihat history donor darahnya (apabila melakukan penjadwalan melalui aplikasi), dan melihat informasi mengenai tempat atau lokasi donor darah.