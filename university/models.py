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
