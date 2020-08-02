from django.http import Http404
from django.http import HttpResponseNotFound, HttpResponseServerError
from django.shortcuts import render
from django.views import View

from app.models import Company
from app.models import Specialty
from app.models import Vacancy


# Create your views here.


def custom_handler404(request, exception):
    return HttpResponseNotFound('Ой, что то сломалось... Простите извините!')


def custom_handler500(request):
    return HttpResponseServerError('Ошибка на нашей стороне')


class HomeView(View):
    def get(self, request):
        specialties = Specialty.objects.all()
        companies = Company.objects.all()
        context = {
            'specialties': specialties,
            'companies': companies
        }
        return render(request, 'app/index.html', context=context)


class AllVacancies(View):
    def get(self, request):
        vacancy = Vacancy.objects.all()
        context = {
            'vacancy': vacancy
        }
        return render(request, 'app/all_vacancies.html', context=context)


class SpecialVacancies(View):
    def get(self, request, specialty_title_str):
        specialty_title = Specialty.objects.filter(code=specialty_title_str).first()
        if not specialty_title:
            raise Http404
        special_vacancies = Vacancy.objects.filter(skills=specialty_title_str)
        context = {
            'specialty_title': specialty_title,
            'special_vacancies': special_vacancies
        }
        return render(request, 'app/special_vacancies.html', context=context)


class CompanyCard(View):
    def get(self, request, company_id):
        company = Company.objects.filter(id=company_id).first()
        vacancy = Vacancy.objects.filter(compania=company.name)
        if not company:
            raise Http404

        context = {
            'company': company,
            'vacancy': vacancy
        }

        return render(request, 'app/company.html', context=context)


class Vacancies(View):
    def get(self, request, vacancy_id):
        vacancy = Vacancy.objects.filter(id=vacancy_id).first()
        if not vacancy:
            raise Http404
        context = {
            'vacancy': vacancy
        }
        return render(request, 'app/vacancy.html', context=context)
