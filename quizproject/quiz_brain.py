class QuizBrain:
    def __init__(self,q_list):
        self.question_number=0
        self.score=0
        self.question_list=q_list
    def still_has_question(self):
        return self.question_number < len(self.question_list)
    def next_question(self):
        current_question=self.question_list[self.question_number]
        self.question_number+=1
        choice=input(f"Q{self.question_number}. {current_question.text} (True/False) : ")
        self.check_answer(choice,current_question.answer)
    def check_answer(self,choice,correct_answer):
        if choice.lower()==correct_answer.lower():
            print("Your answer is correct!")
            self.score+=1
        else:
            print("Your answer is wrong!")
        print(f"The correct answer is {correct_answer}")
        print(f"Your current score is {self.score}/{self.question_number}")
        print("\n")