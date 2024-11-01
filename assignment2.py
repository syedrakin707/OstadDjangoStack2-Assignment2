import json

class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def display_person_info(self):
        print("Name: " + self.name)
        print("Age: " + self.age)
        print("Address: " + self.address)

class Student(Person):
    def __init__(self, name, student_id, age, address):
        super().__init__(name, age, address)
        self.student_id = student_id
        self.grades = {}
        self.courses = []

    def add_grade(self, subject, grade):
        self.grades[subject] = grade

    def enroll_course(self, course):
        self.courses.append(course)

    def display_student_info(self):
        print("Student Information:")
        print("Name: " + self.name)
        print("ID: " + self.student_id)
        print("Age: " + self.age)
        print("Address: " + self.address)
        print("Enrolled Courses: ", end="")
        for i in self.courses:
            if i == self.courses[-1]:
                print(i.course_name, end=" ")
            else:
                print(i.course_name, end=", ")
        print()
        print("Grades: {}".format(self.grades))

class Course:
    def __init__(self, course_name, course_code, instructor):
        self.course_name = course_name
        self.course_code = course_code
        self.instructor = instructor
        self.students = []

    def add_students(self, student):
        self.students.append(student)

    def display_course_info(self):
        print("Student Information:")
        print("Course Name: " + self.course_name)
        print("Code: " + self.course_code)
        print("Instructor: " + self.instructor)
        print("Enrolled Students: ", end="")
        for i in self.students:
            if i == self.students[-1]:
                print(i.name, end=" ")
            else:
                print(i.name, end=", ")
        print()


def save_file():
    studentJSONs = []
    for i in students:
        studentJSON = {
            "Name": i.name,
            "ID": i.student_id,
            "Age": i.age,
            "Address": i.address,
            "Grades": i.grades,
            "Courses": [x.course_code for x in i.courses]
        }
        studentJSONs.append(studentJSON)
    with open("studentsData.json", "w") as studentsJSONFile:
        json.dump(studentJSONs, studentsJSONFile, indent=4)

    coursesJSONs = []
    for j in courses:
        courseJSON = {
            "CourseName": j.course_name,
            "CourseCode": j.course_code,
            "Instructor": j.instructor,
            "Students": [y.student_id for y in j.students]
        }
        coursesJSONs.append(courseJSON)
    with open("coursesData.json", "w") as coursesJSONFile:
        json.dump(coursesJSONs, coursesJSONFile, indent=4)
    print("All students and courses saved successfully")


def load_data():
    students = []
    courses = []
    with open("studentsData.json", "r") as studentsJSONFile:
        studentsJSON = json.load(studentsJSONFile)
        for x in studentsJSON:
            testStudent = Student(x['Name'], x['ID'], x['Age'], x['Address'])
            students.append(testStudent)

    with open("coursesData.json", "r") as coursesJSONFile:
        coursesJSON = json.load(coursesJSONFile)
        for y in coursesJSON:
            testCourse = Course(y['CourseName'], y['CourseCode'], y['Instructor'])
            courses.append(testCourse)

    for k in range(0, len(students)):
        for subject in studentsJSON[k]['Courses']:
            testCourse = None
            for test in courses:
                if test.course_code == subject:
                    testCourse = test
            students[k].enroll_course(testCourse)
        for subject, grade in studentsJSON[k]['Grades'].items():
            students[k].add_grade(subject, grade)

    for l in range(0, len(courses)):
        for enrolledStudent in coursesJSON[l]['Students']:
            testStudent = None
            for test in students:
                if test.student_id == enrolledStudent:
                    testStudent = test
            courses[l].add_students(testStudent)
    print("Data Loaded Successfully")


if __name__ == '__main__':
    print("==== Student Management System ====")
    print("1. Add New Student")
    print("2. Add New Course")
    print("3. Enroll Student in Course")
    print("4. Add Grade for Student")
    print("5. Display Student Details")
    print("6. Display Course Details")
    print("7. Save Data to File")
    print("8. Load Data from File")
    print("0. Exit")
    print()
    students = []
    courses = []
    while True:
        option = int(input("Select Option: "))
        if option == 1:
            studentName = input("Enter Name: ")
            studentAge = input("Enter Age: ")
            studentAddress = input("Enter Address: ")
            studentId = input("Enter Student ID: ")
            student = Student(studentName, studentId, studentAge, studentAddress)
            students.append(student)
            print("Student {} (ID:{}) added successfully".format(studentName, studentId))
        elif option == 2:
            courseName = input("Enter Course Name: ")
            courseCode = input("Enter Course Code: ")
            courseInstructor = input("Enter Instructor Name: ")
            course = Course(courseName, courseCode, courseInstructor)
            courses.append(course)
            print("Course {} (Code:{}) created with instructor {}".format(courseName, courseCode, courseInstructor))
        elif option == 3:
            studentId = input("Enter Student ID: ")
            courseCode = input("Enter Course Code: ")
            targetCourse = None
            targetStudent = None
            for i in students:
                if i.student_id == studentId:
                    targetStudent = i
            for j in courses:
                if j.course_code == courseCode:
                    targetCourse = j
            if targetCourse is None:
                print("Course Does Not Exist")
            elif targetStudent is None:
                print("Student Does Not Exist")
            else:
                targetCourse.add_students(targetStudent)
                targetStudent.enroll_course(targetCourse)
                print("Student {} (ID: {}) enrolled in {} (Code: {})".format(targetStudent.name,
                                                                         targetStudent.student_id,
                                                                         targetCourse.course_name,
                                                                         targetCourse.course_code))
        elif option == 4:
            studentId = input("Enter Student ID: ")
            courseCode = input("Enter Course Code: ")
            targetCourse = None
            targetStudent = None
            for i in students:
                if i.student_id == studentId:
                    targetStudent = i
            for j in courses:
                if j.course_code == courseCode:
                    targetCourse = j
            if targetCourse is None:
                print("Course Does Not Exist")
            elif targetStudent is None:
                print("Student Does Not Exist")
            else:
                studentGrade = input("Enter Grade: ")
                targetStudent.add_grade(targetCourse.course_name, studentGrade)
                print("Grade {} is added for {} in {}".format(studentGrade,
                                                          targetStudent.name,
                                                          targetCourse.course_name))
        elif option == 5:
            studentId = input("Enter Student ID: ")
            targetStudent = None
            for i in students:
                if i.student_id == studentId:
                    targetStudent = i
            if targetStudent is None:
                print("Student Does Not Exist")
            else:
                targetStudent.display_student_info()
        elif option == 6:
            courseCode = input("Enter Course Code: ")
            targetCourse = None
            for j in courses:
                if j.course_code == courseCode:
                    targetCourse = j
            if targetCourse is None:
                print("Course Does Not Exist")
            else:
                targetCourse.display_course_info()
        elif option == 7:
            save_file()
        elif option == 8:
            load_data()
        elif option == 0:
            print("Exiting Student Management System. Goodbye!")
            break