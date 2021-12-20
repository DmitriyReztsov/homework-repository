import datetime as dt
import io
from contextlib import redirect_stdout

from homework05.oop_1 import Homework, Student, Teacher


def test_creation_inctances():
    teacher = Teacher("First_name_teacher", "Last_name_teacher")
    student = Student("First_name_student", "Last_name_student")
    homework = Homework("Text_hw", 2)
    assert isinstance(teacher, Teacher)
    assert isinstance(student, Student)
    assert isinstance(homework, Homework)
    assert teacher.first_name == "First_name_teacher"
    assert student.first_name == "First_name_student"
    assert homework.deadline == dt.timedelta(days=2)


def test_methods(setup_instances):
    student, teacher, homework = setup_instances
    time_now = dt.datetime.now()
    expired_homework = teacher.create_homework("Learn functions", 0)
    assert expired_homework.created.replace(microsecond=0) == time_now.replace(
        microsecond=0
    )
    assert expired_homework.deadline == dt.timedelta(0)
    assert expired_homework.text == "Learn functions"

    create_homework_too = teacher.create_homework
    oop_homework = create_homework_too("create 2 simple classes", 5)
    assert oop_homework.deadline == dt.timedelta(5)

    assert isinstance(student.do_homework(oop_homework), Homework)

    with redirect_stdout(io.StringIO()) as output:
        response = student.do_homework(expired_homework)
    assert response is None
    assert output.getvalue() == "You are late\n"

    assert homework.is_active is True
    homework.created = dt.datetime.now() - dt.timedelta(2)
    assert homework.is_active is False
