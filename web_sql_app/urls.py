from django.urls import path
from .views import MainView, Sp_Get_AmcomView, Sp_Get_TalonView, Sp_Accept_Amcom_PayView, HomeView
from django.contrib.auth.views import LogoutView
from django.conf import settings

urlpatterns = [
    path('', MainView.as_view(), name='signin'),
    path('home/', HomeView.as_view(), name='home'),
    path('sp_get_amcom/', Sp_Get_AmcomView.as_view(), name='sp_get_amcom'),
    path('sp_get_talon/', Sp_Get_TalonView.as_view(), name='sp_get_talon'),
    path('sp_accept_amcom_pay/', Sp_Accept_Amcom_PayView.as_view(), name='sp_accept_amcom_pay'),
    path('signout/', LogoutView.as_view(), {'next_page': settings.LOGOUT_REDIRECT_URL}, name='signout',),
]