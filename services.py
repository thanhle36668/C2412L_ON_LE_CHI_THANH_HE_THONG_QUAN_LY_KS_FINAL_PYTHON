from models import PhieuThue, PhongVIP

def tinh_tien(phong, so_ngay_thue):
    return phong.tinh_tien(so_ngay_thue)

class QuanLyKhachSan:
    def __init__(self):
        self.danh_sach_phong = []
        self.danh_sach_phieu_thue = []
        self.lich_su_doanh_thu = []

    def them_phong(self, phong):
        for p in self.danh_sach_phong:
            if p.ma_phong == phong.ma_phong:
                raise ValueError("Mã phòng đã tồn tại.")

        if phong.gia_co_ban <= 0:
            raise ValueError("Giá cơ bản phải lớn hơn 0.")
        if isinstance(phong, PhongVIP):
            if phong.phi_don_dep < 0 or phong.phi_minibar < 0:
                raise ValueError("Phí dọn dẹp và phí minibar không được âm.")
            
        self.danh_sach_phong.append(phong)

    def dat_phong(self, ma_phong, khach_hang, so_ngay_thue):
        phong_tim = next((p for p in self.danh_sach_phong if p.ma_phong == ma_phong), None)

        if phong_tim is None:
            raise ValueError("Phòng không tồn tại.")

        if phong_tim.trang_thai == "Đã thuê":
            raise ValueError("Phòng đã được thuê.")

        if so_ngay_thue <= 0:
            raise ValueError("Số ngày thuê phải lớn hơn 0.")

        phieu_thue = PhieuThue(khach_hang, phong_tim, so_ngay_thue)
        self.danh_sach_phieu_thue.append(phieu_thue)
        phong_tim.trang_thai = "Đã thuê"

        return phieu_thue

    def tra_phong(self, ma_phong):
        phong_tim = next((p for p in self.danh_sach_phong if p.ma_phong == ma_phong), None)

        if phong_tim is None:
            raise ValueError("Phòng không tồn tại.")

        phieu_thue_tim = next((pt for pt in self.danh_sach_phieu_thue if pt.phong.ma_phong == ma_phong), None)

        if phieu_thue_tim is None:
            raise ValueError("Phòng này chưa được thuê.")

        tong_tien = tinh_tien(phieu_thue_tim.phong, phieu_thue_tim.so_ngay_thue)

        loai = "VIP" if isinstance(phong_tim, PhongVIP) else "Thuong"
        self.lich_su_doanh_thu.append({
            "loai_phong": loai,
            "ma_phong": phong_tim.ma_phong,
            "ten_phong": phong_tim.ten_phong,
            "ma_khach_hang": phieu_thue_tim.khach_hang.ma_khach,
            "ten_khach_hang": phieu_thue_tim.khach_hang.ten,
            "so_ngay_thue": phieu_thue_tim.so_ngay_thue,
            "tong_tien": tong_tien
        })

        self.danh_sach_phieu_thue.remove(phieu_thue_tim)
        phong_tim.trang_thai = "Trống"

        return tong_tien

    def bao_cao_doanh_thu(self):
        tong_doanh_thu = sum(hoa_don["tong_tien"] for hoa_don in self.lich_su_doanh_thu)

        so_phong_trong = sum(1 for p in self.danh_sach_phong if p.trang_thai == "Trống")

        return {
            "tong_doanh_thu": tong_doanh_thu,
            "so_phong_trong": so_phong_trong
        }