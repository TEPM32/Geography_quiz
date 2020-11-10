from Question import Question

question_prompts = [
    "1. What is the capital of Lithuania?\n(a) Vilnius\n(b) Riga\n(c) Tallin\n(d) Helsinki\n\n",
    "2. What is the highest mountain of Croatia?\n(a) Medvednica\n(b) Papuk\n(c) Dinara\n(d) Velebit\n\n",
    "3. Which country isn't in Africa?\n(a) Kenya\n(b) Botswana\n(c) Belize\n(d) Falkland Islands\n\n",
    "4. What is the capital of Kyrgyzstan\n(a) Dushanbe\n(b) Tashkent\n(c) Bishkek\n(d) Kabul\n\n",
    "5. Which lake is not located in Russia? \n(a) Baikal\n(b) Enare\n(c) Caspian\n(d) Onega\n\n",
    "6. Which country is not covered by Altai mountains?\n(a) Russia\n(b) Mongolia\n(c) Kazakhstan\n(d) Uzbekistan\n\n",
    "7. Which U.S. state is largest by area?\n(a) Alaska\n(b) Arizona\n(c) Texas\n(d) California\n\n",
    "8. Which sea is does not surround Italy\n(a) Adriatic\n(b) Ligurian\n(c) Balearic\n(d) Tyrrhenian\n\n",
    "9. Which of the following deserts is not a cold one?\n(a) Patagonian\n(b) Gobi \n(c) Atacama\n(d) Sonoran\n\n",
    "10. On the shores of which lake Chicago is located? \n(a) Ontario\n(b) Erie\n(c) Michigan\n(d) Saint-Jean\n\n",
    "11. What color does not appear on Norwegian flag?\n(a) Red\n(b) Yellow\n(c) Blue\n(d) White\n\n",
    "12. Which country is the smallest in the world?\n(a) Monaco\n(b) Vatican City\n(c) San Marino\n(d) Tuvalu\n\n",

]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "d"),
    Question(question_prompts[3], "c"),
    Question(question_prompts[4], "b"),
    Question(question_prompts[5], "d"),
    Question(question_prompts[6], "a"),
    Question(question_prompts[7], "c"),
    Question(question_prompts[8], "d"),
    Question(question_prompts[9], "c"),
    Question(question_prompts[10], "b"),
    Question(question_prompts[11], "b")
]


def run_test(questions):
    score = 0  # for tracking correct answers
    for question in questions:
        answer = input(question.prompt)
        if answer.lower() == question.answer:
            score += 1
        else:
            pass
    print("You got " + str(score) + "/" + str(len(questions)) + " correct.")
    if score == 0:
        print("How on earth...?")
    elif 0 < score <= 4:
        print("Better luck next time!")
    elif 4 < score <= 8:
        print("Not bad... But I bet you can do even better!")
    elif 8 < score <= 11:
        print("Welldone! You have a very good geography knowledge.")
    elif score == 12:
        print("Wow! You are a geowizard! Congratulations.")

    print("Game over.")


run_test(questions)

# if answer.lower != "a" or "b" or "c" or "d":
#    print("Invalid input. Please try again.")
#    print(question)   /// or run_test(questions[question]) ???
