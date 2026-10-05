print("========================================")
print("    HEALTHCARE TEXT ANALYZER")
print("========================================")

symptom = input("Enter your symptoms: ")

text = symptom.lower()

print("\n----------------------------------------")
print("Entered Symptoms:")
print(symptom)

if "fever" in text and "cough" in text:
    print("\nPossible Condition: Common Flu")
    print("Advice: Take adequate rest and stay hydrated.")

elif "headache" in text and "cold" in text:
    print("\nPossible Condition: Common Cold")
    print("Advice: Take rest and drink warm fluids.")

elif "stomach pain" in text or "stomach ache" in text:
    print("\nPossible Condition: Digestive Problem")
    print("Advice: Drink enough water and eat light food.")

elif "sore throat" in text and "cough" in text:
    print("\nPossible Condition: Throat Infection")
    print("Advice: Drink warm fluids and get proper rest.")

elif "body pain" in text and "fever" in text:
    print("\nPossible Condition: Viral Infection")
    print("Advice: Rest and stay hydrated.")

elif "headache" in text:
    print("\nPossible Condition: Headache")
    print("Advice: Take rest and stay hydrated.")

elif "cough" in text:
    print("\nPossible Condition: Cough/Respiratory Problem")
    print("Advice: Drink warm fluids and monitor your symptoms.")

else:
    print("\nNo matching condition found.")
    print("Please consult a qualified healthcare professional.")

print("\nNote: This application is for educational purposes only.")
print("----------------------------------------")