import random

class Employee:
    PART_TIME_HOURS = 6
    FULL_TIME_HOURS = 8

    def __init__(self, wage_per_hour, max_hours, max_days):
        self.wage_per_hour = wage_per_hour
        self.max_hours = max_hours
        self.max_days = max_days
        self.wage = 0
        self.total_hours = 0
        self.working_days = 0

    @classmethod
    def compute_monthly_wage(cls, company_name, wage_per_hour, max_days, max_hours):
        employee = cls(wage_per_hour, max_hours, max_days)

        job_type = input(f'Enter a type of job for {company_name} (part/full): ').strip().lower()
        if job_type not in ["part", "full"]:
            print("Invalid job type. Please enter 'part' or 'full'.")
            return 0

        hours_per_day = cls.PART_TIME_HOURS if job_type == "part" else cls.FULL_TIME_HOURS

        for _ in range(max_days):
            if employee.total_hours >= max_hours:
                break

            if random.randint(0, 1) == 0:
                continue

            employee.add_hours(hours_per_day)

        print(f"Total monthly wage for {company_name}: {employee.wage}")
        return employee.wage

    def add_hours(self, hours):
        if self.total_hours + hours <= self.max_hours:
            self.wage += hours * self.wage_per_hour
            self.total_hours += hours
            self.working_days += 1
        else:
            remaining_hours = self.max_hours - self.total_hours
            self.wage += remaining_hours * self.wage_per_hour
            self.total_hours = self.max_hours

Employee.compute_monthly_wage("CompanyA", 20, 20, 160)
Employee.compute_monthly_wage("CompanyB", 15, 25, 200)
Employee.compute_monthly_wage("CompanyC", 22, 18, 150)
