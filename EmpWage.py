import random

def monthly_wage():
    wage = 0
    working_days = 30

    job_type = input("Enter the type of job (part/full): ").strip().lower()

    if job_type not in ["part", "full"]:
        print("Invalid job type. Please enter either 'part' or 'full'.")
        return 0

    hourly_rate = 20
    hours_per_day = 6 if job_type == "part" else 8

    for _ in range(working_days):
        attendance = random.randint(0, 1)
        if attendance == 1:
            wage += hourly_rate * hours_per_day

    return wage

print(f"Total monthly wage: {monthly_wage()}")