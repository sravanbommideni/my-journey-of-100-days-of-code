from quiz_brain import QuizBrain
from question_model import Question
from data import question_data

question_bank = []

for q in question_data:
    question = Question(q['question'],q['correct_answer'])
    question_bank.append(question)

quiz_brain = QuizBrain(question_bank)

while quiz_brain.still_has_questions() :
    quiz_brain.next_question()

print("you have completed the Quiz")
print(f"your final score is : {quiz_brain.score}/{len(question_bank)}")