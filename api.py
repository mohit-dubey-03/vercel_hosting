from flask import Flask, request, jsonify
from flask_cors import CORS
import json

# Initialize the Flask app and enable CORS
app = Flask(__name__)
CORS(app)

# Load marks data from the JSON file
with open("q-vercel-python.json", "r") as file:
    student_data = json.load(file)

# Convert the list of students into a dictionary for fast lookup
student_marks = {student["name"]: student["marks"] for student in student_data}

# Endpoint to get marks by name
@app.route('/', methods=['GET'])
def home():
    return "Hello, World!"

@app.route('/api', methods=['GET'])
def get_marks():
    names = request.args.getlist("name")
    marks = []

    # Lookup marks for each name
    for name in names:
        marks.append(student_marks.get(name, None))  # Return None if the student is not found

    return jsonify({"marks": marks})

if __name__ == "__main__":
    app.run(debug=True)
