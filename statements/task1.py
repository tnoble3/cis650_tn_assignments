name = input("Enter your name: ").strip()
age = int(input("Enter your age: ")).strip()
#creating an age validation function
def validateAge(age):
    if age <= 0:
        print("You are not born yet.")
    elif age < 18:
        print("You are a minor.")
    elif age <= 99:
        print("You are an adult. ")
    else: 
        print("Nice to meet you.") 
        
#verifying the traits of the input
if name == "":
    print("Name cannot be blank.")
else:
    try:
        age = int(age)
    except ValueError:
        print("Age must be a number.")
    else:
        if name.lower() != "trinity":
            print("This program can only be used by Trinity")
        else:
            validateAge(age)