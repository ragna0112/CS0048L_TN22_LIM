print("\nStudent Grading Calculator")

def menu():
    print("\nMenu:")
    print(" 1. Add Score")
    print(" 2. Calculate Average")
    print(" 3. Exit")

def add_score(scores):
    subject = input(" Enter the subject: ")
    score = input(" Enter the score: ")

    if score.isdigit():
        scores[subject] = int(score)
        print(" Score is added.")
    else:
        print(" Enter a number score.")

def calculate_average(scores):
    if scores:
        average = sum(scores.values()) / len(scores)
        print(f"Average Grade: {average:.2f}")
    else:
        print("No scores available to calculate average.")

def main():
    scores = {}
    while True:
        menu()
        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            add_score(scores)
        elif choice == '2':
            calculate_average(scores)
        elif choice == '3':
            print("Thank you for using the student grade calculator.")
            break
        else:
            print("Invalid choice. Choose from (1-3).")

main()
