Hand Gesture Mouse Control dengan MediaPipe
Program Python untuk mengontrol mouse dan browser (Chrome) menggunakan gesture tangan berbasis MediaPipe Hands dan OpenCV. Gesture tangan digunakan untuk menggerakkan kursor, klik, scroll, dan membuka TikTok secara otomatis.

Fitur
•	Deteksi tangan secara real-time menggunakan kamera
•	Gerakan kursor menggunakan jari telunjuk
•	Klik mouse dengan gesture Thumb Up
•	Scroll halaman dengan gesture Point
•	Membuka Google Chrome (mode guest) dan TikTok dengan gesture Fist
•	Tampilan visual landmark tangan

Teknologi
Program ini dikembangkan dan diuji menggunakan:
•	Python 3.x
•	OpenCV 4.12.0
•	MediaPipe 0.10.14
•	PyAutoGUI 0.9.54
•	NumPy 2.2.6

Instalasi
Pastikan Python dan kamera sudah tersedia, lalu install dependency berikut:
pip install opencv-python mediapipe pyautogui numpy

Menjalankan Program
Jalankan file Python:
python gesture_tangan.py
Tekan tombol ESC untuk keluar dari program.

Cara Penggunaan Gesture
Gesture	Deskripsi Fungsi
Point (☝️)	Menggerakkan kursor mouse
Thumb Up (👍)	Klik mouse
Fist (✊)	Membuka Google Chrome & TikTok
Open Palm (✋)	Tidak ada aksi
Unknown	Tidak dikenali

Alur Kerja Singkat
1.	Kamera menangkap citra tangan
2.	MediaPipe mendeteksi landmark tangan
3.	Sistem menentukan jari yang terbuka
4.	Gesture diklasifikasikan dengan rule-based
5.	Aksi mouse / browser dijalankan sesuai gesture

