from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


new_q = Question("hello", "False")
question_bank = []
for question in question_data:
    x = Question(question['text'], question['answer'])
    question_bank.append(x)

que = QuizBrain(question_bank)
# print(f"[{question_bank[3].text}], [{question_bank[0].answer}]")
# for i in question_bank:
#     print(i.text, i.answer)
while que.still_has_questions():
    que.next_question()
print(f"Score:{(que.score / len(question_bank)) * 100}%")
