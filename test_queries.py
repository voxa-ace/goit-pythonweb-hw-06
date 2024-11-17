from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import *
from samples_database import *  
from my_select_advanced import *  


# Step 1: Set up the SQLAlchemy session
DATABASE_URL = "sqlite:///your_database.db"  
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

# Step 2: Test the query functions
try:
    # Get the top 5 students with the highest average grades
    top_students = select_1(session)
    print("Top 5 students with the highest average grades:")
    for student in top_students:
        print(f"{student.name}: {student.avg_grade}")

    # Get the student with the highest average grade in a specific subject (e.g., subject_id=1)
    best_student_in_subject = select_2(session, subject_id=1)
    print("\nStudent with the highest average grade in subject 1:")
    print(f"{best_student_in_subject.name}: {best_student_in_subject.avg_grade}")

    # Get the average grade across the entire course (all students)
    overall_avg_grade = select_4(session)
    print("\nOverall average grade across the entire course:", overall_avg_grade)

    # Get courses taught by a specific teacher (e.g., teacher_id=1)
    courses_by_teacher = select_5(session, teacher_id=1)
    print("\nCourses taught by teacher 1:")
    for course in courses_by_teacher:
        print(course.name)


    # Get the average grade given by teacher 1 to student 1
    avg_grade = select_1_advanced(session, student_id=1, teacher_id=1)
    print("\nAverage grade given by teacher 1 to student 1:", avg_grade)

    # Get grades of students in group 1 for subject 1 on the last session
    grades_last_session = select_2_advanced(session, group_id=1, subject_id=1)
    print("\nGrades of students in group 1 for subject 1 on the last session:")
    for student in grades_last_session:
        print(f"{student.name}: {student.grade} (Date: {student.date})")


finally:
    # Step 3: Close the session after testing
    session.close()
