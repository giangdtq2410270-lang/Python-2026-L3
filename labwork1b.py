students=[]
courses=[]
mark={}

def input_student():
    num_student=int(input("The number of student: "))
    for i in range (num_student):
        print("student",i+1)
        s_name=input("Student name: ")
        s_id=input("Student ID: ")
        dob=input("DoB: ")
        student= {'Name':s_name,'ID':s_id,'DOB':dob,'Mark':{}}
        students.append(student)
    return students
def input_course():
    num_course=int(input("The number of courses: "))
    for i in range (num_course):
        c_name=input("Course name: ")
        c_id=input("Course ID: ")
        course = {'name':c_name,'id':c_id}
        courses.append(course)
    return courses
def input_mark():
    c_id=input("enter course ID to input mark: ")
    c_found= False
    for course in courses:
        if course['id']==c_id:
            c_found = True
            break
    if not c_found:
        print("Course not found")
        return
    for student in students:
        mark=float(input("Mark for " + student['Name'] + ":"))
        student['Mark'][c_id]=mark
def list_course():
    print("============List of Courses============")
    for course in courses:
        print(course)

def list_student():
    print("==============List of Students===============")
    for student in students:
        print(student)
def show_marks():
    c_id = input("Enter course id to show marks:")
    c_name = ""
    for course in courses:
        if course['id'] == c_id:
            c_name = course['name']
            break
    if c_name=="":
        print("Course not found")
        return
    print("Course:", course['name'])
    for student in students:
        if c_id in student['Mark']:
            mark=student['Mark'][c_id]
            print("Student:", student['Name'], "| Mark:", mark)
input_student()
input_course()
while True:
    choice = int(input("1.List Students | 2. List Courses | 3.Input Mark | 4.Show Marks | 5.Exit "))
    if choice == 1:
        list_student()
    elif choice == 2:
        list_course()
    elif choice == 3:
        input_mark()
    elif choice == 4:
        show_marks()
    elif choice == 5:
        break

