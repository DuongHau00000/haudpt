phantu = list(map(int,input("Nhập các số nguyên: ").split()))
tong = sum(phantu)
tb =tong / len(phantu) if phantu else 0
print("Tổng các phần tử là:",tong)
print("Trung bình các phần tử là:",tb)