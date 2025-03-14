songuyen = list(map(int, input("Nhập các số nguyên: ").split()))
songuyen_check = int(input("Nhập số cần kiểm tra: "))
count = songuyen.count(songuyen_check)
print(f"Số {songuyen_check} xuất hiện {count} lần trong danh sách.")