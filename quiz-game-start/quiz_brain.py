class QuizzBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list


    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        q = self.question_list[self.question_number]
        self.question_number += 1
        answer = input(print(f"Q.{self.question_number}: {q.text} (True/False)?:"))
        self.check_answer(answer, q.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("you got it right!")
            self.score += 1
        else:
            print("That's wrong.")
        print(f"The correct answer was {correct_answer}.")
        print(f"Your current score is {self.score}.")