#FUNCTIONS args and kwargs

#arguments

def display_name(*args):
    for args in args:
        print(args,end=" ")

display_name("dr.","sd","qewrf","ERJYD","JYDGDJH","JHGK")  

def multiply_numbers(*args):

    result=1
    for i in args:
        result*=i
    return result    

o=multiply_numbers(2, 3, 4)
print(o)

#sample programs in argsuments

#sample program 1
#average:
def average(*score):

    if not score:
        return 0
    else:
        return sum(score)/len(score)

print(average(20,30,40))
print(average())

#sample program 2
#small and big number finder

def find_small(*number):

    if not number:
        return 0
    
    elif number==0:
        return 0
    
    else:
        return min(number),max(number)
    

print(find_small(20,10,3,44))


#keywordarguments

#sample programs in keyword argsuments

#sample program 1
#detail

def print_user_detail(**detail):

    if not detail:
        return 0
    for i,j in detail.items():
        print(f"{i.upper()} - {j}")

        #return(f"{i.upper()} - {j}")
        #due to it will end when it calls so the  it will 
        # come out of the loop thats why we us ethe print function
print("-" * 15)
print(print_user_detail(name="shri",age=18,city="thanjore"))
print("-" * 15)

#sample program 2
#pet descriper
def animal(**get_user):

    for i,j in get_user.items():
        print(f"{i.upper()} : {j}")

print("-" * 15)
print(animal(name=input(),age=int(input()),breed=input(),colour=input()))
print("-" * 15)


#multiple return statements and if-else,loops ,multiple functions
# with if and else
def classify_temp(c):
    if c >= 30:
        return "Hot hot hot ! ! !\n"
    elif c >= 15:
        return "warm!!!\n"

    elif c>= 0:
        return "cold! ! !\n"

    else:
        return "freezee! ! ! ! !\n"

print(classify_temp(343)) 
print(classify_temp(44))
print(classify_temp(2))
print(classify_temp(-2))


#loops
def first_negative(numbers):
    index=0
    for num in numbers:
        if num < 0:
            return index
        else:
            if num > 0:
                return index
                index+=1
            elif num==0:
                return index
                index+=1
    return "not possible"        

print(first_negative([5,12,-3,8,-10]))
print(first_negative([13,-16,45,0]))
print(first_negative([45-0]))


# two distinct functions

#classroom projects
#FUNCTION 1
def score_obtain(score):

    if not score:
        return 0
    elif score>100:
        return 0
    elif score>90:
        return "S-RANK"

    elif score>80:
        return "A-RANK"

    elif score>=75:
        return "B-RANK"

    elif score>=65:
        return "C-RANK"

    elif score>=55:
        return "D-RANK"

    else:
        return "E-RANK"
#function 2
def process_classroom_performance(**student_score):
    S_RANK_count=0
    A_RANK_count=0
    B_RANK_count=0
    C_RANK_count=0
    D_RANK_count=0
    E_RANK_count=0

    for i,j in student_score.items():

        result=score_obtain(j)

        if result == "S-RANK":
            S_RANK_count += 1

        elif result == "A-RANK":
            A_RANK_count += 1

        elif result == "B-RANK":
            B_RANK_count += 1

        elif result == "C-RANK":
            C_RANK_count += 1

        elif result == "D-RANK":
            D_RANK_count += 1    

        else:
            E_RANK_count += 1

    return (
        S_RANK_count,
        A_RANK_count,
        B_RANK_count,
        C_RANK_count,
        D_RANK_count,
        E_RANK_count
    )    

S_RANK,A_RANK,B_RANK,C_RANK,D_RANK,E_RANK = process_classroom_performance(
    Alice=int(input()),
    Bob=int(input()),
    Charlie=int(input()),
    David=int(input()),
    Eve=int(input())
)

print("------Classroom Analysis Results------")
print(f"Students with S-RANKS: {S_RANK}")
print(f"Students with A-RANKS: {A_RANK}")
print(f"Students with B-RANKS: {B_RANK}")
print(f"Students with C-RANKS: {C_RANK}")
print(f"Students with D-RANKS: {D_RANK}")
print(f"Students with E-RANKS: {E_RANK}")
print("--------------------------------------")

#programs on both *args and **kwargs
#sample 1
def make_sandwich(*ingrediants,**options):
    print("Making sandwhich:")

    for ingrediant in ingrediants:
        print(f" - {ingrediant}")

    if options:
        print("options:")
        for i,j in options.items():
            print(f"{i} : {j}")

make_sandwich(" Turkey", " Swiss", " Lettuce", toasted=True, sauce="Mayonice")   

#sample proram 2
#random function
import random

# Computer choice
def computer_choice():

    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)


# Winner
def winner(user, computer):

    if user == computer:
        return "tie"

    elif ((user == "rock" and computer == "scissors") or
          (user == "paper" and computer == "rock") or
          (user == "scissors" and computer == "paper")):
        return "user"

    return "computer"


# Get user choice
def get_user():

    while True:
        user = input("ENTER USER'S CHOICE: ").lower()

        if user in ["rock", "paper", "scissors"]:
            return user

        elif user == "quit":
            return "quit"

        else:
            print("Invalid choice! Please enter rock, paper, scissors, or quit.")


# Main game
def play():

    user_point = 0
    computer_point = 0
    tie_point = 0

    print("-" * 20)
    print("WELCOME")
    print("-" * 20)

    while True:

        user = get_user()

        if user == "quit":
            break

        # Computer randomly chooses
        computer = computer_choice()

        print(f"Computer chose: {computer}")

        # Find winner
        result = winner(user, computer)

        if result == "tie":
            print("Tie round!\n")
            tie_point += 1

        elif result == "user":
            print("User won!\n")
            user_point += 1

        else:
            print("Computer won!\n")
            computer_point += 1

        # Display scoreboard
        print(f"Scoreboard -> You: {user_point} | Computer: {computer_point} | Ties: {tie_point}")
        print("-" * 40)

    print("-" * 15)
    print("GAME OVER")
    print("-" * 15)

    print(f"Final Score -> You: {user_point} | Computer: {computer_point} | Ties: {tie_point}")


if __name__ == "__main__":
    play()
