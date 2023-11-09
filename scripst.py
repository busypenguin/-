from datacenter.models import Schoolkid
from datacenter.models import Mark
from datacenter.models import Chastisement
from datacenter.models import Lesson
from datacenter.models import Commendation


def fix_marks(schoolkid_name):
    schoolkid = Schoolkid.objects.get(full_name__contains=schoolkid_name)
    child_bad_marks = Mark.objects.filter(schoolkid=schoolkid, points__lt=4)
    for bad_mark in child_bad_marks:
        bad_mark.points = 5
        bad_mark.save()


def remove_chastisements(schoolkid_name):
    schoolkid = Schoolkid.objects.get(full_name__contains=schoolkid_name)
    schoolkid_chastisement = Chastisement.objects.filter(schoolkid=schoolkid)
    schoolkid_chastisement.delete()


def create_commendation(schoolkid_name, subject):
    schoolkid = Schoolkid.objects.get(full_name__contains=schoolkid_name)
    lessons_subject = Lesson.objects.filter(subject__title=subject, year_of_study=schoolkid.year_of_study, group_letter=schoolkid.group_letter)
    lesson_subject = lessons_subject[0]
    Commendation.objects.create(text='Хвалю', created=lesson_subject.date, schoolkid=schoolkid, subject=lesson_subject.subject,teacher=lesson_subject.teacher)


create_commendation('Фролов Иван', 'Музыка')