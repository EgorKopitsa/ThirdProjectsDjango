from django.db import models

# Create your models here.


class Company(models.Model):
    name = models.CharField(max_length=20)
    location = models.CharField(max_length=20)
    logo = models.CharField(max_length=20, default='https://place-hold.it/100x60')
    description = models.CharField(max_length=200)
    employee_count = models.IntegerField()

    def __str__(self) -> str:
        return f'{self.name} {self.location} {self.description} {self.employee_count}'


class Specialty(models.Model):
    code = models.CharField(max_length=10)
    title = models.CharField(max_length=10)
    picture = models.CharField(max_length=20, default='https://place-hold.it/100x60')

    def __str__(self) -> str:
        return f'{self.code} {self.title}'


class Vacancy(models.Model):
    title = models.CharField(max_length=10)
    specialty = models.ForeignKey(Specialty, on_delete=models.CASCADE, related_name="vacancies")
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="vacancies")
    compania = models.CharField(max_length=15, default='')
    skills = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    salary_min = models.IntegerField()
    salary_max = models.IntegerField()
    published_at = models.CharField(max_length=10)

    def __str__(self) -> str:
        return f'{self.title} {self.specialty} {self.company} {self.skills} {self.description} {self.salary_max}' \
               f' {self.salary_min} {self.published_at} {self.compania} '
