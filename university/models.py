from django.db import models


class Group(models.Model):
    name = models.CharField(
        verbose_name='Название группы',
        max_length=100,
    )

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'

    def __str__(self):
        return f'Группа "{self.name}"'


class Student(models.Model):
    first_name = models.CharField(
        verbose_name='Имя',
        max_length=250,
    )
    last_name = models.CharField(
        verbose_name='Фамилия',
        max_length=250,
    )
    group = models.ForeignKey(
        Group,
        verbose_name='Группа',
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'

    def __str__(self):
        return f'{self.last_name} {self.first_name}'


class Lesson(models.Model):
    class Rooms(models.TextChoices):
        FIRST = '001', '001'
        SECOND = '002', '002'
        THIRD = '003', '003'

    class Time(models.TextChoices):
        NINE = '9', '09:00'
        ELEVEN = '11', '11:00'
        THIRTEEN = '13', '13:00'

    group = models.ForeignKey(
        Group, verbose_name='Группа', on_delete=models.CASCADE,
    )
    room = models.CharField('Аудитория', choices=Rooms.choices, max_length=50)
    time = models.CharField('Время начала', choices=Time.choices, max_length=50)

    class Meta:
        verbose_name = 'Занятие'
        verbose_name_plural = 'Занятия'

    def __str__(self):
        return f'{self.time}: {self.group} {self.room}'
