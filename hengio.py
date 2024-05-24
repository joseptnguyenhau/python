import time

def hen_gio(phut):
    print(f"Đợi {phut} phút...")
    time.sleep(phut * 60)
    print("Hẹn giờ đã kết thúc!")

phut_hen_gio = int(input("Nhập số phút hẹn: "))
hen_gio(phut_hen_gio)
