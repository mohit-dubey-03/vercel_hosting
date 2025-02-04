from flask import Flask, request, jsonify
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)  # This enables CORS for all routes

# Load student data
with open("q-vercel-python.json", "r") as file:
    student_data = json.load(file)

student_marks = {student["name"]: student["marks"] for student in student_data}

@app.route('/')
def home():
    return "Hello, World!"

@app.route('/api', methods=['GET'])
def get_marks():
    # Get list of names from query parameters
    names = request.args.getlist('name')
    
    if not names:
        # Return an error if no names are provided
        return jsonify({
            "error": "No names provided. Use ?name=... in the URL."
        }), 400  # Bad Request status code
    
    # Lookup marks for each name
    marks = []
    for name in names:
        mark = student_marks.get(name)
        if mark is None:
            # Optionally handle unknown names, here we append None
            marks.append(None)
        else:
            marks.append(mark)
    
    return jsonify({
        "marks": marks,
        "names_searched": names
    })

if __name__ == "__main__":
    app.run(debug=True)