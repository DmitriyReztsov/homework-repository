import datetime

from django.db import models
from humans.models import Student, Teacher
from hw12.my_errors import DeadlineError


class Homework(models.Model):
    """
    Class presented instancrs of homeworks.

    """

    text = models.TextField()
    deadline = models.DurationField()
    created_by = models.ForeignKey(
        Teacher, on_delete=models.CASCADE, related_name="homework"
    )
    created = models.DateTimeField(auto_now=True)

    @property
    def is_active(self) -> bool:
        """
        Returns True if current date is still lower than creation date added to deadline.

        """
        return (self.created + self.deadline) > datetime.datetime.now()


class HomeworkResult(models.Model):
    """
    Accepts instance of Student as an author of solution, instance of Homework
    done by author and solution itself as a string.
    Valuates homework - it should be Homework instance only. Overwise ValueError
    raises.

    :raise ValueError: If homework is not Homework instance.

    """

    student = models.ForeignKey(
        Student, on_delete=models.CASCADE, related_name="hw_result"
    )
    homework = models.ForeignKey(
        Homework, on_delete=models.CASCADE, related_name="hw_result"
    )
    solution = models.TextField()
    created = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if self.homework.is_active:
            return super().save(*args, **kwargs)
        raise DeadlineError("You are late")


class HomeworkDone(models.Model):
    """
    Модель для хранения HomeworkResult после успешного прохождения check_homework
    (гарантировано остутствие повторяющихся результатов по каждому
    заданию).
    Общий для всех учителей.

    """

    homework_done = models.ForeignKey(
        HomeworkResult, on_delete=models.CASCADE, unique=True
    )
