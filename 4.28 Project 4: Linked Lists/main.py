from slist import SList
from course import Course

def calculate_gpa(courseList):
    sumGrades = 0
    credits = 0
    for course in courseList:
        sumGrades += course.grade() * course.credit_hr()
        credits += course.credit_hr()

    if credits == 0:
        return 0
    return sumGrades / credits

def is_sorted(lyst):
    for i in range(0, len(lyst) - 1):
        if lyst[i].number() > lyst[i + 1].number():
            return False
    return True

def main():
    courseList = SList()
    courseList.insert(Course(1234, 'Test Name', 3.0, 3.5))

    gpa = calculate_gpa(courseList)
    print(f"GPA: {gpa}")

    sorted_status = is_sorted(courseList)
    print(f"Is sorted: {sorted_status}")

if __name__ == "__main__":
    main()
