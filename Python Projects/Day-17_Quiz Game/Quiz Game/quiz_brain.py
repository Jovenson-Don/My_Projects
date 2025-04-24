# Define the QuizBrain class to manage the quiz behavior
class QuizBrain:

    # Initialize with a list of Question objects
    def __init__(self, question_list):
        self.question_number = 0  # Track the current question index
        self.question_list = question_list  # Store the list of questions
        self.score = 0  # Initialize the quiz score

    # Check if there are still questions left to ask
    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    # Present the next question to the user
    def next_question(self):
        # Get the current question based on the question number
        current_question = self.question_list[self.question_number]
        self.question_number += 1  # Increment the question number

        # Prompt the user for an answer
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False:) ")

        # Check if the user's answer is correct
        self.check_answer(user_answer, current_question.answer)

    # Compare the user's answer to the correct answer
    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1  # Increase the score if correct
        else:
            print("You got it wrong.")

        # Print the current score and the correct answer
        print(f"{self.score}/{self.question_number}")
        print(f"The correct answer is: {correct_answer}")
        print("\n")  # Add a line break for readability
