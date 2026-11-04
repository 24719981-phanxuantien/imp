# RSA C Web - Flask + Render

Website giao diện tiếng Việt để mã hóa/giải mã RSA bằng chương trình C.

## Chạy thử trên Windows

1. Cài Python 3.10+ và GCC (ví dụ MinGW-w64).
2. Mở CMD tại thư mục dự án.
3. Cài thư viện:

   ```cmd
   py -m pip install -r requirements.txt
   ```

4. Biên dịch C (nếu dùng MinGW):

   ```cmd
   gcc -O2 rsa.c -o rsa.exe
   ```

   Trên Windows, sửa `app.py` để executable là `rsa.exe`, hoặc chạy trên môi trường Linux/Render dùng file `rsa`.

5. Chạy:

   ```cmd
   py app.py
   ```

6. Mở `http://127.0.0.1:5000`.

## Đưa lên GitHub

Tạo repository mới, giải nén dự án, sau đó chạy:

```bash
git init
git add .
git commit -m "Create RSA C web application"
git branch -M main
git remote add origin https://github.com/USERNAME/REPOSITORY.git
git push -u origin main
```

Thay `USERNAME/REPOSITORY` bằng địa chỉ repository của bạn.

## Deploy trên Render

1. Đăng nhập https://render.com và chọn **New + → Web Service**.
2. Kết nối GitHub và chọn repository vừa push.
3. Chọn Runtime: **Python**.
4. Build Command:

   ```bash
   pip install -r requirements.txt && gcc -O2 -Wall -Wextra rsa.c -o rsa
   ```

5. Start Command:

   ```bash
   gunicorn app:app
   ```

6. Chọn **Create Web Service** và chờ Render deploy.

## Lưu ý thuật toán

Đây là RSA giáo dục, mã hóa từng byte độc lập, không phải AES và không phải thiết kế RSA an toàn cho dữ liệu thực tế. Cần dùng cặp khóa RSA hợp lệ; modulus `n` phải lớn hơn 255. Bản demo không có padding OAEP, xác thực hay quản lý khóa an toàn.
