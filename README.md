# Скрипт для взлома электронного дневника и исправления в нём оценок

Проект создан для помощи Ване с его мечтой!

### Как пользоваться


#### 1. Исправить оценки


* Скачайте файл `scripst.py` и добавьте его в репозиторий с базой данных.
* Напишите в терминале ```python3 manage.py shell```.
* В открытом shell можете использовать команды из `scripst.py`.

```fix_marks(Фамилия Имя ученика)``` нужен для исправления всех плохих оценок на '5'.


```remove_chastisements(Фамилия Имя ученика)``` нужен для удаления замечаний в электронном дневнике.

```create_commendation(Фамилия Имя ученика, Предмет):``` нужен для сохдания похвалы по определенному предмету.

Очень важно записать фамилию и имя верно, так, как она записана в эл. дневнике.

Также Предмет следует писать с большой буквы.


### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).