from django.urls import path

from .views import RegistrationView, UserInfoView

urlpatterns = [
    path('registration/', RegistrationView.as_view(), name='registration'),
    path('info/', UserInfoView.as_view(), name='info')
]