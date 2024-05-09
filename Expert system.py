questions = {
    "What is the capital of France?": {
        "options": ["A. Paris", "B. London", "C. Berlin", "D. Rome"],
        "answer": "A"
    },
    "Which planet is known as the Red Planet?": {
        "options": ["A. Venus", "B. Mars", "C. Jupiter", "D. Saturn"],
        "answer": "B"
    },
    "Who wrote 'Romeo and Juliet'?": {
        "options": ["A. William Shakespeare", "B. Charles Dickens", "C. Jane Austen", "D. Mark Twain"],
        "answer": "A"
    }
}
def quiz():
    score = 0
    for question in questions:
        print(question)
        for option in questions[question]["options"]:
            print(option)
        answer = input("Enter your answer (A/B/C/D): ").upper()
        if answer == questions[question]["answer"]:
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is:", questions[question]["answer"])
    print("You got", score, "out of", len(questions), "questions correct.")
quiz()
