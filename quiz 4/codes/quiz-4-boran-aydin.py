def create_student (name, age):
    name = str(name)    
    age = int(age)
    student_tuple = (name, age)
    
    return (student_tuple)

def describe_student (student_tuple):
    student_description = "Student",(student_tuple[0]), "is" ,(student_tuple[1]), "years old."
    
    return student_description

input_name = input("Enter student's name: ")
input_age = (input("Enter student's age: "))
input_age = int(input_age)
student = (create_student(input_name, input_age))
print(describe_student(student)) 