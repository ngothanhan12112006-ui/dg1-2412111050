#!/bin/bash
TARGET_DIR="$1"

if [ -z "$1" ]; then
    echo "Lỗi: Vui lòng cung cấp đường dẫn thư mục cần backup."
    echo "Cách sử dụng: $0 <duong_dan_thu_muc>"
    exit 1
fi
if [ ! -d "$TARGET_DIR" ]; then
    echo "Lỗi: Thư mục '$TARGET_DIR' không tồn tại!"
    exit 1
fi
BACKUP_DIR="$HOME/backup"
mkdir -p "$BACKUP_DIR"
DIR_NAME=$(basename "$(realpath "$TARGET_DIR")")
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")
BACKUP_FILE="$BACKUP_DIR/${DIR_NAME}_${TIMESTAMP}.tar.gz"
echo "Đang nén thư mục '$TARGET_DIR'..."
tar -czf "$BACKUP_FILE" -C "$(dirname "$(realpath "$TARGET_DIR")")" "$DIR_NAME"

if [ $? -ne 0 ]; then
    echo "Lỗi: Quá trình tạo file nén thất bại."
    exit 1
fi
LOG_DIR="logs"
mkdir -p "$LOG_DIR"
LOG_FILE="$LOG_DIR/backup.log"

LOG_TIME=$(date +"%Y-%m-%d %H:%M:%S")
echo "[$LOG_TIME] - Backup thành công: $BACKUP_FILE" >> "$LOG_FILE"
echo "Hoàn tất! File backup đã được lưu tại: $BACKUP_FILE"
exit 0
