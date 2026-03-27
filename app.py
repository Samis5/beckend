from flask import Flask, request, jsonify

app = Flask(__name__)

databaza = {
    "students": [
        {
            "id": 1,
            "name": "Peter Novák",
            "age": 18,
            "vyska": 175,
            "image": "https://picsum.photos/200?random=1"
        },
        {
            "id": 2,
            "name": "Marek Horváth",
            "age": 22,
            "vyska": 182,
            "image": "https://picsum.photos/200?random=2"
        },
        {
            "id": 3,
            "name": "Lucia Kováčová",
            "age": 19,
            "vyska": 168,
            "image": "https://picsum.photos/200?random=3"
        },
        {
            "id": 4,
            "name": "Jana Vargová",
            "age": 25,
            "vyska": 170,
            "image": "https://picsum.photos/200?random=4"
        },
        {
            "id": 5,
            "name": "Tomáš Tóth",
            "age": 30,
            "vyska": 185,
            "image": "https://picsum.photos/200?random=5"
        },
        {
            "id": 6,
            "name": "Adam Bielik",
            "age": 17,
            "vyska": 178,
            "image": "https://picsum.photos/200?random=6"
        },
        {
            "id": 7,
            "name": "Martin Šimko",
            "age": 28,
            "vyska": 190,
            "image": "https://picsum.photos/200?random=7"
        },
        {
            "id": 8,
            "name": "Eva Kráľová",
            "age": 21,
            "vyska": 165,
            "image": "https://picsum.photos/200?random=8"
        },
        {
            "id": 9,
            "name": "Filip Urban",
            "age": 26,
            "vyska": 180,
            "image": "https://picsum.photos/200?random=9"
        },
        {
            "id": 10,
            "name": "Dominik Krajč",
            "age": 16,
            "vyska": 172,
            "image": "https://picsum.photos/200?random=10"
        }
    ]
}


@app.route("/")
def home():
    return jsonify({"message": "Flask backend beží!"})

@app.route("/api")
def api():
    return jsonify(databaza)

@app.route("/api/students/<int:student_id>")
def find_students(student_id):
    for student in databaza["students"]:
        if student["id"] == student_id:
            return jsonify(student)
    return jsonify({"error": "Student not found"}), 404


if __name__ == "__main__":
    app.run(debug=True)