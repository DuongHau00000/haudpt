songuyen=list(map(int, input("Nhập các số nguyên: ").split()))
a_songuyen=list(set(songuyen))
for i in songuyen:
    if i not in a_songuyen:
        a_songuyen.append(i)
print("Danh sách sau khi xóa các phần tử trùng lặp",a_songuyen)