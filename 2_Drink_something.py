person_age = int(input())
age_drink = ""

if person_age <= 14:
    age_drink = "drink toddy"
elif person_age <= 18:
    age_drink = "drink coke"
elif person_age <= 21:
    age_drink = "drink beer"
else:
    age_drink = "drink whisky"

print(age_drink)