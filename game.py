questions = ["Who's dd: ", "Who's oggy: "]
answers = ["a", "b"]
points = 0

print("Welcome to KBC")

def lifey(index):
    print(f"Lifeline: The answer is {answers[index]}") 
    return points

for i in range(len(questions)):
    a = input(questions[i])

    if a == answers[i]:
        points += 100
        print(f"Correct! You have won {points} points.")

    elif a == "life":
        points = lifey(i)

    elif a == "stop":
        print(f"Thanks for playing! You have won {points} points.")
        break

    else:
        print("Incorrect answer.")
else:
    print(f"Thanks for playing! You have won {points} points.")
