from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient
import random
import os

app = Flask(__name__)

client = MongoClient("mongodb://localhost:27017/")
db = client["questions"]
mcqs_collection = db["MCQs"]
subjective_collection = db["Subjective"]

if not os.path.exists("generated_quizzes"):
    os.makedirs("generated_quizzes")

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        mcq_marks = int(request.form['mcq_marks'])
        num_2_marks = int(request.form['marks_2'])
        num_3_marks = int(request.form['marks_3'])
        num_5_marks = int(request.form['marks_5'])

        # Calculate total marks dynamically
        total_marks = mcq_marks + (num_2_marks * 2) + (num_3_marks * 3) + (num_5_marks * 5)

        # Fetch MCQs
        mcq_questions = list(mcqs_collection.find())
        selected_mcqs = random.sample(mcq_questions, min(mcq_marks, len(mcq_questions)))

        # Fetch subjective questions
        subjective_questions = []
        for marks, num_questions in [(2, num_2_marks), (3, num_3_marks), (5, num_5_marks)]:
            questions = list(subjective_collection.find({"marks": marks}))
            selected = random.sample(questions, min(num_questions, len(questions)))
            subjective_questions.extend(selected)

        # Generate the quiz content
        generated_quiz = "Generated Quiz:\n\n"

        # MCQ Section
        generated_quiz += "MCQ Section:\n"
        for idx, mcq in enumerate(selected_mcqs):
            generated_quiz += f"{idx + 1}. {mcq['question']}\n"
            for i, option in enumerate(mcq['options']):
                generated_quiz += f"   {chr(65 + i)}. {option}\n"
            generated_quiz += "\n"

        # Subjective Section
        generated_quiz += "Subjective Section:\n"
        for idx, subj in enumerate(subjective_questions, start=len(selected_mcqs) + 1):
            generated_quiz += f"{idx}. {subj['question']} ({subj['marks']} marks)\n"

        # Save the quiz
        with open('generated_quizzes/generated_quiz.txt', 'w') as f:
            f.write(generated_quiz)

        return render_template('quiz.html', quiz_content=generated_quiz, total_marks=total_marks)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
