songuyen= list(map(int,input("Nhập các số nguyên: ").split()))
danhsach_remove = int(input("Nhập số cần xóa khỏi danh sách: "))
if danhsach_remove in songuyen:
    songuyen.remove(danhsach_remove)
    print("Danh sách sau khi xóa:",songuyen)
else:
    print(f"Số{danhsach_remove} không có trong danh sách.")