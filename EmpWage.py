import random

def calculate_wage():
    wage = 0
    total_hours = 0
    working_days = 0
    max_hours = 100
    max_days = 20

    job_type = input("Enter the type of job (part/full): ").strip().lower()

    if job_type not in ["part", "full"]:
        print("Invalid job type. Please enter either 'part' or 'full'.")
        return 0

    hourly_rate = 20
    hours_per_day = 6 if job_type == "part" else 8

    while total_hours < max_hours and working_days < max_days:
        attendance = random.randint(0, 1)
        
        if attendance == 1:
            wage += hourly_rate * hours_per_day
            total_hours += hours_per_day
            working_days += 1

    print(f"Total working days: {working_days}")
    print(f"Total hours worked: {total_hours}")
    
    return wage

print(f"Total wage earned: {calculate_wage()}")
