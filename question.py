class Question:
    def __init__(self, prompt, options, answer):
        self.prompt = prompt
        self.options = options
        self.answer = answer

    def check_answer(self, user_answer):
        return user_answer.lower() == self.answer.lower()
