class QuizBrain:

    def __init__(self,liist):
        self.question_list=liist
        self.question_number=0
        self.score=0

    def still_has_questions(self):
        if self.question_number==len(self.question_list):
            return False
        else:
            return True

    def next_question(self):
        quest=self.question_list[self.question_number]
        self.question_number+=1
        user_input=input(f"Q.{self.question_number} : {quest.text} (True/False) ?\n>").lower()
        while user_input not in ['true','false']:
            user_input = input(f"enter a valid input\n>").lower()
        self.check_answer(user_input,quest.answer)

    def check_answer(self,user_answer,crct_answer):
        if user_answer==crct_answer.lower():
            self.score+=1
            print("you got it right.")
            print(f"score : {self.score}/{self.question_number}\n")
        else:
            print("sorry...you are wrong")
            print(f"score : {self.score}/{self.question_number}\n")