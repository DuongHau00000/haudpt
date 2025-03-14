songuyen = list(map(int, input("Nhập các số nguyên: ").split()))
a_songuyen=[]
for i in songuyen:
    if i % 2 == 0:
        a_songuyen.append(i)
print("Danh sách chỉ chứa số chẵn:",a_songuyen)