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
    def __init__(self, message):
        self.message = message


class Human:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name


class Student(Human):
    def do_homework(self, homework, result):
        if homework.is_active:
            return HomeworkResult(self, homework, result)
        raise DeadlineError("You are late")


class Teacher(Human):
    """структура с интерфейсом как в словаря, сюда поподают все
    HomeworkResult после успешного прохождения check_homework
    (нужно гаранитровать остутствие повторяющихся результатов по каждому
    заданию), группировать по экземплярам Homework.
    Общий для всех учителей.

    """

    homework_done = defaultdict(list)

    @classmethod
    def check_homework(cls, hw_result):
        """принимает экземпляр HomeworkResult и возвращает True если
        ответ студента больше 5 символов, так же при успешной проверке добавить
        в homework_done.
        Если меньше 5 символов - никуда не добавлять и вернуть False.

        """
        if len(hw_result.solution) > 5:
            if hw_result not in cls.homework_done[hw_result.homework]:
                cls.homework_done[hw_result.homework].append(hw_result)
            return True
        return False

    @classmethod
    def reset_results(cls, homework=None):
        """если передать экземпряр Homework - удаляет только
        результаты этого задания из homework_done, если ничего не передавать,
        то полностью обнулит homework_done.

        """

        if not homework:
            cls.homework_done.clear()
        else:
            cls.homework_done.pop(homework)

    @staticmethod
    def create_homework(text, deadline):
        return Homework(text, deadline)


class Homework:
    def __init__(self, text, deadline):
        self.text = text
        self.deadline = datetime.timedelta(deadline)
        self.created = datetime.datetime.now()

    @property
    def is_active(self):
        return (self.created + self.deadline) > datetime.datetime.now()


class HomeworkResult:
    """HomeworkResult принимает объект автора задания, принимает исходное задание
    и его решение в виде строки

    """

    def __init__(self, student: Student, homework: Homework, solution: str):
        self.student = student
        self.homework = homework
        self.solution = solution
        self.created = datetime.datetime.now()
        for key in self.__init__.__annotations__:
            if not isinstance(self.__dict__[key], self.__init__.__annotations__[key]):
                raise ValueError(
                    f"WHAT??? Your <{self.__dict__[key]}> should be type of <{self.__init__.__annotations__[key]}>"
                )


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
