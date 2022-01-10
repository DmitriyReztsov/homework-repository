# deals/tests/tests_models.py
import datetime

from django.test import TestCase
from homeworks.models import Homework, HomeworkDone, HomeworkResult
from humans.models import Student, Teacher
from hw12.my_errors import DeadlineError


class HumanModelTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.teacher = Teacher.objects.create(first_name="Test", last_name="Teacher")

        cls.student = Student.objects.create(first_name="Test", last_name="Student")

    def test_creation(self):
        teacher = HumanModelTest.teacher
        student = HumanModelTest.student
        self.assertEqual(str(teacher), "Test Teacher")
        self.assertEqual(str(student), "Test Student")

    def test_migration(self):
        teacher_qs = Teacher.objects.all()
        student_qs = Student.objects.all()
        self.assertEqual(len(teacher_qs), 2)
        self.assertEqual(len(student_qs), 2)


class HomeworkModelTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.teacher = Teacher.objects.create(first_name="Test", last_name="Teacher")

        cls.student = Student.objects.create(first_name="Test", last_name="Student")

    def test_migration(self):
        homework_qs = Homework.objects.all()
        hw_result_qs = HomeworkResult.objects.all()
        hw_done_qs = HomeworkDone.objects.all()
        self.assertEqual(len(homework_qs), 1)
        self.assertEqual(len(hw_result_qs), 1)
        self.assertEqual(len(hw_done_qs), 1)

    def test_creation_hw(self):
        teacher = HomeworkModelTest.teacher
        student = HomeworkModelTest.student

        homework = teacher.create_homework(
            text="test django models", deadline=datetime.timedelta(days=2)
        )
        self.assertTrue(homework.is_active)
        self.assertEqual(homework.created_by, teacher)

        hw_result = student.do_homework(homework=homework, solution="BlaBlaBlaBlaBla")
        self.assertEqual(hw_result.student, student),
        self.assertEqual(hw_result.homework, homework)

        hw_done = teacher.check_homework(hw_result=hw_result)
        self.assertTrue(hw_done)
        self.assertTrue(HomeworkDone.objects.filter(homework_done=hw_result).exists())

    def test_expired_hw(self):
        teacher = HomeworkModelTest.teacher
        student = HomeworkModelTest.student
        homework = teacher.create_homework(
            text="test django models", deadline=datetime.timedelta(days=0)
        )

        self.assertFalse(homework.is_active)

        hw_result = student.do_homework(homework=homework, solution="BlaBlaBlaBlaBla")

        self.assertIsNone(hw_result)
        with self.assertRaises(DeadlineError):
            HomeworkResult.objects.create(
                student=student, homework=homework, solution="BlaBla"
            )
