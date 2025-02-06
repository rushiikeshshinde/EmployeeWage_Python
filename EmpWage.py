import random

def check_attendance(attendance):
    
    if attendance == 0:
        print('Employee is Absent')

    if attendance == 1:
        print('Employee is Present')

attendance_check=random.randint(0,1)
check_attendance(attendance_check)