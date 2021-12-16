import datetime as dt

import pytest

from homework06.oop_2 import DeadlineError, Homework, HomeworkResult, Student, Teacher


def setup_instances():
    teacher_1 = Teacher("First_name_teacher", "Last_name_teacher")
    teacher_2 = Teacher("Aleksandr", "Smetanin")
    student_1 = Student("First_name_student", "Last_name_student")
    student_2 = Student("First_name_student_2", "Last_name_stident_2")
    homework = Homework("Text_hw", 2)
    return (teacher_1, teacher_2, student_1, student_2, homework)


def test_creation_inctances():
    teacher_1, teacher_2, student_1, student_2, homework = setup_instances()
    result_1 = HomeworkResult(student_1, homework, "solution")
    result_2 = student_2.do_homework(homework, "solution 2")
    assert isinstance(teacher_1, Teacher)
    assert isinstance(student_1, Student)
    assert isinstance(homework, Homework)
    assert isinstance(result_1, HomeworkResult)
    assert isinstance(result_2, HomeworkResult)
    assert teacher_1.first_name == "First_name_teacher"
    assert student_2.first_name == "First_name_student_2"
    assert homework.deadline == dt.timedelta(days=2)
    assert result_1.solution == "solution"
    assert result_2.solution == "solution 2"


def test_new_methods_custom_error():
    teacher_1, teacher_2, student_1, student_2, homework = setup_instances()
    expired_homework = teacher_1.create_homework("Learn functions", 0)

    with pytest.raises(DeadlineError):
        student_2.do_homework(expired_homework, "smth done")


def test_new_methods_hw_dict():
    teacher_1, teacher_2, student_1, student_2, homework = setup_instances()
    result_1 = HomeworkResult(student_1, homework, "solution")
    result_2 = student_2.do_homework(homework, "solution 2")
    result_3 = student_1.do_homework(homework, "few")
    teacher_1.check_homework(result_1)
    temp_1 = teacher_1.homework_done

    teacher_2.check_homework(result_1)
    temp_2 = Teacher.homework_done
    assert temp_1 == temp_2

    response_1 = teacher_1.check_homework(result_2)
    response_2 = teacher_1.check_homework(result_3)
    assert response_1 is True
    assert response_2 is False
    assert len(Teacher.homework_done[homework]) == 2
