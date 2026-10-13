
from flask import Flask, jsonify, request, render_template
import json
import os

app = Flask(__name__)


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, "data", "students.json")



def read_students():
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)



def write_students(students):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(students, f, ensure_ascii=False, indent=4)



@app.route("/")
def home():
    students = read_students()

    return render_template(
        "index.html",
        students=students
    )



@app.route("/api/health", methods=["GET"])
def health():
    return jsonify({
        "status": "ok",
        "student": "2412111050"
    }), 200



@app.route("/api/students", methods=["GET"])
def get_students():
    students = read_students()

    lop = request.args.get("lop")

    if lop:
        students = [
            student for student in students
            if student.get("lop") == lop
        ]

    return jsonify(students), 200



@app.route("/api/students/<int:student_id>", methods=["GET"])
def get_student(student_id):
    students = read_students()

    for student in students:
        if int(student["id"]) == student_id:
            return jsonify(student), 200

    return jsonify({
        "error": "Student not found"
    }), 404



@app.route("/api/students", methods=["POST"])
def add_student():

    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return jsonify({
            "error": "Invalid JSON"
        }), 400

    required_fields = [
        "mssv",
        "ho_ten",
        "lop",
        "diem"
    ]

    for field in required_fields:
        if field not in data:
            return jsonify({
                "error": f"Missing field: {field}"
            }), 400

    for field in ["mssv", "ho_ten", "lop"]:
        if not isinstance(data[field], str) or not data[field].strip():
            return jsonify({
                "error": f"Invalid field: {field}"
            }), 400

    try:
        if isinstance(data["diem"], bool):
            raise ValueError

        diem = float(data["diem"])

    except (ValueError, TypeError):
        return jsonify({
            "error": "Diem phai la mot so"
        }), 400

    if not 0 <= diem <= 10:
        return jsonify({
            "error": "Diem phai nam trong khoang 0 den 10"
        }), 400

    students = read_students()

    new_id = max(
        (int(student["id"]) for student in students),
        default=0
    ) + 1

    new_student = {
        "id": new_id,
        "mssv": data["mssv"].strip(),
        "ho_ten": data["ho_ten"].strip(),
        "lop": data["lop"].strip(),
        "diem": diem
    }

    students.append(new_student)

    write_students(students)

    return jsonify(new_student), 201



if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))

    app.run(
        host="0.0.0.0",
        port=port
    )
