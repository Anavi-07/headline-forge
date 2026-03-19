import random
subjects = {
    "funny": [
        "A group of monkeys",
        "A lazy programmer",
        "A talking parrot",
        "A dog in a suit"
    ],
    "tech": [
        "An AI robot",
        "A mysterious hacker",
        "A startup founder",
        "A tech company"
    ],
    "famous": [
        "Virat Kohli",
        "Narendra Modi",
        "A billionaire",
        "A YouTuber"
    ]
}

actions = [
    "forgets their own speech",
    "orders food at 3 AM",
    "crashes a random party",
    "starts dancing in public",
    "creates chaos on social media",
    "accidentally goes live",
    "fails miserably but becomes famous"
]

places_or_things = [
    "in Mumbai",
    "in Delhi",
    "on Instagram",
    "on YouTube",
    "during a live stream",
    "at a press conference",
    "in a viral video",
    "at midnight",
    "inside a gaming room"
]

def generate_headline(category):
    subject = random.choice(subjects[category])
    action = random.choice(actions)
    place = random.choice(places_or_things)

    return f"📰 BREAKING NEWS: {subject} {action} {place}!"


print("🔥 Welcome to Headline Generator 🔥")

while True:
    print("\nChoose a category:")
    print("1. Funny")
    print("2. Tech")
    print("3. Famous")

    choice = input("Enter choice (1/2/3): ").strip()

    if choice == "1":
        category = "funny"
    elif choice == "2":
        category = "tech"
    elif choice == "3":
        category = "famous"
    else:
        print("❌ Invalid choice! Try again.")
        continue

    headline = generate_headline(category)
    print("\n" + headline)

    user_input = input("\nDo you want another headline? (yes/no): ").strip().lower()

    if user_input == "no":
        break

print("\n✨ Thanks for using the Headline Generator!")