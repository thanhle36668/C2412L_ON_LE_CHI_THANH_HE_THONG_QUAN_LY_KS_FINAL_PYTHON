# **ĐỀ THI THỰC HÀNH PYTHON: XÂY DỰNG HỆ THỐNG QUẢN LÝ KHÁCH SẠN**

**Mục tiêu:** Vận dụng linh hoạt Lập trình hướng đối tượng (OOP), chia tách Module, xử lý file và xử lý ngoại lệ (Exception Handling) để hoàn thiện một ứng dụng Giao diện dòng lệnh (CLI).

### **1. Thiết kế nền tảng đối tượng**

**Yêu cầu:** Viết code trong file models.py.

- Tạo lớp cơ sở Phong gồm các thuộc tính: Mã phòng, Tên phòng, Giá cơ bản, Trạng thái (Trống/Đã thuê). Sử dụng tính đóng gói (private/protected) cho thuộc tính Trạng thái để không bị thay đổi trực tiếp từ bên ngoài mà phải qua phương thức.
- Tạo hai lớp con kế thừa từ Phong:
  - PhongThuong: Không có phí phụ thu.
  - PhongVIP: Có thêm thuộc tính Phí dịch vụ dọn dẹp và Phí minibar.
- Tạo lớp KhachHang gồm: Mã khách, Tên, Số CCCD/CMND.
- Tạo lớp PhieuThue gồm: Khách hàng (object), Phòng (object), Số ngày thuê.

### **2. Xử lý nghiệp vụ lõi & Tính đa hình**

**Yêu cầu:** Viết code trong file services.py.

- Viết phương thức tinh_tien() cho PhongThuong và PhongVIP. (Gợi ý: PhongVIP sẽ cộng thêm các khoản phí dịch vụ, thể hiện tính **Đa hình** khi gọi hàm tính tiền).
- Tạo lớp QuanLyKhachSan lưu danh sách các phòng và các phiếu thuê hiện tại.
- Viết chức năng **Thêm phòng mới** vào hệ thống.
- Viết chức năng **Đặt phòng**:
  - Kiểm tra phòng có trống không?
  - Nếu trống, đổi trạng thái phòng thành "Đã thuê" và tạo một PhieuThue.

### **3. Lưu trữ dữ liệu**

**Yêu cầu:** Viết code trong file file_handler.py và tích hợp vào services.py.

- Khi chương trình tắt, dữ liệu về các phòng và phiếu thuê không được mất đi.
- Viết hàm save_data(danh_sach_phong, danh_sach_phieu) để xuất dữ liệu ra file khachsan_data.json.
- Viết hàm load_data() để tự động đọc dữ liệu từ file JSON này khi khởi động lại chương trình.

### **4. Hoàn thiện quy trình & Báo cáo**

**Yêu cầu:** Bổ sung vào services.py.

- Viết chức năng **Trả phòng**:
  - Nhập mã phòng cần trả.
  - Tính tổng tiền khách phải trả dựa trên số ngày và loại phòng.
  - Chuyển trạng thái phòng về lại "Trống".
  - Lưu doanh thu của phiếu thuê này vào lịch sử.
- Viết chức năng **Báo cáo doanh thu**: In ra tổng doanh thu khách sạn đã kiếm được và hiển thị số lượng phòng đang trống hiện tại.

### **5. Xây dựng Giao diện CLI & Bắt lỗi hệ thống**

**Yêu cầu:** Lắp ráp tất cả vào main.py.

- Thiết kế một Menu chạy vòng lặp while True:
  - Hiển thị danh sách phòng
  - Thêm phòng mới
  - Đặt phòng
  - Trả phòng & Thanh toán
  - Xem báo cáo doanh thu
  - Thoát & Lưu dữ liệu
- **Bắt lỗi (Try-Except):** Đảm bảo chương trình không bị crash (văng lỗi) khi:
  - Người dùng nhập chữ vào những chỗ yêu cầu nhập số (ví dụ: số ngày thuê, giá tiền).
  - Người dùng chọn đặt một phòng không tồn tại.
  - File JSON chưa được tạo trong lần chạy đầu tiên.
