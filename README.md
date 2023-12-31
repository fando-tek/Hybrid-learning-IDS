# PENINGKATAN KINERJA PADA INTRUSION DETECTION SYSTEM (IDS) DENGAN 3 LAPISAN PEMBELAJARAN HIBRID
Dengan perkembangan teknologi informasi yang pesat saat ini, serangan siber terhadap jaringan semakin meningkat dan menyebabkan kerugian finansial yang signifikan. Oleh karena itu, sistem deteksi intrusi (IDS) berbasis anomali menggunakan pembelajaran mesin menjadi salah satu pendekatan untuk mendeteksi serangan siber.\
\
Untuk meningkatkan kinerja IDS, diusulkan metode hibrid dengan menggunakan Long Short Term Memory (LSTM) dan Random Forest (RF), dengan dataset CICCSE-IDS2018. Dalam pembentukan model hibrid, model lapisan satu menggunakan LSTM untuk klasifikasi biner, mengklasifikasikan aliran data sebagai data normal atau data serangan. Data normal diklasifikasikan kembali dengan model lapisan dua dan data serangan diklasifikasikan kembali dengan model lapisan tiga. \
\
Jika hasil model lapisan dua diklasifikasikan sebagai data normal, maka merupakan hasil akhir, dan jika diklasifikasikan sebagai data serangan maka diklasifikasikan kembali dengan model lapisan tiga secara multikelas menggunakan Random Forest. Hasil klasifikasi multikelas lapisan tiga merupakan hasil akhir dari model hibrid ini. \
\
Berdasarkan pengujian dan analisis, model hibrid dengan evaluasi terbaik di peroleh menggunakan dataset dengan rasio 3 : 1. Model hibrid ini mencapai hasil klasifikasi multi kelas dengan accuracy 99,7618%, precision 99,1901%, recall 96,8809% dan f1-score 97,9508%.
#### Hasil Evaluasi Model Hibrid dengan dataset rasio 3 banding 1
|	Accuracy|	Precision|	Recall|	F1-score|
|---|---|---|---|
|99,7618 %|99,1901 %|	96,8809 %|	97,9508 %|
