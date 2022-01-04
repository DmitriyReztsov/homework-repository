from datetime import datetime

from django.db import models

from hw12.my_errors import DeadlineError


class Human(models.Model):
    """
    Base class for instances, presented a man.

    """

    first_name = models.CharField(max_length=450)
    last_name = models.CharField(max_length=450)

    def __str__(self) -> str:
        return "%s %s" % (self.first_name, self.last_name)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["first_name", "last_name"], name="persons name"
            )
        ]


class Teacher(Human):
    @staticmethod
    def check_homework(hw_result) -> bool:
        from homeworks.models import HomeworkDone

        """
        Accepts inctanse of HomeworkResult and returns True if answer
        contains more than 5 characters, adds the instance into homework_done as well.
        Overwise - just returns False.

        """
        if len(hw_result.solution) > 5:
            HomeworkDone.objects.get_or_create(homework_done=hw_result)
            return True
        return False

    @staticmethod
    def reset_results(homework=None):
        from homeworks.models import HomeworkDone

        """
        Removes instance of Homework if the inctanse
        passed. Clears the dict overwise.

        :param homework: homework should be removed.
        :type homework: oop_2.Homework or None.

        """
        if not homework:
            HomeworkDone.objects.all().delete()
        else:
            HomeworkDone.objects.get(homework_done=homework).delete()

    def create_homework(self, text: str, deadline: datetime):
        from homeworks.models import Homework

        """
        Creates instance of Homework class.

        """
        return Homework.objects.create(created_by=self, text=text, deadline=deadline)


class Student(Human):
    def do_homework(self, homework, solution):
        from homeworks.models import HomeworkResult

        """
        Method checks if a student is in time to present the result.
        If the date of deadline is over DeadlineError with message 'You are late'
        raises.

        :raise oop_2.DeadlineError: If current date is bigger than date of daedline.

        """
        try:
            hw = HomeworkResult.objects.create(
                student=self, homework=homework, solution=solution
            )
        except DeadlineError:
            return None
        return hw
