import math


def main():
    # students = [
    #     {"id": "101", "name": "Alice", "marks": 85},
    #     {"id": "102", "name": "Bob", "marks": 90},
    #     {"id": "103", "name": "Charlie", "marks": 78},
    # ]
    students = []
    n = int(input("Enter Number of Students :"))

    for i in range(n):
        # student = {}
        # id = input("Input id : ")
        # name = input("Input Name :")
        # marks = int(input("Input Marks :"))
        # student["id"] = id
        # student["name"] = name
        # student["marks"] = marks
        
        student_data = input("Enter ID, Name, and Marks (space-separated): ").split()
        
        student = {
            "id": student_data[0],
            "name": student_data[1],
            "marks": int(student_data[2]),
        }
        students.append(student)

    highest_marks_student = max(students, key=lambda x: x["marks"])
    print(f" {highest_marks_student}")


if __name__ == "__main__":
    main()
