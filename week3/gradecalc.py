score = int(input("Please enter your score (0–100): "))

# Determine the grade

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"\nYour grade: {grade}")

# Personal feedback

feedback = {
    "A": "Fantastic performance! Keep it up!",
    "B": "Great job! You’re close to the top.",
    "C": "Good work – with a bit more effort you can improve.",
    "D": "You passed, but some extra practice would help.",
    "F": "Don’t give up! Everyone has tough days."
    }

print(feedback[grade])
