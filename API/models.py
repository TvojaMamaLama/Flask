from django.db import models


class Qualification(models.Model):
    """Возможные квалификации инвестора"""
    QUALIFICATION_CHOICES = [
        ('NO', 'NO_QUALIFICATION'),
        ('GR', 'GRADUATE'),
        ('H6P', 'HAVE_6_IN_PAPER'),
        ('S6', 'SELL6'),
        ('H6D', 'HAVE_6_IN_DEPOSIT'),
        ('E2', 'EXPERIENCE_2_YEAR'),
        ('AQ', 'ALREADY_QUALIFIED'),
    ]
    status = models.CharField('Статус квалификации', choices=QUALIFICATION_CHOICES, blank=False, max_length=3)
    description = models.TextField('Описание квалификации')

    def __str__(self):
        return self.description


class Investor(models.Model):
    """Модель описывает данные о инвесторе и его паспорте"""
    name = models.CharField('Имя', max_length=50, blank=False)
    sur_name = models.CharField('Фамилия', max_length=60, blank=False)
    patronymic = models.CharField('Отчество', max_length=50, default='')
    birth_date = models.DateField('Дата рождения', blank=False)
    birth_place = models.CharField('Место рождения', max_length=30, blank=False)
    registration_address = models.CharField('Адрес регистрации', max_length=300, blank=False)
    passport_series_number = models.PositiveIntegerField('Серия и номер паспорта', blank=False)
    passport_department_code = models.PositiveIntegerField('Код подразделения паспорта', blank=False)
    passport_issue_date = models.DateField('Дата выдачи паспорта', blank=False)
    passport_issued_by = models.CharField('Кем выдан паспорт', max_length=300, blank=False)
    passport_photo_page = models.FileField(
        'Фото паспорта',
        blank=False,
        upload_to='passport/')
    passport_registration_page = models.FileField(
        'Фото регистрации',
        blank=False,
        upload_to='passport/')
    platform_rules = models.BooleanField('Принял правила', default=False)
    qualification = models.ManyToManyField(Qualification)

    def __str__(self):
        return f'{self.name} {self.sur_name}'
