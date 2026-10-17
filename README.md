# Hệ Thống Quản Lý Khách Sạn

Bài thi thực hành Python - Ứng dụng CLI quản lý khách sạn áp dụng Lập trình hướng đối tượng (OOP), chia tách module, xử lý file và xử lý ngoại lệ.

## Thông tin

- **Họ và tên:** Lê Chí Thành
- **Lớp:** C2412L_ON
- **Ngôn ngữ:** Python 3

## Chức năng chính

1. Hiển thị danh sách phòng
2. Thêm phòng mới (Phòng thường / Phòng VIP)
3. Đặt phòng (kiểm tra phòng trống, tạo phiếu thuê)
4. Trả phòng & thanh toán (tính tiền theo loại phòng, lưu doanh thu)
5. Xem báo cáo doanh thu & số phòng còn trống
0. Thoát & tự động lưu dữ liệu

## Kiến trúc dự án

```text
HE_THONG_QUAN_LY_KHACH_SAN/
│
├── main.py            ← Giao diện CLI (menu, nhập liệu, bắt lỗi)
│
├── services.py        ← Nghiệp vụ lõi (QuanLyKhachSan)
│        │
│        └── dùng ──► models.py        ← Các lớp đối tượng (Phong, KhachHang, ...)
│
├── file_handler.py    ← Lưu / đọc dữ liệu JSON
│
└── khachsan_data.json ← Dữ liệu lưu trữ (tự sinh khi chạy)
```

### Vai trò từng module

| File | Vai trò | Nội dung chính |
| :--- | :--- | :--- |
| `main.py` | Giao diện | Menu `while True`, hàm nhập số an toàn, bắt lỗi `try-except` |
| `services.py` | Nghiệp vụ | Lớp `QuanLyKhachSan`: thêm phòng, đặt phòng, trả phòng, báo cáo |
| `models.py` | Đối tượng | `Phong`, `PhongThuong`, `PhongVIP`, `KhachHang`, `PhieuThue` |
| `file_handler.py` | Lưu trữ | `save_data()` và `load_data()` với file `khachsan_data.json` |

### Luồng hoạt động

```text
Người dùng ──► main.py ──► services.py ──► models.py
                  │             │
                  └─────────────┴──► file_handler.py ──► khachsan_data.json
```

## Điểm nổi bật kỹ thuật

- **Đóng gói:** thuộc tính `trang_thai` của `Phong` dùng `@property`/`@setter`, chỉ nhận giá trị hợp lệ.
- **Kế thừa:** `PhongThuong` và `PhongVIP` kế thừa từ `Phong`.
- **Đa hình:** phương thức `tinh_tien()` được ghi đè; `PhongVIP` cộng thêm phí dọn dẹp và phí minibar.
- **Xử lý ngoại lệ:** bắt lỗi nhập chữ vào ô số, đặt phòng không tồn tại, và file JSON chưa tồn tại ở lần chạy đầu.
- **Lưu trữ bền vững:** dữ liệu phòng, phiếu thuê và lịch sử doanh thu được lưu vào `khachsan_data.json` và tự động tải lại khi khởi động.

## Yêu cầu hệ thống

- Python 3.8 trở lên (không cần thư viện ngoài).

## Hướng dẫn chạy

```bash
python main.py
```

Sau đó chọn chức năng theo menu hiển thị. Chọn `0` để thoát và lưu dữ liệu.

## Định dạng dữ liệu (`khachsan_data.json`)

File JSON gồm 3 phần: `danh_sach_phong`, `danh_sach_phieu_thue`, `lich_su_doanh_thu`. File này được tạo tự động trong lần chạy đầu tiên khi bạn lưu dữ liệu.
