import random

def check_attendance(attendance):
    
    if attendance == 0:
        return 0

    if attendance == 1:
        time = input("Enter type of job (part/full): ").lower()

        if time == "part":
            return 20*6
        
        elif time == "full":
            return 20*8

attendance_check=random.randint(0,1)
print(f"The wage is: {check_attendance(attendance_check)}")