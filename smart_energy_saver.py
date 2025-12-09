import random

# Simulated data
appliances = {
    "ac": 6,
    "tv": 4,
    "fridge": 24,
    "washing machine": 1
}

power = {
    "ac": 1.5,
    "tv": 0.1,
    "fridge": 0.2,
    "washing machine": 0.5
}

TARIFF = 60  # LKR per kWh

tips = [
    "Use LED bulbs to reduce electricity usage.",
    "Turn off appliances completely instead of standby.",
    "Use your washing machine only with full loads.",
    "Reduce AC usage during the daytime.",
    "Unplug chargers when not in use."
]

# Welcome message
print("🤖 Welcome to Smart Energy Saver Chatbot!")
print("You can ask me things like:")
print(" - Show my usage")
print(" - Give me suggestions")
print(" - What is my electricity cost?")
print(" - Give me a tip")
print(" - Exit\n")

while True:
    user = input("You: ").lower()

    # Exit
    if "exit" in user or "bye" in user:
        print("\nBot: Goodbye! Save energy 🌱")
        break

    # Usage
    elif "usage" in user or "show" in user:
        print("\nBot: Here is your appliance usage:")
        for a, h in appliances.items():
            print(f" - {a.title()}: {h} hours/day")

    # Suggestions
    elif "suggest" in user or "save" in user:
        print("\nBot: Here are some energy-saving suggestions:")
        if appliances["ac"] > 5:
            print(" - Reduce AC usage to 4 hours/day.")
        if appliances["tv"] > 3:
            print(" - Reduce TV screen time.")
        print(" - Turn off lights when not in use.")
        print(" - Use washing machine only with full loads.")

    # Cost
    elif "cost" in user or "bill" in user:
        total = 0
        for a in appliances:
            total += appliances[a] * 7 * power[a] * TARIFF

        print(f"\nBot: Your estimated weekly electricity cost is: LKR {total:.2f}")
        print(f"Bot: If you follow my tips, you can save about LKR {total * 0.10:.2f} per week.")

    # Tips
    elif "tip" in user:
        print("\nBot Tip:", random.choice(tips))

    # Unknown input
    else:
        print("\nBot: Sorry, I didn't understand that.")
        print("Try asking: usage, suggestions, cost, or tip.\n")
