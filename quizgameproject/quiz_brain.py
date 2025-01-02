class Brain:
    def __init__(self,q_list):
        self.ques_num =0
        self.ques_list= q_list
        
    def next_ques(self):
        curr_ques = self.ques_list[self.ques_num]
        
        self.ques_num +=1
        
        input(f"Q{self.ques_num}: {curr_ques.text}(True/False): ")