class Report:
    """
    A Report object contains all the questions
    and answers associated with a report.
    """
    def __init__(self, questions):
        self.questions_and_answers = {}
        for question in questions:  #enter in data with association by using dict 
            self.questions_and_answers[question] = []
   
    def save_answer(self, question, answer):
        if question not in self.questions_and_answers:
            msg = 'Question "{}" not in list of questions'.format(question)
            raise KeyError(msg)
        self.questions_and_answers[question].append(answer)
    
    def __repr__(self):
        return '<Report: {} questions>'.format(len(self.questions_and_answers))    
    
    def __str__(self):
        ret_str = ''
        for question, answers in self.questions_and_answers.items():
            ret_str += str(question) + '\n' #ret_str = ret_str + str(question)
            for answer in answers:
                ret_str += '    ' + str(answer) + '\n'
        return ret_str
        


class Question: 
    def __init__(self, text):
        self.text = text 
    def __repr__(self):
        return '<>'.format(self.text)
    def __str__(self):
        return self.text 

class Answer: 
    def __init__(self, text):
        self.text = text 
   
    def __repr__(self):
        return '<Answer: {}>'.format(self.text)
    
    def __str__(self):
        return self.text


#tuple    
questions = (
    Question('How are you today?'),
    Question('What is your fav color?'),
    Question('Is S&P short for slurpies and pop?'),
)

report = Report(questions) #pass questions to instance of Report 

#for each report, iterate thru every question 
for question, answers in report.questions_and_answers.items():
    print(question)
    answer_text = True #jump into loop at least once 
    while answer_text:
        answer_text = input('> ')
        answer_text = answer_text.strip() #removes whitespace before and after string
        if answer_text: #not empty
            answer = Answer(answer_text) #create Answer obj 
            answers.append(answer) #stretch list 
        
print()
print(report)
