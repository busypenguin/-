from datacenter.models import Schoolkid
from datacenter.models import Mark
from datacenter.models import Chastisement
from datacenter.models import Lesson
from datacenter.models import Commendation
import random


COMMENDATIONS = ['Хорошая работа!', 'Хвалю!', 'Молодец!', 'Как всегда прекрасно!', 'Продолжай стараться!', 'Так дежать']


def find_schoolkid(schoolkid_name):
    try:
        schoolkid = Schoolkid.objects.get(full_name__contains=schoolkid_name)
    except Schoolkid.MultipleObjectsReturned:
        print('Не удалось найти ученика')
        return
    except Schoolkid.DoesNotExist:
        print('Вы ошиблись')
        return


def fix_marks(schoolkid_name):
    schoolkid = find_schoolkid(schoolkid_name)
    child_bad_marks = Mark.objects.filter(schoolkid=schoolkid, points__lt=4)
    child_bad_marks.update(points=5)


def remove_chastisements(schoolkid_name):
    schoolkid = find_schoolkid(schoolkid_name)
    schoolkid_chastisement = Chastisement.objects.filter(schoolkid=schoolkid)
    schoolkid_chastisement.delete()


def create_commendation(schoolkid_name, subject):
    schoolkid = find_schoolkid(schoolkid_name)
    certain_lessons = Lesson.objects.order_by(subject__title=subject, year_of_study=schoolkid.year_of_study, group_letter=schoolkid.group_letter)
    certain_lesson = certain_lessons.first()
    Commendation.objects.create(text=random.choice(COMMENDATIONS), created=certain_lesson.date, schoolkid=schoolkid, subject=certain_lesson.subject, teacher=certain_lesson.teacher)
