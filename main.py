import time
from random import randint
from datetime import datetime
import sys

# 🔒 Pengecekan Masa Aktif Script
expired_date = datetime(2025, 5, 30, 23, 0, 0)  # 13 Mei 2025 pukul 23:00
now = datetime.now()
if now > expired_date:
    print(f"⛔️ Masa aktif script telah habis pada {expired_date.strftime('%d-%m-%Y %H:%M:%S')}. Silakan hubungi pembuat.")
    sys.exit()

def get_dummy_history():
    return [randint(0, 9) for _ in range(15)]

def predict_skorselisih(data):
    recent = ["Big" if x >= 5 else "Small" for x in data]
    big = recent.count("Big")
    small = recent.count("Small")
    selisih = abs(big - small)

    if selisih >= 5:
        return "Big" if big < small else "Small"
    elif 2 <= selisih <= 3:
        return "Big" if big > small else "Small"
    else:
        return recent[0] if recent else "Big"

print("🌀 NEXT PERIODE...")

last_sent_time = 0

while True:
    now = time.localtime()
    current_second = now.tm_sec
    current_minute = now.tm_min
    current_time = time.time()
    current_periode = int(current_time // 60)

    # Deteksi hanya saat mendekati detik 55 (maks 2x per ronde)
    if 00 <= current_second <= 00 and current_periode != last_sent_time:
        data = get_dummy_history()
        hasil = predict_skorselisih(data)

        print("========================")
        print("55five - WinGo - 1 Menit")
        print(f"Periode  : {current_periode % 1000}")
        print(f"Prediksi : {hasil}")
        print("K³ Cukup")
        print("========================")

        last_sent_time = current_periode
        time.sleep(2.5)  # Hindari spam saat looping cepat
    else:
        time.sleep(0.2)  # Loop cepat agar tangkap detik 55 dengan akurat
