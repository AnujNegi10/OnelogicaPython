from question_model import Question
from data import question_data

from quiz_brain import Brain

question_bank = []
for question in question_data:
    ques_text = question["text"]
    ques_answer = question["answer"]
    
    new_ques = Question(ques_text,ques_answer)
    question_bank.append(new_ques)

quiz = Brain(question_bank)

quiz.next_ques()