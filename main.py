class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
    
    def add_courses(self, course_name):
        self.finished_courses.append(course_name)   
        
    def rate_lec(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
    def average_grade(self):
        total_grades = 0
        total_courses = 0
        for course, grades in self.grades.items():
            total_grades += sum(grades)
            total_courses += len(grades)
        av_grade_stud = total_grades / total_courses if total_courses > 0 else 0
        return av_grade_stud
    
    def __str__(self):
        return (f"Имя: {self.name} \n" 
                f"Фамилия: {self.surname} \n" 
                f"Средняя оценка за домашние задания: {self.average_grade():.2f} \n"
                f"Курсы в процессе изучения: {self.courses_in_progress} \n"
                f"Завершенные курсы: {self.finished_courses}"
)
    
    def __eq__(self, grade):
        return (self.average_grade() == grade.average_grade())
    
    def average_grade_for_course(students, course_name):
        total_grades = 0
        total_students = 0
        for student in students:
            if course_name in student.grades:
                total_grades += sum(student.grades[course_name])
                total_students += len(student.grades[course_name])
        total_average_grades = total_grades / total_students if total_students > 0 else 0
        return total_average_grades        
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
            
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
    def average_grade(self):
        total_grades = 0
        total_courses = 0
       
        for course, grades in self.grades.items():
            total_grades += sum(grades)
            total_courses += len(grades)
        av_grade_lec = total_grades / total_courses if total_courses > 0 else 0
        return av_grade_lec
        #return sum(self.grades.values()) / len(self.grades)

    def __eq__(self, grade):
        return (self.average_grade() == grade.average_grade())            

    def __str__(self):
        return (f"Имя: {self.name} \n" 
                f"Фамилия: {self.surname} \n" 
                f"Средняя оценка за лекции: {self.average_grade():.2f}"
)
    def average_grade_for_course(lecturers, course_name):
        total_grades = 0
        total_lecturers = 0
        for lecturer in lecturers:
            if course_name in lecturer.grades:
                total_grades += sum(lecturer.grades[course_name])
                total_lecturers += len(lecturer.grades[course_name])
        total_average_grades = total_grades / total_lecturers if total_lecturers > 0 else 0
        return total_average_grades    

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
    def __str__(self):
        return (f"Имя: {self.name} \n" 
                f"Фамилия: {self.surname}" 
)
        
student1 = Student('Галина', 'Самбука', 'female')
student1.courses_in_progress += ['Python']
student1.add_courses('Вышивание бисером')
student2 = Student('Михаил', 'Вассерман', 'male')
student2.courses_in_progress += ['Python']
student2.add_courses('Выживание в тайге')
reviewer1 =  Reviewer('Сергей', 'Проверяльщиков')
reviewer1.courses_attached += ['Python']
reviewer2 =  Reviewer('Василиса', 'Премудрая')
reviewer2.courses_attached += ['Python']
lector1 = Lecturer('Борис', 'Лектор')
lector1.courses_attached +=['Python']
lector2 = Lecturer('Ева', 'Плюмбум')
lector2.courses_attached +=['Python']


student1.rate_lec(lector1, 'Python', 10)
student1.rate_lec(lector1, 'Python', 5)
student1.rate_lec(lector1, 'Python', 10)

student2.rate_lec(lector2, 'Python', 10)
student2.rate_lec(lector2, 'Python', 5)
student2.rate_lec(lector2, 'Python', 10)
 
reviewer1.rate_hw(student1, 'Python', 10)
reviewer1.rate_hw(student1, 'Python', 10)
reviewer1.rate_hw(student1, 'Python', 10)
 
reviewer2.rate_hw(student2, 'Python', 9)
reviewer2.rate_hw(student2, 'Python', 9)
reviewer2.rate_hw(student2, 'Python', 9) 

print(student1)
print("------------------------")
print(student2)
print("------------------------")
print(lector1)
print("------------------------")
print(lector2)
print("------------------------")
print(reviewer1)
print("------------------------")
print(reviewer2)
print("------------------------")

if lector1 == lector2: 
    print("Лекторы,", lector1.name, "и", lector2.name, "- имеют одинаковые средние оценки")
else:
    print("Лекторы,", lector1.name, "и", lector2.name, "- имеют различные средние оценки")

if student1 == student2: 
    print("Студенты,", student1.name, "и", student2.name, "- имеют одинаковые средние оценки")
else:
    print("Студенты,", student1.name, "и", student2.name, "- имеют различные средние оценки")
print("------------------------")

students = [student1, student2]
lecturers = [lector1, lector2]
course_name = 'Python'

average_kurs_grade_s = Student.average_grade_for_course(students, course_name)
print(f"Средняя оценка за домашние задания по курсу: '{course_name}': {average_kurs_grade_s:.2f}")

average_kurs_grade_l = Lecturer.average_grade_for_course(lecturers, course_name)
print(f"Средняя оценка за лекции по курсу: '{course_name}' {average_kurs_grade_l:.2f}")
print("------------------------")
