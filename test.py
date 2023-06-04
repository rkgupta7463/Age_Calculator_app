import datetime

def calculate_age(birth_year, birth_month, birth_day):
    current_date = datetime.date.today()
    if birth_year & birth_month & birth_day > 0: 
        birth_date = datetime.date(birth_year, birth_month, birth_day)
        age = current_date - birth_date
        years = age.days // 365
        months = (age.days % 365) // 30
        days = (age.days % 365) % 30
        print("Your age is: {} years, {} months, and {} days".format(years, months, days))
    else:
        message="Year , month and, days is not invalid!"    
        print(message)
    # Display the result

# Prompt the user to enter their birth date
birth_year = int(input("Enter your birth year: "))
birth_month = int(input("Enter your birth month: "))
birth_day = int(input("Enter your birth day: "))

# Calculate the age
calculate_age(birth_year, birth_month, birth_day)


