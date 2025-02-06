import random

def check_attendance(attendance):
    
    match attendance:
        case 0:
            return 0
        
        case 1:
            time = input("Enter a type of job (part/full) :").lower()

            match time:                
                case "part":
                    return 20 * 6
                
                case "full":
                    return 20 * 8
                
                case _:
                    return "Invalid job type"

attendance_check=random.randint(0,1)
print(f"The wage is: {check_attendance(attendance_check)}")