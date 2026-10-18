from models import PhongThuong, PhongVIP, KhachHang
from services import QuanLyKhachSan
from file_handler import save_data, load_data

def nhap_so_nguyen(so, min_gia_tri = None):
    while True:
        try:
            gia_tri = int(input(so))
            if min_gia_tri is not None and gia_tri < min_gia_tri:
                print(f"Vui lòng nhập số nguyên lớn hơn hoặc bằng {min_gia_tri}.")
                continue
            return gia_tri
        except ValueError:
            print("Vui lòng nhập một số nguyên hợp lệ.")

def nhap_so_thuc(so):
    while True:
        try:
            return float(input(so))
        except ValueError:
            print("Vui lòng nhập một số hợp lệ.")

def dinh_dang_tien(so):
    return f"{so:,.0f}".replace(",", ".")

def hien_thi_danh_sach_phong(ql):
    if len(ql.danh_sach_phong) == 0:
        print("Danh sách phòng trống.")
        return

    for p in ql.danh_sach_phong:
        loai = "VIP" if isinstance(p, PhongVIP) else "Thuong"
        print(f"Mã Phòng: {p.ma_phong}, Tên Phòng: {p.ten_phong}, Loại: {loai}, Giá Cơ Bản: {dinh_dang_tien(p.gia_co_ban)}, Trạng Thái: {p.trang_thai}")

def them_phong_moi(ql):
    ma_phong = input("Nhập mã phòng: ")
    ten_phong = input("Nhập tên phòng: ")
    gia_co_ban = nhap_so_thuc("Nhập giá phòng: ")

    loai = input("Loại phòng (1=Thuong, 2=VIP): ")
    if loai == "2":
        phi_don_dep = nhap_so_thuc("Nhập phí dọn dẹp: ")
        phi_minibar = nhap_so_thuc("Nhập phí minibar: ")
        phong = PhongVIP(ma_phong, ten_phong, gia_co_ban, phi_don_dep, phi_minibar)
    else:
        phong = PhongThuong(ma_phong, ten_phong, gia_co_ban)

    try:
        ql.them_phong(phong)
        print("Thêm phòng thành công.")
    except ValueError as e:
        print("Lỗi: ", e)

def dat_phong_moi(ql):
    ma_phong = input("Nhập mã phòng: ")

    ma_khach = input("Nhập mã khách hàng: ")
    ten_khach = input("Nhập tên khách hàng: ")
    while True:
        so_cccd = input("Nhập số CCCD: ")
        if so_cccd.isdigit() and len(so_cccd) in (9, 12):
            break
        print("Số CCCD không hợp lệ. Vui lòng nhập lại (9 hoặc 12 chữ số).")
    khach_hang = KhachHang(ma_khach, ten_khach, so_cccd)

    so_ngay_thue = nhap_so_nguyen("Nhập số ngày thuê: ", min_gia_tri=1)

    try:
        phieu_thue = ql.dat_phong(ma_phong, khach_hang, so_ngay_thue)
        print("Đặt phòng thành công.")
        print(f"Tên khách hàng: {phieu_thue.khach_hang.ten}, Tên phòng: {phieu_thue.phong.ten_phong}, Số ngày thuê: {phieu_thue.so_ngay_thue}")
    except ValueError as e:
        print("Lỗi: ", e)

def tra_phong_va_thanh_toan(ql):
    ma_phong = input("Nhập mã phòng: ")

    try:
        tong_tien = ql.tra_phong(ma_phong)
        print(f"Tổng tiền đã thanh toán: {dinh_dang_tien(tong_tien)}")
        print("Trả phòng và thanh toán thành công.")
    except ValueError as e:
        print("Lỗi: ", e)

def xem_bao_cao_doanh_thu(ql):
    ket_qua = ql.bao_cao_doanh_thu()
    tong_doanh_thu = ket_qua.get("tong_doanh_thu", 0)
    so_phong_trong = ket_qua.get("so_phong_trong", 0)
    print(f"Tổng doanh thu: {dinh_dang_tien(tong_doanh_thu)} | Số phòng còn trống: {so_phong_trong}")

def main():
    du_lieu = load_data()
    ql = QuanLyKhachSan()
    ql.danh_sach_phong = du_lieu["danh_sach_phong"]
    ql.danh_sach_phieu_thue = du_lieu["danh_sach_phieu_thue"]
    ql.lich_su_doanh_thu = du_lieu["lich_su_doanh_thu"]

    while True:
        print("===== QUẢN LÝ KHÁCH SẠN =====")
        print("1. Hiển thị danh sách phòng")
        print("2. Thêm phòng mới")
        print("3. Đặt phòng")
        print("4. Trả phòng & thanh toán")
        print("5. Xem báo cáo doanh thu")
        print("0. Thoát & lưu dữ liệu")

        chon = input("Chọn chức năng: ")

        if chon == "1":
            hien_thi_danh_sach_phong(ql)
        elif chon == "2":
            them_phong_moi(ql)
        elif chon == "3":
            dat_phong_moi(ql)
        elif chon == "4":
            tra_phong_va_thanh_toan(ql)
        elif chon == "5":
            xem_bao_cao_doanh_thu(ql)
        elif chon == "0":
            save_data(ql.danh_sach_phong, ql.danh_sach_phieu_thue, ql.lich_su_doanh_thu)
            print("Đã lưu dữ liệu. Tạm biệt!")
            break
        else:
            print("Lựa chọn không hợp lệ.")

if __name__ == "__main__": 
    main()
