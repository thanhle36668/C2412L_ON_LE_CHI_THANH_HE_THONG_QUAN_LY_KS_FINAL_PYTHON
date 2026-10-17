class Phong:
    def __init__(self, ma_phong, ten_phong, gia_co_ban, trang_thai = "Trống"):
        self.ma_phong = ma_phong
        self.ten_phong = ten_phong
        self.gia_co_ban = gia_co_ban
        self.trang_thai = trang_thai

    @property
    def trang_thai(self):
        return self._trang_thai

    @trang_thai.setter
    def trang_thai(self, trang_thai_moi):
        if trang_thai_moi in ["Trống", "Đã thuê"]:
            self._trang_thai = trang_thai_moi
        else:
            raise ValueError("Trạng thái chỉ được là 'Trống' hoặc 'Đã thuê'")

    def tinh_tien(self, so_ngay_thue):
        return self.gia_co_ban * so_ngay_thue

class PhongThuong(Phong):
    def __init__(self, ma_phong, ten_phong, gia_co_ban):
        super().__init__(ma_phong, ten_phong, gia_co_ban)

    def tinh_tien(self, so_ngay_thue):
        return self.gia_co_ban * so_ngay_thue    

class PhongVIP(Phong):
    def __init__(self, ma_phong, ten_phong, gia_co_ban, phi_don_dep, phi_minibar):
        super().__init__(ma_phong, ten_phong, gia_co_ban)
        self.phi_don_dep = phi_don_dep
        self.phi_minibar = phi_minibar

    def tinh_tien(self, so_ngay_thue):
        return (self.gia_co_ban + self.phi_don_dep + self.phi_minibar) * so_ngay_thue

class KhachHang:
    def __init__(self, ma_khach, ten, so_cccd):
        self.ma_khach = ma_khach
        self.ten = ten
        self.so_cccd = so_cccd

class PhieuThue:
    def __init__(self, khach_hang, phong, so_ngay_thue):
        self.khach_hang = khach_hang
        self.phong = phong
        self.so_ngay_thue = so_ngay_thue
