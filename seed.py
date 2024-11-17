from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from faker import Faker
from models import Base, Student, Teacher, Group, Subject, Grade
import random

DATABASE_URL = "postgresql+psycopg2://postgres:some-password@localhost:5432/your_database_name"

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

faker = Faker()

# Створення груп
groups = [Group(name=f"Group {i}") for i in range(1, 4)]
session.add_all(groups)
session.commit()

# Створення викладачів
teachers = [Teacher(name=faker.name()) for _ in range(5)]
session.add_all(teachers)
session.commit()

# Створення предметів
subjects = [
    Subject(name=f"Subject {i}", teacher=random.choice(teachers)) for i in range(1, 8)
]
session.add_all(subjects)
session.commit()

# Створення студентів
students = [Student(name=faker.name(), group=random.choice(groups)) for _ in range(50)]
session.add_all(students)
session.commit()

# Створення оцінок
grades = [
    Grade(
        student=random.choice(students),
        subject=random.choice(subjects),
        grade=random.randint(60, 100),
        date=faker.date_between(start_date="-1y", end_date="today")
    )
    for _ in range(1000)
]
session.add_all(grades)
session.commit()

print("Database seeded successfully!")
