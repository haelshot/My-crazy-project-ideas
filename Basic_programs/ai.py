Questions = ['hi', 'how are you ?', 'good', 'do you want to talk about it ?',
             'okay i respect your decision', 'alright lets talk', 'okay',
             'ohh', 'i am sorry', 'you will be alright trust me']
Answers = ['hi', 'fine', 'i am not fine', 'yes', 'no', 'okay']
print('Enter your answers(the numbers they are numbered with) '
      'according to those series of answers below..... answers are in numbers')
class ai:
    def __init__(self, questions, answers):
        self.question = questions
        self.answer = answers
        num = 0
        for answer in Answers:
            num += 1
            print(f'{num}. {answer}')
        x = 0
        for question in Questions:
            print(Questions[x])
            x += 1
            user_input = input('Enter your answer: ')
            if user_input == 'i am not fine' or user_input == 'im not fine' or user_input == 'am not fine':
                x += 1
            if user_input == 'yes' or user_input == 'yeah':
                x += 1
                input("Talk to me: ")
                x += 1
                for quest in range(2):
                    x += 1
                    print(Questions[x])
            if user_input == 'no' or user_input == 'not really':
                x = x


ai_prompt = ai(Questions, Answers)
