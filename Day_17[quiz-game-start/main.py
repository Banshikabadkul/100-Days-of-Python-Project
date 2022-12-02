from question_model import Question
from data import question_data

question_bank = []

for i in question_data:
    q1 = i["text"]
    ai = i["answer"]
    new_que = Question(q1, a1)
    question_bank.append(new_que)


