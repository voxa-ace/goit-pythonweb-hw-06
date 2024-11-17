from sqlalchemy import func
from models import Student, Grade, Subject, Group


# 1. Find the top 5 students with the highest average grades across all subjects:
def select_1(session):
    """
    Find the top 5 students with the highest average grades across all subjects.
    """
    result = session.query(
        Student.name,
        func.avg(Grade.grade).label('avg_grade')
    ).join(Grade).group_by(Student.id).order_by(func.avg(Grade.grade).desc()).limit(5).all()
    return result

# 2. Find the student with the highest average grade in a specific subject:
def select_2(session, subject_id):
    """
    Find the student with the highest average grade in a specific subject.
    
    Args:
    subject_id (int): The ID of the subject.
    """
    result = session.query(
        Student.name,
        func.avg(Grade.grade).label('avg_grade')
    ).join(Grade).filter(Grade.subject_id == subject_id).group_by(Student.id).order_by(func.avg(Grade.grade).desc()).first()
    return result

# 3. Find the average grade for groups in a specific subject:
def select_3(session, subject_id):
    """
    Find the average grade for groups in a specific subject.
    
    Args:
    subject_id (int): The ID of the subject.
    """
    result = session.query(
        Group.name,
        func.avg(Grade.grade).label('avg_grade')
    ).join(Student).join(Grade).filter(Grade.subject_id == subject_id).group_by(Group.id).all()
    return result

# 4. Find the average grade across the entire course (all grade records):
def select_4(session):
    """
    Find the average grade across all grade records.
    """
    result = session.query(
        func.avg(Grade.grade).label('avg_grade')
    ).scalar()
    return result

# 5. Find which courses are taught by a specific teacher:
def select_5(session, teacher_id):
    """
    Find which courses are taught by a specific teacher.
    
    Args:
    teacher_id (int): The ID of the teacher.
    """
    result = session.query(Subject.name).filter(Subject.teacher_id == teacher_id).all()
    return result

# 6. Find the list of students in a specific group:
def select_6(session, group_id):
    """
    Find the list of students in a specific group.
    
    Args:
    group_id (int): The ID of the group.
    """
    result = session.query(Student.name).filter(Student.group_id == group_id).all()
    return result

# 7. Find the grades of students in a specific group for a specific subject:
def select_7(session, group_id, subject_id):
    """
    Find the grades of students in a specific group for a specific subject.
    
    Args:
    group_id (int): The ID of the group.
    subject_id (int): The ID of the subject.
    """
    result = session.query(
        Student.name,
        Grade.grade,
        Grade.date
    ).join(Grade).filter(
        Student.group_id == group_id,
        Grade.subject_id == subject_id
    ).all()
    return result

# 8. Find the average grade given by a specific teacher across their subjects:
def select_8(session, teacher_id):
    """
    Find the average grade given by a specific teacher across their subjects.
    
    Args:
    teacher_id (int): The ID of the teacher.
    """
    result = session.query(
        func.avg(Grade.grade).label('avg_grade')
    ).join(Subject).filter(Subject.teacher_id == teacher_id).join(Grade).scalar()
    return result

# 9. Find the list of courses attended by a specific student:
def select_9(session, student_id):
    """
    Find the list of courses attended by a specific student.
    
    Args:
    student_id (int): The ID of the student.
    """
    result = session.query(Subject.name).join(Grade).filter(Grade.student_id == student_id).all()
    return result

# 10. Find the list of courses a specific student is taking from a specific teacher:
def select_10(session, student_id, teacher_id):
    """
    Find the list of courses a specific student is taking from a specific teacher.
    
    Args:
    student_id (int): The ID of the student.
    teacher_id (int): The ID of the teacher.
    """
    result = session.query(Subject.name).join(Grade).filter(
        Grade.student_id == student_id,
        Subject.teacher_id == teacher_id
    ).all()
    return result
