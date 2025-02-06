import random

class Employee:
    PART_TIME_HOURS = 6
    FULL_TIME_HOURS = 8
    WAGE_PER_HOUR = 20
    MAX_HOURS = 100
    MAX_DAYS = 20

    def __init__(self):
        self.wage = 0
        self.total_hours = 0
        self.working_days = 0

    @classmethod
    def compute_monthly_wage(cls):
        employee = cls()
        job_type = input('Enter a type of job (part/full): ').strip().lower()

        if job_type not in ["part", "full"]:
            print("Invalid job type. Please enter 'part' or 'full'.")
            return 0

        hours_per_day = cls.PART_TIME_HOURS if job_type == "part" else cls.FULL_TIME_HOURS

        for _ in range(cls.MAX_DAYS):
            if employee.total_hours >= cls.MAX_HOURS:
                break

            if random.randint(0, 1) == 0:
                continue

            employee.add_hours(hours_per_day)

        return employee.wage

    def add_hours(self, hours):
        if self.total_hours + hours <= Employee.MAX_HOURS:
            self.wage += hours * Employee.WAGE_PER_HOUR
            self.total_hours += hours
            self.working_days += 1
        else:
            remaining_hours = Employee.MAX_HOURS - self.total_hours
            self.wage += remaining_hours * Employee.WAGE_PER_HOUR
            self.total_hours = Employee.MAX_HOURS

print(f"Total monthly wage: {Employee.compute_monthly_wage()}")
