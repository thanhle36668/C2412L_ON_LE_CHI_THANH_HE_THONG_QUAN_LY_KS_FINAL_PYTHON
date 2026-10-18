import json
from models import PhongThuong, PhongVIP, KhachHang, PhieuThue

def save_data(danh_sach_phong, danh_sach_phieu_thue, danh_sach_doanh_thu):
    ds_phong_json = []
    for p in danh_sach_phong:
        if isinstance(p, PhongVIP):
            ds_phong_json.append({
                "loai_phong": "VIP",
                "ma_phong": p.ma_phong,
                "ten_phong": p.ten_phong,
                "gia_co_ban": p.gia_co_ban,
                "trang_thai": p.trang_thai,
                "phi_don_dep": p.phi_don_dep,
                "phi_minibar": p.phi_minibar
            })
        else:
            ds_phong_json.append({
                "loai_phong": "Thuong",
                "ma_phong": p.ma_phong,
                "ten_phong": p.ten_phong,
                "gia_co_ban": p.gia_co_ban,
                "trang_thai": p.trang_thai
            })

    ds_phieu_thue_json = []
    for pt in danh_sach_phieu_thue:
        ds_phieu_thue_json.append({
            "ma_khach": pt.khach_hang.ma_khach,
            "ten_khach": pt.khach_hang.ten,
            "so_cccd": pt.khach_hang.so_cccd,
            "ma_phong": pt.phong.ma_phong,
            "so_ngay_thue": pt.so_ngay_thue
        })

    with open("khachsan_data.json", "w", encoding="utf-8") as f:
        json.dump({
            "danh_sach_phong": ds_phong_json,
            "danh_sach_phieu_thue": ds_phieu_thue_json,
            "lich_su_doanh_thu": danh_sach_doanh_thu
        }, f, ensure_ascii=False, indent=4)

def load_data():
    try:
        with open("khachsan_data.json", "r", encoding="utf-8") as f:
            data = json.load(f)

        danh_sach_phong = []
        for p in data["danh_sach_phong"]:
            if p["loai_phong"] == "VIP":
                phong = PhongVIP(p["ma_phong"], p["ten_phong"], p["gia_co_ban"], p["phi_don_dep"], p["phi_minibar"])
            else:
                phong = PhongThuong(p["ma_phong"], p["ten_phong"], p["gia_co_ban"])
            phong.trang_thai = p["trang_thai"]
            danh_sach_phong.append(phong)

        danh_sach_phieu_thue = []
        for pt in data["danh_sach_phieu_thue"]:
            khach_hang = KhachHang(pt["ma_khach"], pt["ten_khach"], pt["so_cccd"])

            phong = next((p for p in danh_sach_phong if p.ma_phong == pt["ma_phong"]), None)

            if phong is not None:
                try:
                    phieu_thue = PhieuThue(khach_hang, phong, pt["so_ngay_thue"])
                except ValueError:
                    phong.trang_thai = "Trống"
                    print(f"Bỏ qua phiếu thuê lỗi (mã phòng {pt['ma_phong']}) và trả phòng về Trống.")
                    continue
                danh_sach_phieu_thue.append(phieu_thue)

        danh_sach_doanh_thu = data.get("lich_su_doanh_thu", [])

        return {
            "danh_sach_phong": danh_sach_phong,
            "danh_sach_phieu_thue": danh_sach_phieu_thue,
            "lich_su_doanh_thu": danh_sach_doanh_thu
        }
    
    except (FileNotFoundError, json.JSONDecodeError):
        return {
            "danh_sach_phong": [], 
            "danh_sach_phieu_thue": [],
            "lich_su_doanh_thu": []
        }