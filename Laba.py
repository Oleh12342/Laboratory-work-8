# Створення словника успішності студентів
students_dict = {}

# Функція для додавання студента до словника
def add_student(group_number, full_name, course, subjects_grades):
    students_dict[full_name] = {
        "Номер групи": group_number,
        "Курс": course,
        "Предмети та оцінки": subjects_grades
    }

# Додавання студента до словника
add_student(
    group_number="CS-01",
    full_name="Кулеш Олег Ярославович",
    course=2,
    subjects_grades={
        "Математика": 95,
        "Фізика": 88,
        "Програмування": 92
    }
)

add_student(
    group_number="CS-01",
    full_name="Шебедко Іван Дмитрович",
    course=2,
    subjects_grades={
        "Математика": 75,
        "Фізика": 85,
        "Програмування": 89
    }
)

# Виведення інформації про студентів
def display_students():
    for full_name, details in students_dict.items():
        print(f"Студент: {full_name}")
        print(f"  Група: {details['Номер групи']}")
        print(f"  Курс: {details['Курс']}")
        print(f"  Предмети та оцінки:")
        for subject, grade in details["Предмети та оцінки"].items():
            print(f"    {subject}: {grade}")
        print()

# Виклик функції для відображення студентів
display_students()

# Завдання для другого студента:
# Реалізувати функцію для сортування студентів у словнику за середнім балом
