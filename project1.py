def quiz_game():
    # List of questions, options, and answers
    questions = [
        {
            "question": "What is the capital of India?",
            "options": ["A) New delhi", "B) London", "C) Berlin", "D) Madrid"],
            "answer": "A"
        },
        {
            "question": "What is 2 + 2 and 2*2?",
            "options": ["A) 3", "B) 4", "C) 5", "D) 6"],
            "answer": "B"
        },
        {
            "question": "What is the capital of Spain?",
            "options": ["A) Lisbon", "B) Madrid", "C) Rome", "D) Athens"],
            "answer": "B"
        },
        {
            "question": "What is 5 * 6?",
            "options": ["A) 28", "B) 29", "C) 30", "D) 31"],
            "answer": "C"
        },
        {
            "question": "What is the largest planet in our solar system?",
            "options": ["A) Earth", "B) Mars", "C) Jupiter", "D) Saturn"],
            "answer": "C"
        },
        {
            "question": "who was the captain of india in 2024 T20 world cup?",
            "options": ["A) Rohit Sharma","B) Kl Rahul","C) Virat Kohli","D) hardik pandya"],
            "answer":"A"
        },
        {
            "question":"what is the national animal of India?",
            "options":["A) zebra","B) elephant","C) Lion","D) Tiger"],
            "answer": "D"
        },
        {
            "question":"In IPL till now which team had not won a single trophy?",
            "options":["A)RCB","B)CSK","C)MI","D)RR"],
            "answer":"A"
        },
        {
            "question":"How many wonders of world are there till the date?",
            "options":["A)7","B)4","C)5","D)8"],
            "answer":"A"
        },
        {
            "question":"after how many years lob sabha election will conduct?",
            "options":["A)6","B)6","C)8","D)5"],
            "answer":"D"
        }
    ]

    score = 0
    i=0

    print("Welcome to the Quiz Game!")
    print("You will be asked a series of multiple-choice questions. Try to answer them correctly.")

    for i, q in enumerate(questions):
        print(f"\nQuestion {i + 1}: {q['question']}")
        for option in q["options"]:
            print(option)
        
        user_answer = input("Your answer (A, B, C, or D): ").upper() 
        
        if user_answer == q["answer"]:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is {q['answer']}.")

    print(f"\nYour final score is {score} out of {len(questions)}.")
    print("Thank you for playing!")

quiz_game()