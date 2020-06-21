"""personal_finance_management_app URL Configuration

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

from personal_finance_management_app.views import (
    StatisticPageViewForConsumer,
    MainPageView,
    StatisticPageViewForBusiness,
    RegistrationForBusiness,
    RegistrationForConsumer,
    LogInToPersonalAccount,
    PersonalAccount,
    WritingOfExpensesByCheque, WritingOfExpensesManually)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainPageView.render_main_page),
    path('', MainPageView.render_main_page),
    path('', MainPageView.render_main_page),
    path('consumer-statistics/', StatisticPageViewForConsumer.display_expense_structure),
    path('business-statistics/', StatisticPageViewForBusiness.display_expense_structure),
    path('registration-for-business/', RegistrationForBusiness.register),
    path('registration-for-consumer/', RegistrationForConsumer.register),
    path('log-in/', LogInToPersonalAccount.log_in),
    path('personal-account/', PersonalAccount.entering_to_personal_account),
    path('consumer-expenses/', WritingOfExpensesByCheque.write_down_expenses),
    path('consumer-expenses-save/', WritingOfExpensesByCheque.save_of_cheque),
    path('consumer-expenses-manually/', WritingOfExpensesManually.write_down_expenses),
    path('consumer-statistics-periods/', StatisticPageViewForConsumer.display_periods),
    path('consumer-statistics-structure/', StatisticPageViewForConsumer.display_structure),
    path('consumer-statistics-structure-of-two-periods/', StatisticPageViewForConsumer.display_structure_of_two_periods),

]
