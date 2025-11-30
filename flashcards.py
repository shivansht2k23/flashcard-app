import json
import random
import os

FLASHCARDS_FILE = "flashcards.json"


def load_flashcards():
    if os.path.exists(FLASHCARDS_FILE):
        with open(FLASHCARDS_FILE, "r") as f:
            return json.load(f)
    return {}


def save_flashcards(cards):
    with open(FLASHCARDS_FILE, "w") as f:
        json.dump(cards, f, indent=4)


def add_flashcard(cards):
    question = input("Enter the question: ")
    answer = input("Enter the answer: ")
    cards[question] = answer
    save_flashcards(cards)
    print("Flashcard added!\n")


def quiz(cards):
    if not cards:
        print("No flashcards available yet!\n")
        return

    questions = list(cards.keys())
    random.shuffle(questions)

    score = 0
    for q in questions:
        print(f"\nQ: {q}")
        user_answer = input("Your answer: ")

        if user_answer.strip().lower() == cards[q].lower():
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Wrong! Correct answer: {cards[q]}")

    print(f"\nYour final score: {score}/{len(cards)}\n")


def view_flashcards(cards):
    if not cards:
        print("No flashcards yet!\n")
        return

    print("\n=== All Flashcards ===")
    for q, a in cards.items():
        print(f"- {q} → {a}")
    print()


def menu():
    cards = load_flashcards()

    while True:
        print("\n=== FLASHCARD QUIZ APP ===")
        print("1. Add a flashcard")
        print("2. Take a quiz")
        print("3. View all flashcards")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_flashcard(cards)
        elif choice == "2":
            quiz(cards)
        elif choice == "3":
            view_flashcards(cards)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.\n")


menu()
