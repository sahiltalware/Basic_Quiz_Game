#BASIC QUIZ GAME USING PYTHON PROGRAMMING

# LIST OF QUESTIONS, OPTIONS AND ANSWERS
questions = ("1.who developed python programing language:",
             "2.what is the extenction of python file ?:",
             "3.which type of programming does python support ?:",
             "4.which of the following is not a core data type ?",
             "5.which keyword is used for function in python language ?")
options = (("A.Wick van Rossum", "B.Rasmus Lerdorf", "C.Guido van Rossum", "D.Niene Stom"),
           ("A. .python", "B. .pl", "C. .py", "D. .p"),
           ("A.object-oriented programming", "B.structured programming", "C.functional programming", "D.all of the above"),
           ("A.Lists", "B.Dictionary", "C.Tuples", "D.Class"),
           ("A.Function", "B.def", "C.Fun", "D.Define"))

answers = ("C", "C", "A", "D","B")

guesses = []

# Track of correct answer
score = 0

question_num = 0

for question in questions:

    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("enter your choice:").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score+=1
        print("correct")
    else:
        print("incorrect")
        print(f"{answers[question_num]} is the correct answer")

    question_num += 1

print("---------------")
print("    result     ")
print("---------------")

# we iterate the answers and guesses
print("answers:", end="")
for answer in answers:
    print(answer, end="")
print()

print("guesses: ", end="")
for guess in guesses:
    print(guess, end="")
print()

# Print Final Score
print("SCORE:", score)
score = int(score / len(questions) * 100)
print(f"Your score in % is: {score}%")