from quiz import Quiz
from question import Question

def main():
    quiz = Quiz()

    # Add questions to the quiz
    quiz.add_question(Question(
        "What is the capital of France?",
        ["Paris", "London", "Berlin", "Madrid"],
        "A"
    ))
    quiz.add_question(Question(
        "Who wrote 'To Kill a Mockingbird'?",
        ["Harper Lee", "Mark Twain", "J.K. Rowling", "Ernest Hemingway"],
        "A"
    ))
    quiz.add_question(Question(
        "What is the largest planet in our solar system?",
        ["Earth", "Mars", "Jupiter", "Saturn"],
        "C"
    ))

    # Start the quiz
    quiz.start()

if __name__ == "__main__":
    main()
