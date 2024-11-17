from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from faker import Faker
from models import *
import random

DATABASE_URL = 'postgresql://postgres:qwerty@localhost:5432/postgres'

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

faker = Faker()

groups = [Group(name=f"Group {i}") for i in range(1, 4)]
session.add_all(groups)
session.commit()

teachers = [Teacher(name=faker.name()) for _ in range(5)]
session.add_all(teachers)
session.commit()

subjects = [
    Subject(name=f"Subject {i}", teacher=random.choice(teachers)) for i in range(1, 8)
]
session.add_all(subjects)
session.commit()

students = [Student(name=faker.name(), group=random.choice(groups)) for _ in range(50)]
session.add_all(students)
session.commit()

grades = [
    Grade(
        student=random.choice(students),
        subject=random.choice(subjects),
        grade=random.randint(60, 100),
        date_received=faker.date_between(start_date="-1y", end_date="today")  # змінено на date_received
    )
    for _ in range(1000)
]
session.add_all(grades)
session.commit()

Base.metadata.create_all(engine)

print("Database seeded successfully!")

