
# BÀI THỰC HÀNH DG1

## Thông tin sinh viên

- Họ và tên: Ngô Thành An
- MSSV: 2412111050
- Tên Project: dg1_2412111050
- Môi trường: Ubuntu WSL2
- Công nghệ: Linux, Git, GitHub, Python Flask, Docker, Docker Compose, Nginx.

---

# PHẦN A - LINUX VÀ BACKUP

## A1. Làm việc với Linux

Kiểm tra thư mục hiện tại:

```bash
pwd
```

Hiển thị danh sách file:

```bash
ls -la
```

Tạo thư mục project:

```bash
mkdir -p ~/dg1_2412111050
cd ~/dg1_2412111050
```

## A2. Phân quyền và Backup

Tạo thư mục chứa script:

```bash
mkdir -p scripts
```

Cấp quyền thực thi cho script đã tạo:

```bash
chmod +x scripts/backup.sh
```

Chạy script:

```bash
./scripts/backup.sh
```

Kiểm tra kết quả backup:

```bash
ls -lh backups/
```

Lưu ý: Đường dẫn backup cần đối chiếu với script thực tế.

---

# PHẦN B - GIT VÀ GITHUB

## B1. Khởi tạo Git

```bash
git init
```

Kiểm tra trạng thái:

```bash
git status
```

## B2. Quản lý nhánh

Các nhánh sử dụng:

- main
- develop
- feature/web-app
- feature/docker

Kiểm tra:

```bash
git branch -a
```

## B3. File .gitignore

Các nội dung cần loại trừ:

```gitignore
logs/
*.tar.gz
__pycache__/
node_modules/
.env
.venv/
*.bak
```

## B4. Commit và Push

```bash
git add .
git commit -m "Complete DG1 practice"
git push origin feature/docker
```

---

# PHẦN C - ỨNG DỤNG PYTHON FLASK

## C1. Xây dựng ứng dụng Web

Ứng dụng Flask sử dụng dữ liệu sinh viên lưu trong file JSON.

Cấu trúc:

```text
app/
├── app.py
├── data/
│   └── students.json
├── templates/
│   └── index.html
└── static/
    └── style.css
```

## C2. Các API

| Phương thức | Endpoint | Chức năng |
|---|---|---|
| GET | / | Trang chủ |
| GET | /api/health | Kiểm tra trạng thái |
| GET | /api/students | Danh sách sinh viên |
| GET | /api/students?lop=... | Lọc theo lớp |
| GET | /api/students/1 | Tìm theo ID |
| POST | /api/students | Thêm sinh viên |

## C3. Chạy ứng dụng

Kích hoạt môi trường ảo:

```bash
source .venv/bin/activate
```

Cài Flask:

```bash
pip install -r requirements.txt
```

Chạy chương trình:

```bash
python app/app.py
```

Kiểm tra API:

```bash
curl -i http://localhost:5000/api/health
curl -i http://localhost:5000/api/students
```

Kết quả mong đợi: HTTP 200 OK.

---

# PHẦN D - DOCKER

## D1. Dockerfile

Ứng dụng được đóng gói bằng Docker.

Kiểm tra Docker:

```bash
docker --version
docker compose version
```

Build Image:

```bash
docker build -t dg1-flask:1.0 .
```

## D2. Chạy Container

```bash
docker run -d --name dg1-container -p 5000:5000 dg1-flask:1.0
```

Kiểm tra:

```bash
docker ps
```

Kiểm thử:

```bash
curl -i http://localhost:5000/api/health
```

## D3. Docker Compose và Nginx

Các service:

- web: Ứng dụng Flask.
- nginx: Reverse Proxy.

Khởi động:

```bash
docker compose up -d --build
```

Kiểm tra:

```bash
docker compose ps
```

Kiểm thử thông qua Nginx:

```bash
curl -i http://localhost:8080/
curl -i http://localhost:8080/api/health
curl -i http://localhost:8080/api/students
```

## Kết quả kiểm thử

- Health API qua Nginx: Đã từng trả về HTTP 200.
- Students API qua Nginx: Đã từng trả về HTTP 200.
- Trang chủ: Cần xác nhận lại sau khi khắc phục lỗi thiếu students.json.

---

# KẾT LUẬN

Bài thực hành DG1 bao gồm:

1. Thao tác Linux và Backup.
2. Quản lý mã nguồn bằng Git và GitHub.
3. Xây dựng ứng dụng Flask quản lý sinh viên.
4. Đóng gói ứng dụng bằng Docker.
5. Triển khai Docker Compose kết hợp Nginx.

Sinh viên: Ngô Thành An

MSSV: 2412111050
