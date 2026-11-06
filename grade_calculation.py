
#Practice Problem 2: Student Grade Calculator

def main():
    # 1. Take the student's name as input
    name = input("Enter student's name: ")

    # 2. Take marks for three subjects
    try:
        sub1 = float(input("Enter Math marks: "))
        sub2 = float(input("Enter English marks: "))
        sub3 = float(input("Enter Python marks: "))
    except ValueError:
        print("Invalid input! Please enter numerical values for marks.")
        return

    # 6. Check if any subject mark is below 0 or above 100
    if not (0 <= sub1 <= 100) or not (0 <= sub2 <= 100) or not (0 <= sub3 <= 100):
        print("Error: Invalid marks entered! Marks must be between 0 and 100.")
        return

    # 3. Calculate the average marks
    average_marks = (sub1 + sub2 + sub3) / 3

    # 4. Determine the grade using the given conditions
    if 80 <= average_marks <= 100:
        grade = "A+"
    elif 70 <= average_marks < 80:
        grade = "A"
    elif 60 <= average_marks < 70:
        grade = "A-"
    elif 50 <= average_marks < 60:
        grade = "B"
    elif 40 <= average_marks < 50:
        grade = "C"
    else:
        grade = "F"

    # 5. Display the student's name, average marks, and final grade
    print("\n--- Student Report Card ---")
    print(f"Student Name:  {name}")
    print(f"Average Marks: {average_marks:.2f}")
    print(f"Final Grade:   {grade}")

if __name__ == "__main__":
    main()
