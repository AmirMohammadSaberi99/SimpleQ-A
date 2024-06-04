from question import Question

class Quiz:
    def __init__(self):
        self.questions = []
        self.score = 0

    def add_question(self, question):
        self.questions.append(question)

    def start(self):
        for i, question in enumerate(self.questions):
            print(f"\nQuestion {i + 1}: {question.prompt}")
            for j, option in enumerate(question.options):
                print(f"{chr(65 + j)}. {option}")
            answer = input("Your answer: ").strip()
            if question.check_answer(answer):
                print("Correct!")
                self.score += 1
            else:
                print(f"Wrong! The correct answer is {question.answer}")
        self.show_score()

    def show_score(self):
        print(f"\nYour final score is {self.score}/{len(self.questions)}")
