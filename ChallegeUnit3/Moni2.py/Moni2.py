class Student:

  def _init_(self,name, roll_number, cgpa):
    self.name = name
    self.roll_number = roll_number
    self.cgpa = cgpa


def sort_students(student_list):
  #Sort the list of students in dece dingorder of CGPA
  sorted_students = sorted(student_list, key=lambda student: student.cgpa, reverse=True)
  return sorted_students


#Example usage:
students = [
   Student("Monica", "M2530", 9.9),
   Student("Maji", "M2531", 8.9),
   Student("Arun", "M2532", 9.8),
   Student("Nithin", "M2533", 9.1),
   Student("Vennila", "M2534", 9.2),
]

sorted_students = sort_students(students)

#Print the sorted list of students
for student in sorted_students:
  print("Name: {}, Roll Number: {}, CGPA: {}".format(student.name, student.roll_number, student.cgpa))