songuyen = list(map(int, input("Nhập các số nguyên:").split()))
a_songuyen = set(songuyen)
if len(a_songuyen)>=2:
    sx_songuyen=sorted(a_songuyen,reverse=True)
    sx_ln=sx_songuyen[1]
    print("Số lớn thứ hai trong danh sách là:", sx_ln)
else:
    print("Danh sách không đủ ít nhất 2 số khác nhau.")