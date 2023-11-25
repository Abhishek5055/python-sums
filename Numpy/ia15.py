from datetime import date

def calculate_age_in_days(birthdate):
    today = date.today()
    age = today - birthdate
    return age.days

# Replace 'YYYY-MM-DD' with your actual birthdate in ISO format.
birthdate_str = "2000-01-01"
birthdate = date.fromisoformat(birthdate_str)

age_in_days = calculate_age_in_days(birthdate)
print("You are", age_in_days, "days old.")
