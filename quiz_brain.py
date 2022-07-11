class QuizBrain:
    def __init__(self,question_list):
        self.score = 0
        self.question_number = 0
        self.question_list = question_list

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, user, answer):
        while (user.lower() != 'true') and (user.lower() != 'false'):
            user = input('You typed wrong, please type either "True" or "False": ')
        return user.lower() == answer.lower()

    def next_question(self):
        current_question = self.question_list[self.question_number]
        number = self.question_number
        number += 1
        user = input(f"Q.{number}: {current_question.text} (True or False): ")
        if self.check_answer(user, current_question.answer):
            self.score += 1
        else:
            self.score += 0
        print(f"Score: {self.score}")
        self.question_number += 1


