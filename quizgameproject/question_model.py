class Question:
    def __init__(self,q_text,q_answer):
        self.text=q_text
        self.answer = q_answer 

myque = Question("hello","this is the answer")
print(myque.text,myque.answer)