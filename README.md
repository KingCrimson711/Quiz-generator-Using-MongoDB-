# Quiz Generator Using MongoDB

This project is a **Quiz Generator** that allows users to generate quizzes dynamically based on the number of marks specified for MCQs and subjective questions. It uses **Flask for the backend**, **MongoDB for storing questions**, and a simple **HTML + JavaScript frontend** for user interaction.

---

## Features

- Dynamically generates quizzes based on user inputs.
- Supports **MCQs** and **Subjective Questions**.
- Stores questions in a **MongoDB database**.
- Allows teachers to specify total marks and question distribution.

---

## Setup Instructions

### 1. Install MongoDB

MongoDB is required to store and retrieve quiz questions.

- **Install MongoDB**: Download and install from [MongoDB Official Website](https://www.mongodb.com/try/download/community).
- **Run MongoDB**: Start the MongoDB service using:
  ```sh
  mongod --dbpath /path/to/database
  ```
- **Connect to MongoDB**:
  ```sh
  mongo
  ```

### 2. Clone the Repository

```sh
git clone https://github.com/KingCrimson711/Quiz-generator-Using-MongoDB.git
cd Quiz-generator-Using-MongoDB
```

### 3. Set Up a Virtual Environment (Recommended)

```sh
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 4. Install Dependencies

```sh
pip install -r requirements.txt
```

### 5. Configure MongoDB Connection

Ensure MongoDB is running and update the connection string in `app.py` if needed:

```python
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["question"]
```

### 6. Run the Application

```sh
python app.py
```

### 7. Open in Browser

Visit [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser.

---

## MongoDB Database Structure

The **MongoDB database** (`question`) contains two collections: `mcqs` and `subjective`.

### `mcqs` Collection (For Multiple Choice Questions)

Each MCQ document follows this structure:

```json
{
    "_id": ObjectId("67a2048663ddccb722170a53"),
    "question": "Who is considered an innovative entrepreneur?",
    "options": ["Option 1", "Option 2", "Option 3", "Option 4"],
    "answer": "Someone who introduces new products or methods",
    "correct_answer": 1,
    "topic": "Types of Entrepreneurs",
    "difficulty": "Easy"
}
```

### `subjective` Collection (For Subjective Questions)

Each Subjective question document follows this structure:

```json
{
    "_id": ObjectId("67a4c1712be28e29df67a707"),
    "marks": 2,
    "question": "Define entrepreneurship in your own words."
}
```

---

## How It Works

1. User enters **marks distribution** (MCQs & Subjective).
2. The application fetches relevant questions from **MongoDB**.
3. A quiz is dynamically generated and displayed.
4. The quiz can be exported or saved for future use.

---

### Future Enhancements

- Add authentication for teachers.
- Implement AI-generated questions.
- Support for different quiz formats (PDF, Word export).

---

