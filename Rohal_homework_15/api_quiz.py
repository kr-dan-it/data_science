from flask import Flask, jsonify, request
import json
import random

app = Flask(__name__)

with open("quiz_questions.json", "r") as file:
    questions = json.load(file)

@app.route('/questions', methods=["GET"])
def main_page():
    return jsonify({"About": "There is 10 questions",
                    "How": "Enter the answer you think is correct from the list.",
                    "Start": "enter '/questions/1' to begin"}), 200

@app.route('/questions/<int:question_id>', methods=["GET"])
def get_q(question_id):
    for question in questions["Questions"]:
        if question_id == question["id"]:
            return jsonify(question["question"], question["answers"])
    return jsonify({"error": "Question not found"}), 404

@app.route('/questions/<int:question_id>', methods=["POST"])

def answer(question_id):
    current_q = None

    for i, question in enumerate(questions["Questions"]):
        if question_id == question["id"]:
            current_q = question
            break

    answer = request.json["answer"]

    if answer == current_q["correct_answer"]:
        question_id += 1
        return jsonify("Correct!"), 200

    else:
        return jsonify("Wrong answer :("), 200

if __name__ == "__main__":
    app.run(debug=True)