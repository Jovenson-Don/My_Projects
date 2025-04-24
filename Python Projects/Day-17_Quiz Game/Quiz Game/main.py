# Import question data from the data module
from data import question_data

# Import the Question class from the question_model module
from question_model import Question

# Import the QuizBrain class from the quiz_brain module
from quiz_brain import QuizBrain

# Initialize an empty list to hold Question objects
question_bank = []

# Loop through each question in the question data
for question in question_data:
    # Extract the question text and the correct answer
    question_text = question["question"]
    question_answer = question["correct_answer"]

    # Create a new Question object with the extracted data
    new_question = Question(question_text, question_answer)

    # Add the new Question object to the question bank
    question_bank.append(new_question)

# Create a QuizBrain object with the question bank
quiz = QuizBrain(question_bank)

# Loop through the questions while there are still questions left
while quiz.still_has_questions():
    quiz.next_question()

# Print a message when the quiz is completed
print(f"You've completed the quiz!")
print(f"Final score is: {quiz.score}/{quiz.question_number}")
