class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        
    def add_finished_courses(self, course_name):
        self.finished_courses.append(course_name)
    
    def rate_lc(self, lecturer, course, grade):
    # Возможность оценивать лекторов
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if 0 < grade <= 10:
                if course in lecturer.lecturer_grades:
                    lecturer.lecturer_grades[course] += [grade]
                else:
                    lecturer.lecturer_grades[course] = [grade]
                    return 'Оценка добавлена'
            else:
                return 'Ошибка, оценка выставляется от 1 до 10'
        else:
            return 'Ошибка лектор не проводит данный курс'
        
    def average_hw(self):
        all_grades_hw = []
        for grade in self.grades.values():
            all_grades_hw.extend(grade)
        if all_grades_hw:
            average = sum(all_grades_hw) / len(all_grades_hw)
            return average
        else:
            average = 0.0
            return average
        
    def __lt__(self, student):
        return self.average_hw() < student.average_hw()
    
    def __gt__(self, student):
        return self.average_hw() > student.average_hw()
    
    def __le__(self, student):
        return self.average_hw() <= student.average_hw()
    
    def __ge__(self, student):
        return self.average_hw() >= student.average_hw()
    
    def __eq__(self, student):
        return self.average_hw() == student.average_hw()
    
    def __ne__(self, student):
        return self.average_hw() != student.average_hw()
        
    def __str__(self):
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за домашнее задание: {self.average_hw():.2f}\n"
                f"Курсы в процессе изучения: {self.courses_in_progress}\n"
                f"Завершенные курсы: {self.finished_courses}"
        )
        
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name,surname)
        self.lecturer_grades = {}
    
    def average_grade(self):
        all_grades = []
        for course_grades in self.lecturer_grades.values():
            all_grades.extend(course_grades)
        if all_grades:
            average = sum(all_grades) / len(all_grades)
            return average
        else:
            average = 0.0
            return average
        
    def __lt__(self, lecturer):
        return self.average_grade() < lecturer.average_grade()
    
    def __gt__(self, lecturer):
        return self.average_grade() > lecturer.average_grade()
    
    def __le__(self, lecturer):
        return self.average_grade() <= lecturer.average_grade()
    
    def __ge__(self, lecturer):
        return self.average_grade() >= lecturer.average_grade()
    
    def __eq__(self, lecturer):
        return self.average_grade() == lecturer.average_grade()
    
    def __ne__(self, lecturer):
        return self.average_grade() != lecturer.average_grade()
        
    def __str__(self):
        return f"Имя: {self.name}\nФамилия {self.surname}\nСредняя оценка за лекции: {self.average_grade():.2f}"
     
class Reviewer(Mentor):
    
    def rate_hw(self, student, course, grade):
    #Возможность выставлять оценки)
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
            return "Оценка добавлена"
        else:
            return 'Ошибка студент не изучает этот курс'
    
    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"
    

def average_hw_course(students, course):
# Подсчет средней оценки по всем студентам в рамках конкретного курса
    all_grades = []
    for student in students:
        if isinstance(student, Student) and course in student.grades:
            all_grades.extend(student.grades[course])
        
    if all_grades:
        return sum(all_grades) / len(all_grades)
    else:
        return 0.0
    
def average_grade_lc_course(lecturers, course):
    all_grades = []
    for lecturer in lecturers:
        if isinstance(lecturer, Lecturer) and course in lecturer.lecturer_grades:
            all_grades.extend(lecturer.lecturer_grades[course])
    
    if all_grades:
        return sum(all_grades) / len(all_grades)
    else:
        return 0.0
        
        
# Создаем студентов
best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.finished_courses += ['Git']
best_student.courses_in_progress += ['Python']
best_student.grades['Git'] = [10, 10, 10, 10, 10]
best_student.grades['Python'] = [10, 10]

best_student2 = Student('Ruoy', 'Eman', 'your_gender')
best_student2.finished_courses += ['Git']
best_student2.courses_in_progress += ['Python']
best_student2.grades['Git'] = [10, 10, 10, 10, 10, 3, 5, 7]
best_student2.grades['Python'] = [10, 10, 5, 2, 4, 6]

print(best_student.finished_courses)
print(best_student.courses_in_progress)
print(best_student.grades)

best_student.add_finished_courses('Java')
print(best_student.finished_courses)

# Cоздаем лекторов
lecturer1 = Lecturer('Maks', 'leshiy',)
lecturer1.courses_attached += ['Python']
print(lecturer1.courses_attached)

lecturer2 = Lecturer('Maks', 'leshiy',)
lecturer2.courses_attached += ['Python']

# Студент оценивает лектора
best_student.rate_lc(lecturer1,"Python", 10)
best_student.rate_lc(lecturer1,"Python", 5)
best_student.rate_lc(lecturer1,"Python", 3)

best_student.rate_lc(lecturer2,"Python", 10)
best_student.rate_lc(lecturer2,"Python", 5)
best_student.rate_lc(lecturer2,"Python", 3)

print(f'Оценка лектора {lecturer1.lecturer_grades}')

# Создаем Reviewer
reviewer1 = Reviewer('Batya', 'Moget')
reviewer1.courses_attached += ['Python']
# Оценивание студента
reviewer1.rate_hw(best_student, "Python", 10)
reviewer1.rate_hw(best_student, "Python", 5)
reviewer1.rate_hw(best_student, "Python", 6 )
reviewer1.rate_hw(best_student, "Git", 5 )
reviewer1.rate_hw(best_student, "Git", 6 )


print(f'Оценка студента {best_student.grades}')
# Методы Str
print(reviewer1)
print(best_student)
# Методы сравнения по средним оценкам
print(best_student < best_student2)
print(best_student > best_student2)
print(best_student >= best_student2)
print(best_student <= best_student2)
print(best_student == best_student2)
print(best_student != best_student2)


print(lecturer1 < lecturer2)
print(lecturer1 > lecturer2)
print(lecturer1 >= lecturer2)
print(lecturer1 <= lecturer2)
print(lecturer1 == lecturer2)
print(lecturer1 != lecturer2)

student_list = [best_student,best_student2]
lecturer_list = [lecturer1, lecturer2]
print (f'Среденяя оценка всех студентов {average_hw_course(student_list, "Python"):.2f}')
print(f'Средняя оценка всех лекторов {average_grade_lc_course(lecturer_list, "Python"):.2f}')