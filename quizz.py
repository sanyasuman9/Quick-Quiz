def quiz_game(): 
    questions = [
        {"question": "Where is the Living Root Bridge located?", "options": ["Meghalaya", "Assam", "Sikkim", "Bihar"], "answer": "Meghalaya"},
        {"question": "Which is not a song by Louis Tomlinson?", "options": ["Always You", "Adore You", "Chicago", "Only The Brave"], "answer": "Adore You"},
        {"question": "With whom did Hermione go to the Yule Ball with?", "options": ["Draco", "Harry", "Cedric", "Krum"], "answer": "Krum"},
        {"question": "Among these who is an Avenger?", "options": ["Superman", "Black Widow", "Flash", "Wonder Woman"], "answer": "Black Widow"},
    ]
    score = 0

    for q in questions:
        print(q["question"])
        for idx, option in enumerate(q["options"], 1):
            print(f"{idx}. {option}")
        
        try:
            answer = int(input("Choose the correct option (1-4): "))
            if answer < 1 or answer > 4:
                print("Please choose a number between 1 and 4.")
            elif q["options"][answer - 1] == q["answer"]:
                print("Correct!")
                score += 1
            else:
                print("Incorrect.")
        except ValueError:
            print("Invalid input. Please enter a number.")
        
        print()

    print(f"Your final score: {score}/{len(questions)}")
    if score == len(questions):
        print("Woohoo! You're a Champ! 🏆")
    elif score <= 1:
        print("Oh no, you can do better 😢")
    else:
        print("So close! Try again 💪")

quiz_game()
