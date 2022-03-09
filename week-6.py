isTeacher = True
isOver65 = True
haveMedicalCondition = False
vaccination = True

print("Vaccination Check")
print()
question1 = input("Are you a teacher? Answer yes or no. ")
question2 = input("Are you over 65? Answer yes or no. ")
question3 = input("Do you medical condition? Answer yes or no. ")
print()



if question1 == 'yes' and question2 == 'yes' and question3 == 'no':
    print("Is a teacher = ", isTeacher)
    print("Is over 65 = ", isOver65)
    print("Has a medical condition = ", haveMedicalCondition)
    print("Can be give a vaccine = ", vaccination)
    print()
    print("Congrats, you qualify for a vaccine")
    print()
else:
    print("Sorry you don't qualify for a vaccine.")