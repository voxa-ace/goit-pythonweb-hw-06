from sqlalchemy import func
from models import Student, Grade, Subject

# 1. Average grade given by a specific teacher to a specific student:
def select_1_advanced(session, student_id, teacher_id):
    """
    Returns the average grade given by a specific teacher to a specific student.
    
    :param session: The SQLAlchemy session object.
    :param student_id: The ID of the student.
    :param teacher_id: The ID of the teacher.
    :return: The average grade given by the teacher to the student.
    """
    result = session.query(
        func.avg(Grade.grade).label('avg_grade')
    ).join(Subject).filter(
        Grade.student_id == student_id,
        Subject.teacher_id == teacher_id
    ).scalar()
    return result

# 2. Grades of students in a specific group for a specific subject on the last session:
def select_2_advanced(session, group_id, subject_id):
    """
    Returns the grades of students in a specific group for a specific subject on the last session.
    
    :param session: The SQLAlchemy session object.
    :param group_id: The ID of the group.
    :param subject_id: The ID of the subject.
    :return: A list of tuples containing student names, grades, and date of the grade for the last session.
    """
    latest_date_subquery = session.query(
        func.max(Grade.date).label('latest_date')
    ).join(Student).filter(
        Student.group_id == group_id,
        Grade.subject_id == subject_id
    ).scalar_subquery()

    result = session.query(
        Student.name,
        Grade.grade,
        Grade.date
    ).join(Grade).filter(
        Student.group_id == group_id,
        Grade.subject_id == subject_id,
        Grade.date == latest_date_subquery
    ).all()

    return result

