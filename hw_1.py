
class Person:
    def __init__(self, full_name, age, is_married):
        self.full_name = full_name
        self.age = age
        self.is_married = is_married

    def introduce_myself(self):
        marital_status = "ЖЕНАТ" if self.is_married else "НЕЖЕНАТ"
        print(f"ИМЯ: {self.full_name},  {self.age} , {marital_status}.")

class Student(Person):
    def __init__(self, full_name, age, is_married, marks):
        super().__init__(full_name, age, is_married)
        self.marks = marks

    def average_grade(self):
        if self.marks:
            return sum(self.marks.values()) / len(self.marks)
        return 0

class Teacher(Person):
    base_salary = 50000

    def __init__(self, full_name, age, is_married, experience):
        super().__init__(full_name, age, is_married)
        self.experience = experience

    def calculate_salary(self):
        bonus = 0.05 * max(0, self.experience - 3)
        return self.base_salary * (1 + bonus)

def create_students():
    return [
        Student("Joldoshev Aidar", 16, False, {"математика": 5, "физика": 4, "литература": 5}),
        Student("Leo Lomonosov", 17, False, {"математика": 3, "физика": 5 }),
        Student("Petr Alexandrov", 15, False, {"математика": 4, "физика": 4, "история": 3 , "русский язык": 5}),
    ]

teacher = Teacher("Dmitry Alexsandrov", 35, True, 6)
teacher.introduce_myself()
print(f"Зарплата: {teacher.calculate_salary():.2f}")

students = create_students()
for student in students:
    student.introduce_myself()
    print("Оценки:")
    for subject, grade in student.marks.items():
        print(f"  {subject}: {grade}")
    print(f"Средняя оценка: {student.average_grade():.2f}\n")