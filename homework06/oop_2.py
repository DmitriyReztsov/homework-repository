"""
В этом задании будем улучшать нашу систему классов из задания прошлой лекции
(Student, Teacher, Homework)
Советую обратить внимание на defaultdict из модуля collection для
использования как общую переменную


1. Как то не правильно, что после do_homework мы возвращаем все тот же
объект - будем возвращать какой-то результат работы (HomeworkResult)

HomeworkResult принимает объект автора задания, принимает исходное задание
и его решение в виде строки
Атрибуты:
    homework - для объекта Homework, если передан не этот класс -  выкинуть
    подходящие по смыслу исключение с сообщением:
    'You gave a not Homework object'

    solution - хранит решение ДЗ как строку
    author - хранит объект Student
    created - c точной датой и временем создания

2. Если задание уже просрочено хотелось бы видеть исключение при do_homework,
а не просто принт 'You are late'.
Поднимайте исключение DeadlineError с сообщением 'You are late' вместо print.

3. Student и Teacher имеют одинаковые по смыслу атрибуты
(last_name, first_name) - избавиться от дублирования с помощью наследования

4.
Teacher
Атрибут:
    homework_done - структура с интерфейсом как в словаря, сюда поподают все
    HomeworkResult после успешного прохождения check_homework
    (нужно гаранитровать остутствие повторяющихся результатов по каждому
    заданию), группировать по экземплярам Homework.
    Общий для всех учителей. Вариант ипользования смотри в блоке if __main__...
Методы:
    check_homework - принимает экземпляр HomeworkResult и возвращает True если
    ответ студента больше 5 символов, так же при успешной проверке добавить в
    homework_done.
    Если меньше 5 символов - никуда не добавлять и вернуть False.

    reset_results - если передать экземпряр Homework - удаляет только
    результаты этого задания из homework_done, если ничего не передавать,
    то полностью обнулит homework_done.

PEP8 соблюдать строго.
Всем перечисленным выше атрибутам и методам классов сохранить названия.
К названием остальных переменных, классов и тд. подходить ответственно -
давать логичные подходящие имена.
"""
import datetime
from collections import defaultdict


class DeadlineError(Exception):
    pass


class Human:
    """
    Base class for instances, presented a man.

    :param first_name: first name of a man.
    :type first_name: str.
    :param last_name: lat name of a man.
    :type last_name: str.

    """

    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name


class Student(Human):
    def do_homework(self, homework: "Homework", result: str) -> "HomeworkResult":
        """
        Method checks if a student is in time to present the result.
        If the date of deadline is over DeadlineError with message 'You are late'
        raises.

        :raise oop_2.DeadlineError: If current date is bigger than date of daedline.

        """
        if homework.is_active:
            return HomeworkResult(self, homework, result)
        raise DeadlineError("You are late")


class Teacher(Human):
    homework_done = defaultdict(list)
    # структура с интерфейсом как в словаря, сюда поподают все
    # HomeworkResult после успешного прохождения check_homework
    # (нужно гаранитровать остутствие повторяющихся результатов по каждому
    # заданию), группировать по экземплярам Homework.
    # Общий для всех учителей.

    @classmethod
    def check_homework(cls, hw_result: "HomeworkResult") -> bool:
        """
        Accepts inctanse of HomeworkResult and returns True if answer
        contains more than 5 characters, adds the instance into homework_done as well.
        Overwise - just returns False.

        """
        if len(hw_result.solution) > 5:
            if hw_result not in cls.homework_done[hw_result.homework]:
                cls.homework_done[hw_result.homework].append(hw_result)
            return True
        return False

    @classmethod
    def reset_results(cls, homework: "Homework" = None):
        """
        Removes instance of Homework from the homework_done dict if the inctanse
        passed. Clears the dict overwise.

        :param homework: homework should be removed.
        :type homework: oop_2.Homework or None.

        """
        if not homework:
            cls.homework_done.clear()
        else:
            cls.homework_done.pop(homework)

    @staticmethod
    def create_homework(text: str, deadline: datetime):
        """
        Creates instance of Homework class.

        """
        return Homework(text, deadline)


class Homework:
    """
    Class presented instancrs of homeworks.
    :param deadline: numbers of days fron creation date.
    :type kind: int.

    """

    def __init__(self, text: str, deadline: int):
        self.text = text
        self.deadline = datetime.timedelta(deadline)
        self.created = datetime.datetime.now()

    @property
    def is_active(self) -> bool:
        """
        Returns True if current date is still lower than creation date added to deadline.

        """
        return (self.created + self.deadline) > datetime.datetime.now()


class HomeworkResult:
    """
    Accepts instance of Student as an author of solution, instance of Homework
    done by author and solution itself as a string.
    Valuates homework - it should be Homework instance only. Overwise ValueError
    raises.

    :raise ValueError: If homework is not Homework instance.

    """

    def __init__(self, student: Student, homework: Homework, solution: str):
        if not isinstance(homework, Homework):
            raise ValueError("You gave a not Homework object")
        self.student = student
        self.homework = homework
        self.solution = solution
        self.created = datetime.datetime.now()


if __name__ == "__main__":
    opp_teacher = Teacher("Daniil", "Shadrin")
    advanced_python_teacher = Teacher("Aleksandr", "Smetanin")

    lazy_student = Student("Roman", "Petrov")
    good_student = Student("Lev", "Sokolov")

    oop_hw = opp_teacher.create_homework("Learn OOP", 1)
    docs_hw = opp_teacher.create_homework("Read docs", 5)

    result_1 = good_student.do_homework(oop_hw, "I have done this hw")
    result_2 = good_student.do_homework(docs_hw, "I have done this hw too")
    result_3 = lazy_student.do_homework(docs_hw, "done")
    try:
        result_4 = HomeworkResult(good_student, "fff", "Solution")
    except Exception:
        print("There was an exception here")
    opp_teacher.check_homework(result_1)
    temp_1 = opp_teacher.homework_done

    advanced_python_teacher.check_homework(result_1)
    temp_2 = Teacher.homework_done
    assert temp_1 == temp_2

    opp_teacher.check_homework(result_2)
    opp_teacher.check_homework(result_3)

    print(Teacher.homework_done[oop_hw])
    Teacher.reset_results()
    pass
