# Eksplorasi dataset CSE-CIC-IDS2018
Dataset yang digunakan adalah dataset CSE-CIC-IDS2018 yang dibuat khusus untuk melatih model pada IDS berbasis anomali dan diunduh melalui cloud Amazon Web Services (AWS).
Untuk mengunduh dataset ini dilakukan dengan
```
1. Instal AWS CLI dapat diunduh dari https://aws.amazon.com/cli/, tersedia untuk Mac, Windows, dan Linux 
2. Jalankan: aws s3 sync --no-sign-request --region <your-region> "s3://cse-cic-ids2018/" dest-dir\
```
Dataset ini dibuat oleh Communications Security Establishment (CSE) dan Canadian Institute of Cyber Security (CIC) pada tahun 2018, terdiri dari 10 file dengan format CSV dan PCAP. File dengan format CSV digunakan dalam penelitian ini, file CSV ini memiliki total ukuran sebesar 6,72 Gigabyte. Dataset ini mempunyai lebih dari 16 juta sampel dengan 79 fitur pada sembilan file dan 83 fitur pada satu file. Sekitar 83% merupakan data lalu lintas normal dan sekitar 17% merupakan data lalu lintas serangan, yang terdiri dari 14 kelas target. Pada dataset ini, digunakan aliran lalu lintas jaringan.\
 \
Aliran lalu lintas jaringan berisi paket-paket yang dikelompokkan dalam satu periode tertentu, memberikan gambaran aktivitas pada jaringan antara sumber dan tujuan dengan menggunakan protokol TCP dan UDP. Setiap data aliran lalu lintas dikelompokkan berdasarkan IP sumber, IP tujuan, port 22 Universitas Indonesia sumber, port tujuan, dan protokol. Data aliran lalu lintas TCP diakhiri dengan paket FIN bernilai 1, sementara untuk data aliran lalu lintas UDP diakhiri dengan batas waktu (flow timeout) tertentu, batas waktu aliran ini juga berlaku untuk data aliran lalu lintas TCP.\
\
Saat memuat dataset menggunakan pustaka Pandas, secara default tipe data setiap fitur ditetapkan secara otomatis. Tetapi, ini dapat mengkonsumsi banyak memori, mencapai 14,1 Gigabyte. Oleh karena itu diperlukan untuk mengubah tipe data yang sesuai pada setiap fitur saat memuat dataset bertujuan untuk mengoptimalkan penggunaan memori. Penetapan tipe data dilakukan dengan melihat nilai minimum dan maksimum pada setiap fitur, kecuali fitur yang memiliki NaN. Tipe data ditetapkan secara manual saat memuat dataset, dengan penetapan tipe data ini penggunaan memori berkurang menjadi 8 Gigabyte, mengurangi penggunaan memori hingga 44%.
