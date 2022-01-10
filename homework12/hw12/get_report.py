# Instatiate Django and import settings
import os

# mark django settings module as settings.py
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hw12.settings")

# instantiate a web sv for django which is a wsgi
from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()

import csv

from homeworks.models import HomeworkDone


def import_to_csv():
    path = os.path.abspath("homework12/hw12/report.csv")
    qs = HomeworkDone.objects.all()
    with open(path, "w", newline="") as csvfile:
        fieldnames = ["Homework", "Student name", "Creation date", "Teacher name"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for entry in qs:
            homework = entry.homework_done.homework.text
            student_name = str(entry.homework_done.student)
            creation_date = entry.homework_done.created.strftime("%Y-%m-%d %H:%M:%S")
            teacher_name = str(entry.homework_done.homework.created_by)
            writer.writerow(
                {
                    "Homework": homework,
                    "Student name": student_name,
                    "Creation date": creation_date,
                    "Teacher name": teacher_name,
                }
            )


if __name__ == "__main__":
    import_to_csv()
