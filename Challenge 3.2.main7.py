#student details 
class Student:

  def __init__(self, name, roll_number, cgpa):
    self.name = name
    self.roll_number = roll_number
    self.cgpa = cgpa

def sort_students(student_list):
  sorted_students = sorted(student_list,key=lambda student: student.cgpa,reverse=True)
  
  return sorted_students

students = [
  Student("senthil", "A123", 9.9),
  Student("guna", "A124",9.8),
  Student("anbu","A125", 9.7),
  Student("rajan","A126", 9.6),
  Student("mave", "A125", 8.5),
  Student("otis", "A126", 8.4),
]

sorted_students = sort_students(students)

for student in sorted_students:
  print("NAME: {}, ROLL NO: {}, CGPA: {}".format(student.name, student.roll_number, student.cgpa))
