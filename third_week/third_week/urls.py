"""third_week URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from app.views import AllVacancies
from app.views import CompanyCard
from app.views import custom_handler404
from app.views import custom_handler500
from app.views import HomeView
from app.views import SpecialVacancies
from app.views import Vacancies

handler404 = custom_handler404
handler500 = custom_handler500

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='index'),
    path('vacancies/', AllVacancies.as_view(), name='vacancies'),
    path('vacancies/cat/<str:specialty_title_str>/', SpecialVacancies.as_view()),
    path('companies/<int:company_id>/', CompanyCard.as_view()),
    path('vacancies/<int:vacancy_id>/', Vacancies.as_view()),
]
