![Praproses data](https://github.com/fando-tek/Hybrid-learning-IDS/assets/81504312/c1dd3547-4d5e-4cb4-a8d4-6fac1d6f9821)
## 1. Menggabungkan semua dataset CIC2018 menjadi 1 Dataset
Pada tahap ini, dilakukan penggabungan dataset menjadi satu dataset kemudian disimpan dalam format CSV. Setelah itu, dataset yang telah digabungkan di muat kembali untuk selanjutnya dilakukan tahapan praproses lainnya.
## 2. Praproses Data
Tahapan selanjutnya adalah praproses data. Praproses data melalui serangkaian tahapan seperti integrasi data, transformasi data, pembersihan data, dan pengambilan sampel data yang bertujuan untuk memperoleh dataset dalam bentuk yang dibutuhkan untuk membangun model. Gambar diatas menunjukkan alur tahapan praproses data yang digunakan dalam penelitian ini.\
```
- Menghapus duplikat baris header yang memiliki nama yang sama.
- Nama fitur dalam dataset juga diubah menjadi huruf kecil yang dihubungkan dengan garis bawah (underscore) untuk memudahkan akses fitur dalam dataset.
- Protokol yang digunakan dalam penelitian ini adalah TCP dan UDP, sehingga nilai protokol selain 6 (TCP) dan 17 (UDP) dihapus dari dataset.
- Dataset yang digunakan juga mengandung nilai tak terhingga (infinity) dan nilai yang hilang. Untuk menangani masalah ini, nilai infinity diubah menjadi NaN dan fitur (kolom) dihapus pada fitur yang memiliki nilai NaN lebih dari 50%, sedangkan sampel data (baris) dihapus pada fitur yang memiliki nilai NaN kurang dari 50%.
- Penghapusan fitur terhadap fitur yang tidak memiliki variasi nilai.
- Penghapusan salah satu fitur yang memiliki distribusi yang sama dilakukan dengan menghitung koefisien korelasi menggunakan pearson correlation coefficient antara kedua fitur.
- Penambahan label baru ke dalam kelas biner dengan menetapkan label "benign" dan label "0" pada data normal, dan penambahan label "attack" dan label "1" pada data serangan di setiap sampel data. Sehingga terdapat tiga pelabelan kelas target yang berbeda.
- Penyeimbangan kelas dengan menggunakan pendekatan under sampling. Under sampling dilakukan hanya untuk menyeimbangkan data kelas normal terhadap kelas serangan. Under sampling dilakukan dengan menggunakan metode Nearmiss-2 dengan diterapkan tiga rasio pengambilan sampel yang berbeda dan satu rasio tanpa pengambilan sampel (1:1, 2:1, 3:1, dan 4,79:1). Rasio 4,79:1 dibulatkan menjadi rasio 5:1 bertujuan untuk mendapatkan angka yang lebih sederhana dan mudah dipahami.
```
