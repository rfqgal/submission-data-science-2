# Proyek Akhir: Menyelesaikan Permasalahan Jaya Jaya Institut

## Business Understanding

Jaya Jaya Institut merupakan salah satu institusi pendidikan perguruan yang telah berdiri sejak tahun 2000. Hingga saat ini ia telah mencetak banyak lulusan dengan reputasi yang sangat baik. Akan tetapi, terdapat banyak juga siswa yang tidak menyelesaikan pendidikannya alias dropout.

Jumlah dropout yang tinggi ini tentunya menjadi salah satu masalah yang besar untuk sebuah institusi pendidikan. Oleh karena itu, Jaya Jaya Institut ingin mendeteksi secepat mungkin siswa yang mungkin akan melakukan dropout sehingga dapat diberi bimbingan khusus.

### Permasalahan Bisnis

Meskipun Jaya Jaya Institut mencetak banyak lulusan dengan reputasi sangat baik, namun melihat angka jumlah siswa yang dropout itu tinggi menjadi tantangan serius bagi institusi. Hal ini akan mempengaruhi citra dan reputasi akademik institusi, hingga alokasi operasional dan sumber daya seperti beasiswa, pengajar, serta sarana prasarana belajar.

Hingga saat ini belum tersedia sistem atau pendekatan untuk memprediksi sedini mungkin siswa yang berisiko tinggi untuk dropout. Hal ini dapat membuat pihak institusi terlambat dalam memberikan tindakan pencegahan yang dapat dilakukan seperti bimbingan akademik atau bantuan finansial.

### Cakupan Proyek

1. Menganalisis pola dan distribusi `Status` (Dropout/Graduate/Enrolled) berdasarkan berbagai fitur seperti `Displaced`, `Gender`, `Mothers_qualification`, `Fathers_qualification`, `Course`, dsb.
1. Mengidentifikasi faktor-faktor utama yang dapat berkontribusi terhadap pemodelan prediktif siswa keluar dengan machine learning.
1. Membuat model prediksi dropout untuk mengidentifikasi siswa yang berisiko tinggi dropout, guna membantu tim terkait dari Jaya Jaya Institut untuk memberikan tindakan pencegahan.
1. Membangun dashboard bisnis menggunakan Looker Studio untuk menyajikan data `Status` (Dropout/Graduate/Enrolled)  secara visual, sehingga tim terkait dari institut dapat mengambil keputusan yang berbasis data.
1. Memberi rekomendasi strategis berdasarkan analisis yang dilakukan untuk menurunkan tingkat dropout siswa.

### Persiapan

Dataset: https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance/data.csv

#### Setup Environment - Shell/Terminal

```
cd submission-data-science-2
pipenv install
pipenv shell
pip install -r requirements.txt
```

#### Run Notebook

```
cd submission-data-science-2 jupyter-notebook
```

## Business Dashboard

Dashboard bisnis ini menampilkan 10 faktor penting, berdasarkan model yang telah dikembangkan, yang berpotensi mempengaruhi siswa untuk dropout. Faktor tersebut terbagi menjadi:
- Demografis Siswa
- Demografis Orang Tua
- Akademik dan Pendaftaran

Setiap segmen menampilkan faktor gambaran mengenai potensi dropout siswa.

Dashboard Looker Studio dapat diakses pada [tautan berikut](https://lookerstudio.google.com/s/vA8TQCGhxlE).

## Menjalankan Aplikasi Prediksi Dropout

#### Run Streamlit

```
cd submission-data-science-2 
streamlit run app.py
```

#### Access Deployed Model Predict Prototype

Streamlit app: [Student Droprout Rate](https://student-dropout-rate-rfqgal.streamlit.app/)

## Conclusion

 Dari hasil analasis tabel distribusi dan grafik persentase fitur Status pada 10 fitur penting didapati insights sebagai berikut:

1. Sebanyak 32% mahasiswa memutuskan dropout.
1. Sebanyak 12% mahasiswa penerima beasiswa mengalami dropout.
1. Sebanyak 45% mahasiswa berjenis kelamin laki-laki mengalami dropout.
1. `Mothers_qualification`: 6, 9, 10, 11, 27, 34, 35 memiliki dropout tinggi (>60%-100%).
1. `Fathers_qualification`: 6, 10, 13, 18, 20, 22, 25, 27, 29 memiliki 100% dropout.
1. Sebanyak 69% mahasiswa dropout memiliki `Mothers_occupation=0`.
1. Sebanyak 50% mahasiswa dropout memiliki usia 18-19 tahun saat masuk kuliah.
1. Sebanyak 30% mahasiswa dropout mengambil program studi management dan nursing.
1. Sebanyak 50% mahasiswa dropout memiliki usia 23 tahun saat mendaftar kuliah.
1. Sebanyak 25% mahasiswa dropout memiliki skor grade 133 pada tingkat pendidikan sebelumnya.

### Rekomendasi Action Items

1. Gunakan model prediksi untuk menandai mahasiswa dengan:
    - Usia 18, 19 dan 23 tahun saat mendaftar.
    - Grade 133 dari pendidikan sebelumnya.
    - Latar belakang pendidikan dan pekerjaan orang tua dengan kode 6, 9, 10, 11, 27.
  
    Fokuskan perhatian dan intervensi pada kelompok resiko tersebut sejak awal semester.

2. Sediakan program bimbingan akademik khusus untuk mahasiswa dengan potensi dropout tinggi, yaitu dari latar belakang keluarga dengan pendidikan rendah, mahasiswa penerima beasiswa, dan mahasiswa laki-laki.

3. Evaluasi dan mengoptimalkan kurikulum pada program studi dengan dropout tinggi, yaitu Management dan Nursing.
