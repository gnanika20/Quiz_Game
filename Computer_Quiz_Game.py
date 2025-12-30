import sys
print("Hello, Welcome to the quiz game!")
score=0
wrong=0
ready=input("Are you ready to play?(yes/no):")
if ready.lower()!="yes":
    print("No problem!Comeback when you are ready :)")
    sys.exit()
print("\n Okay! Let's start the quiz")
print("\nIf you give 3 wrong answers then the game is over.\n")
Q1=input("1) What does RAM stand for?\n").strip().lower()
if Q1=="random access memory":
    print("Correct Answer!")
    score+=1
else:
    print("Wrong Answer! Correct answer is random access memory")
    wrong+=1 
Q2=input("1) What does R0M stand for?\n").strip().lower()
if Q2=="read only memory":
    print("Correct Answer!")
    score+=1
else:
    print("Wrong Answer! Correct answer is read only memory")
    wrong+=1 
Q3=input("1) What does OS stand for?\n").strip().lower()
if Q3=="operating system":
    print("Correct Answer!")
    score+=1
else:
    print("Wrong Answer! Correct answer is operating system")
    wrong+=1 
if wrong==3:
    print("\nYou gave 3 wrong answers...GAME OVER!")
    sys.exit()
Q4=input("1) What is the brain of the computer?\n").strip().lower()
if Q4=="cpu":
    print("Correct Answer!")
    score+=1
else:
    print("Wrong Answer! Correct answer is cpu")
    wrong+=1 
if wrong==3:
    print("\nYou gave 3 wrong answers...GAME OVER!")
    sys.exit()
Q5=input("1) What does CPU stand for?\n").strip().lower()
if Q5=="central processing unit":
    print("Correct Answer!")
    score+=1
else:
    print("Wrong Answer! Correct answer is central processing unit")
    wrong+=1 
print("\nQuiz Completed :)")
print("Correct Answers:",score)
print("Wrong Answers:",wrong)
if score>=4:
    print("Excellent performance")
elif score >=3:
    print("Good Job")
else:
    print("Needs Improvement :)")